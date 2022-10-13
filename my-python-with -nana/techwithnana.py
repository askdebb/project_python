import requests
import datetime

response = requests.get("https://api.github.com/users/askdebb/repos")

myGitHubRepos = response.json()

chris_repo = open('chris_github_repos.doc', 'w')
chris_repo.write(
    'GitHub Handle||@askdebb||C.W. Debrah||Time Scrapped is: {}\n\n'.format(datetime.datetime.today()))
for repo in myGitHubRepos:
    all_repos = "My GitHub repo: {} \nRepo Url: {}\n\n".format(
        repo['name'], repo['url'])
    print(all_repos)

    for reps in all_repos:
        chris_repo = open('chris_github_repos.doc', 'a')
        chris_repo.write(reps)

chris_repo.close
