import json
import urllib2

try:
    res = urllib2.urlopen("https://api.github.com/orgs/ionian-uni-ieee/repos")
except Exception as e:
    print(e)
    raise SystemExit

try:
    repos = json.load(res)
except Exception as e:
    print(e)
    raise SystemExit

try:
    res.close()
except Exception as e:
    print(e)
    raise SystemExit


for repo in repos:
    name = repo['name']
    stars = repo['stargazers_count']
    forks = repo['forks_count']

    print('------------------------')
    print('Name: ' + name)
    print('Forks: ' + str(forks))
    print('Stars: ' + stars)
    # add print statement here
    print('------------------------')
    print('')
