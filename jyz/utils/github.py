import requests
import json
import os
from datetime import datetime
from blogsite.settings.base import PROJECT_ROOT_DIR


def fetch_user_repositories(username, forked=False):
    github_search_api = "https://api.github.com/search/repositories?q=user:{username}+fork:{forked}"
    forked = "true" if forked else "false"

    request_repo = requests.get(github_search_api.format(
        username=username,
        forked=forked,
    ))
    repos = request_repo.json()

    repositories = []

    for repo in repos['items']:
        repositories.append({
            'name': repo['name'],
            'full_name': repo['full_name'],
            'url': repo['html_url'],
            'description': repo['description'],
            'language': repo['language'] if repo['language'] else None,
        })

    return repositories


def write_user_repositories(username, forked=False, filename='github_metadata.json'):
    github_metadata_dir = os.path.join(PROJECT_ROOT_DIR, filename)
    repository = {}
    today = datetime.now().strftime("%Y%m%d")

    # Check if json file already exists
    if not os.path.exists(github_metadata_dir):
        repository['repos'] = fetch_user_repositories(username=username, forked=forked)
        repository['date_modified'] = datetime.now().strftime("%Y%m%d")

    else:
        # Since path exists, try to load the file and check for date_modified
        # If the file exists and modified date is not equal to today,
        # we should fetch the updated list of repositories...
        with open(github_metadata_dir) as f:
            data = json.load(f)
            if not data['date_modified'] == today:
                repository['repos'] = fetch_user_repositories(username=username, forked=forked)
                repository['date_modified'] = datetime.now().strftime("%Y%m%d")
            else:
                return

    # We can now write it to the file.
    with open(github_metadata_dir, 'w') as f:
        json.dump(repository, f)


def load_user_repositories(username, forked=False, filename='github_metadata.json', load_cached=True):
    github_metadata_dir = os.path.join(PROJECT_ROOT_DIR, filename)
    write_user_repositories(username=username, forked=False)

    if not load_cached:
        repositories = fetch_user_repositories(username=username, forked=False)
        return repositories

    with open(github_metadata_dir) as f:
        data = json.load(f)
    return data['repos']
