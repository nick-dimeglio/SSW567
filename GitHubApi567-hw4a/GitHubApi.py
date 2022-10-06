import requests
import json


def main():
    # get user input
    user = input("Enter a GitHub username: ")
    repos = getRepos(user)
    if repos is not None:
        for item in repos:
            print("Repo: " + item[0] + " Number of commits: " + str(item[1]))


def getRepos(user):
    # get repos from github
    url = "https://api.github.com/users/" + user + "/repos"
    response = requests.get(url)
    repos = json.loads(response.text)
    repoNames = []
    commits = 0
    if repos is not None and "message" not in repos:
        for item in repos:
            repoName = item["name"]
            commits = getCommits(repoName, user)
            repoNames.append([repoName, commits])
    else:
        print("No repos found for user " + user)
        return None
    return repoNames


def getCommits(repoName, user):
    # get commits from github
    url = "https://api.github.com/repos/" + user + "/" + repoName + "/commits"
    response = requests.get(url)
    commits = json.loads(response.text)
    print(commits, url)
    # Just in case the repo is fully empty
    if commits is not None and "message" not in commits:
        return len(commits)
    else:
        return 0
