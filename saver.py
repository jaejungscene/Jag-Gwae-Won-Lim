import urllib
import json
import os

ROOT = os.path.abspath(os.getcwd())

name = "강력20kg"
query = urllib.parse.quote(name)

url = f"https://openapi.naver.com/v1/search/shop?query={query}"
client_id = "4OQMv3YxrKsVojrlewHN"
client_secret = "v7mCeaUi1B"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
response = response.read().decode("utf-8")
response = json.loads(response)

with open(f"{ROOT}/data/{query}.json", "w") as f:
    json.dump(response, f)