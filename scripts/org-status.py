
import json
import urllib2

try:
    res = urllib2.urlopen("https://api.github.com/repos/ionian-uni-ieee/git")
except Exception as e:
    print(e)
    raise SystemExit

try:
    repo = json.load(res)
except Exception as e:
    print(e)
    raise SystemExit

try:
    res.close()
except Exception as e:
    print(e)
    raise SystemExit

name = repo['name']
stars = repo['stargazers_count']

print('------------------------')
print('Name: ' + name)
print('Stars: ' + str(stars))
print('------------------------')
#εγω οταν το τρεχω λόκαλι μονο για ενα ρέπο μου βγάζει (για το /git δλδ) αρα μάλλον δεν πειραζω κατι
#wait i did it! highkey shooketh
