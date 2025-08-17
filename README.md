# Lang-O-Meter

A GitHub Language Stats Analyser. This Python script retrieves and analyses a user's public GitHub repositories to calculate the percentage distribution of programming languages used. It then displays the results in a formatted list and can optionally generate a pie chart visualisation.

-----

## Features

  - Fetches a list of all public repositories for a given GitHub user.
  - Calculates the total lines of code (in bytes) for each programming language.
  - Outputs a sorted list of language percentages.
  - Optionally displays a **pie chart** showing the language distribution in a separate window.

-----

## Requirements

You need to have Python installed on your system. The script also requires a few external libraries. You can install them using `pip`:

```bash
pip install requests matplotlib
```

## How to Use

1.  **Clone the repository** or save the code into a Python file (e.g., `git_stats.py`).

2.  **Generate a GitHub Personal Access Token.**

      * Go to your GitHub account **Settings**.
      * Navigate to **Developer settings** -\> **Personal access tokens** -\> **Tokens (classic)**.
      * Click **Generate new token**.
      * Give it a descriptive name (e.g., "Language Stats Script").
      * No specific scopes are required for public repositories, so you can leave them all unchecked.
      * Click **Generate token** and **copy the token**. Keep this token secure; you will need it to run the script.

3.  **Run the script** from your terminal:

    ```bash
    python git_stats.py
    ```

4.  **Follow the prompts:** The script will ask for the GitHub username and the Personal Access Token you just created.

5.  **View the results:** The language percentages will be printed to the console. You will then be asked if you want to see a pie chart visualisation. Type `y` to display the chart or `n` to exit.

-----

## Example Output

```
Fetching repositories for user: example_user...
Found 15 repositories. Calculating language stats...

--- Language Distribution Across All Repositories ---
Python: 65.34%
JavaScript: 20.10%
HTML: 8.52%
CSS: 4.02%
C++: 2.02%

Do you want to see this distribution as a pie chart? (y/n): y

Displaying pie chart in a new window...
```
