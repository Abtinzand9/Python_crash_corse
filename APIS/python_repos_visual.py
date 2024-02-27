import requests
import plotly.express as px

# make an api call 
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept' : "application/vnd.github.v3+json"}
r = requests.get(url , headers=headers)
print(f"status code : {r.status_code}")

# process overall results 
response_dict = r.json()
print(f"complete resulte { not response_dict['incomplete_results']}")

# process repository information
repo_dicts = response_dict['items']
repo_names , stars = [] , []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make visualization
fig = px.bar(x = repo_names , y = stars)
fig.show()