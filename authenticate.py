import requests
import requests.auth
import json

with open("config.json") as json_file:
    config = json.load(json_file)

# client_auth = requests.auth.HTTPBasicAuth('p-jcoLKBynTLew', 'gko_LXELoV07ZBNUXrvWZfzE3aI')
client_auth = requests.auth.HTTPBasicAuth(config["client_id"], config["client_secret"])

post_data = {"grant_type": "password", "username": config["username"], "password": config["password"]}
headers = {"User-Agent": "fmf_listener/0.1 by " + config["username"]}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

outF = open("auth.json", "w")
outF.write(str(response.json()).replace("'", '"'))
print(response.json())
outF.close()
