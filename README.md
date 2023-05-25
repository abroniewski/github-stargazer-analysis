# GitHub User Analytics Tool

This Python project fetches, analyzes, and presents data from GitHub users who have starred a specific repository. It uses GitHub's API to obtain detailed user information and provides insights into the stargazers of any chosen GitHub repository.

This project is authored by Adam Broniewski. For more information, please visit the author's [website](www.adambron.com) and [LinkedIn profile](https://www.linkedin.com/in/abroniewski/).

## Features
1. **Fetching user data**: User details including username, type, name, company, location, blog, email, followers count, etc. are gathered.
2. **Saving user data**: The fetched user data is stored in a CSV file for future reference and offline analysis.
3. **Analyzing user data**: The tool provides an analysis of the users such as top companies by the number of followers and top users with the most followers.
4. **Rate Limit Handling**: The tool is respectful of GitHub's rate limit for API requests and will pause when the limit is reached, resuming automatically once it resets.
5. **Progress Display**: The fetching process displays a progress bar, making it easy to monitor.

## Usage
Run the main script in the command line. It will prompt you whether you want to fetch new user data. If you select 'yes', the script will fetch and store user data in a CSV file. If you select 'no', it will load previously fetched user data. After loading the data, it will present an analysis.

## Steps to Clone, Install Requirements, and Run

1. Clone the repository using git:

    ```
    git clone https://github.com/abroniewski/github-stargazer-analysis.git
    ```

2. Navigate into the project directory:

    ```
    cd repo
    ```

3. Create a new Conda environment:

    ```
    conda create -n env_name python=3.8
    ```

    Replace `env_name` with your preferred name for the environment.

4. Activate the Conda environment:

    ```
    conda activate env_name
    ```

5. Install the required packages using the `requirements.txt` file:

    ```
    pip install -r requirements.txt
    ```

6. Create a `config.py` file in the root directory of the project, and add your GitHub API token:

    ```python
    token = "YOUR_GITHUB_API_TOKEN"
    ```

7. Run the script:

    ```
    python main.py
    ```

    You will be prompted to enter the repository owner's name and the repository name, and whether you wish to fetch new user data.

## Requirements
- Python 3.6+
- `requests` package
- `pandas` package
- `tqdm` package
- `tabulate` package
- Personal GitHub access token

## Author
Adam Broniewski - [Website](www.adambron.com) | [LinkedIn](https://www.linkedin.com/in/abroniewski/)

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Acknowledgments
This code was written with assistance from OpenAI's ChatGPT.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

**NOTE**: This tool should be used in compliance with the GitHub API Terms of Service.