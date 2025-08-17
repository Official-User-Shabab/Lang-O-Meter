import requests
import sys
import matplotlib.pyplot as plt

def get_user_language_stats(username, token):
    """
    Calculates the total language percentage across a user's public GitHub repositories.

    Args:
        username (str): The GitHub username to analyse.
        token (str): A GitHub Personal Access Token for authentication.

    Returns:
        dict: A dictionary with language percentages.
    """
    base_url = "https://api.github.com"
    headers = {
        "Authorisation": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    #  get a list of all public repositories for the user
    repos_url = f"{base_url}/users/{username}/repos"
    print(f"Fetching repositories for user: {username}...")
    try:
        response = requests.get(repos_url, headers=headers)
        response.raise_for_status() # Raise exception for bad status codes
        repos = response.json()
    except requests.exceptions.HTTPError as err:
        print(f"An HTTP error occurred: {err}")
        return {}
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return {}

    if not repos:
        print(f"No public repositories found for user '{username}'.")
        return {}

    total_language_bytes = {}
    print(f"Found {len(repos)} repositories. Calculating language stats...")

    #Iterate through each repository to get its language breakdown
    for repo in repos:
        repo_name = repo['name']
        languages_url = repo['languages_url']
        
        try:
            lang_response = requests.get(languages_url, headers=headers)
            lang_response.raise_for_status()
            repo_languages = lang_response.json()
            
            #  Sum the language bytes across all repositories
            for language, bytes_of_code in repo_languages.items():
                if language in total_language_bytes:
                    total_language_bytes[language] += bytes_of_code
                else:
                    total_language_bytes[language] = bytes_of_code
        
        except requests.exceptions.HTTPError as err:
            print(f"Warning: Could not get languages for repository '{repo_name}'. Error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Warning: Could not get languages for repository '{repo_name}'. Error: {err}")
    
    # calculate the total percentage for each language
    total_bytes = sum(total_language_bytes.values())
    
    if total_bytes == 0:
        print("No code was found to calculate percentages.")
        return {}

    language_percentages = {
        lang: (bytes_count / total_bytes) * 100 
        for lang, bytes_count in total_language_bytes.items()
    }
    
    #sort the dictionary by percentage in descending order
    sorted_percentages = sorted(language_percentages.items(), key=lambda item: item[1], reverse=True)
    
    return dict(sorted_percentages)

def create_pie_chart(stats):
    """
    Generates a pie chart from the language percentage data.

    Args:
        stats (dict): A dictionary with language percentages.
    """
    if not stats:
        print("Cannot create a pie chart: No language data available.")
        return

    # Prepare data for plotting
    labels = list(stats.keys())
    sizes = list(stats.values())
    
    # creates pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    print("\nDisplaying pie chart in a new window...")
    plt.show()



if __name__ == "__main__":
    github_username = input("Enter the GitHub username: ")
    github_token = input("Enter your GitHub Personal Access Token: ")

    language_stats = get_user_language_stats(github_username, github_token)
    
    if language_stats:
        print("\n--- Language Distribution Across All Repositories ---")
        for language, percentage in language_stats.items():
            print(f"{language}: {percentage:.2f}%")
        
        see_chart = input("\nDo you want to see this distribution as a pie chart? (y/n): ")
        if see_chart.lower() == 'y':
            create_pie_chart(language_stats)
    else:
        print("Failed to retrieve language stats.")
