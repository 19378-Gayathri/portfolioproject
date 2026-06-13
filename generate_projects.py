import requests
import json
import os

USERNAME = "19378-Gayathri"

TOKEN = os.environ["TOKEN_CUSTOM"]

url = f"https://api.github.com/users/{USERNAME}/repos"

headers = {
    "Authorization": f"token {TOKEN}"
}

response = requests.get(url, headers=headers)

repos = response.json()

projects = []

for repo in repos:

    projects.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"],
        "language": repo["language"]
    })

with open("projects.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, indent=4)

print("projects.json updated")
