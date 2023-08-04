import requests

# GitHub API endpoint for commits
repo_owner = 'Neivanny1'
repo_name = 'alx-low_level_programming'
api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'

# Make a GET request to fetch commit data
response = requests.get(api_url)

if response.status_code == 200:
    commits = response.json()
    print(f"Total number of commits: {len(commits)}")

    for commit in commits:
        commit_data = commit['commit']
        author = commit_data['author']['name']
        message = commit_data['message']
        print(f"Author: {author}\nMessage: {message}\n")
        print(f"Total commits {len(commits)}")
else:
    print(f"Failed to fetch commits. Status code: {response.status_code}")
