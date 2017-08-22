import urllib.request, urllib.parse, urllib.error
import json
url = 'http://py4e-data.dr-chuck.net/comments_12592.json'
data =  urllib.request.urlopen(url).read().decode('utf-8')
info = json.loads(data)
total = 0
for comment in info["comments"]:
    total += int(comment["count"])

print ('total: ', total)
