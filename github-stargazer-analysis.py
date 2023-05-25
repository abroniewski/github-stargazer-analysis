import time
import requests
import pandas as pd
from tqdm import tqdm
from tabulate import tabulate
from config import token    # create a config.py file with your GitHub token

BASE_URL = "https://api.github.com"

def get_headers(token):
    return {'Authorization': f'token {token}'}

def check_rate_limit(token):
    url = f"{BASE_URL}/rate_limit"
    response = requests.get(url, headers=get_headers(token))
    rate_limit_data = response.json()
    return rate_limit_data['resources']['core']

def get_total_stargazers(token, repo_owner, repo_name):
    url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}"
    response = requests.get(url, headers=get_headers(token))
    repo_data = response.json()
    return repo_data['stargazers_count']

def handle_rate_limit(token):
    rate_limit = check_rate_limit(token)
    if rate_limit['remaining'] == 0:
        reset_time = rate_limit['reset']
        sleep_time = reset_time - time.time() + 5
        print(f"Rate limit exceeded. Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)

def get_stargazers(token, repo_owner, repo_name):
    session = requests.Session()
    session.headers.update(get_headers(token))

    url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}/stargazers"
    total_stargazers = get_total_stargazers(token, repo_owner, repo_name)
    users = []

    progress_bar = tqdm(total=total_stargazers, desc="Fetching user data")

    while url:
        handle_rate_limit(token)

        response = session.get(url)
        response_json = response.json()

        for user in response_json:
            user_url = f"{BASE_URL}/users/{user['login']}"
            user_response = session.get(user_url)
            user_data = user_response.json()

            users.append({
                'login': user_data.get('login'),
                'type': user_data.get('type'),
                'name': user_data.get('name'),
                'company': user_data.get('company'),
                'blog': user_data.get('blog'),
                'location': user_data.get('location'),
                'email': user_data.get('email'),
                'hireable': user_data.get('hireable'),
                'bio': user_data.get('bio'),
                'twitter_username': user_data.get('twitter_username'),
                'public_repos': user_data.get('public_repos'),
                'public_gists': user_data.get('public_gists'),
                'followers': user_data.get('followers'),
                'following': user_data.get('following'),
                'created_at': user_data.get('created_at'),
                'updated_at': user_data.get('updated_at')
            })

            progress_bar.update(1)

        links = response.headers.get('Link', '').split(', ')
        url = next((link[link.index('<')+1:link.index('>')] for link in links if 'rel="next"' in link), None)

    progress_bar.close()
    return users


def load_stargazers(repo_name):
    return pd.read_csv(f'{repo_name}_stargazers.csv')

def analyze_stargazers(df, repo_name):
    print(f"\nAnalyzing users for repository: {repo_name}")
    print(f"Number of users being analyzed: {len(df)}")
    print("\nTop companies by number of followers:")
    top_companies = df.groupby('company')['followers'].sum(numeric_only=True).sort_values(ascending=False).head(10)
    print(tabulate(top_companies.reset_index(), headers=['Company', 'Followers'], tablefmt='pretty', showindex=False))
    print("\nTop 20 users with most followers:")
    top_users = df.sort_values(by='followers', ascending=False)[['name', 'company', 'blog', 'location', 'email', 'followers']].head(20)
    print(tabulate(top_users, headers='keys', tablefmt='pretty', showindex=False))

if __name__ == "__main__":
    repo_owner = "pgRouting"           # replace with your choice
    repo_name = "pgrouting"            # replace with your choice

    fetch_users = input("\nDo you want to fetch new user data? (y/n): ")
    if fetch_users == "y":
        fetch_users2 = input("Are you sure? (y/n): ")
        if fetch_users2 == "y":
            stargazers = get_stargazers(token, repo_owner, repo_name)
            df = pd.DataFrame(stargazers)
            df.to_csv(f'{repo_name}_stargazers.csv', index=False)
        else:
            print("No users fetched.\n")
    else:
        print("No users fetched.\n")
        
    df = load_stargazers(repo_name)
    analyze_stargazers(df, repo_name)