__doc__ = """
Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:
"""

import requests


def get_github_repositories(username):
    url = 'https://api.github.com/users/{}/repos'.format(username)
    r = requests.get(url)
    list_repos = []
    for repos in r.json():
        list_repos.append(repos['name'])
    return list_repos


def main():
    import sys
    username = sys.argv[1]
    links = get_github_repositories(username)
    for (idx, repos_name) in list(enumerate(links, start=1)):
        print('{}: {}'.format(idx, repos_name))


if __name__ == "__main__":
    main()
