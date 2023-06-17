import json
import urllib.request

url = "https://py4e-data.dr-chuck.net/comments_1829699.json"

response = urllib.request.urlopen(url)
data = response.read().decode()

info = json.loads(data)

count_sum_comments = 0

for item in info["comments"]:
    count_sum_comments += int(item["count"])

print("total count:", count_sum_comments)
