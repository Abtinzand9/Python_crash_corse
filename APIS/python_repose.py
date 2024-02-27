import requests

# make an api call 
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept' : "application/vnd.github.v3+json"}
r = requests.get(url , headers=headers)
print(f"status code : {r.status_code}")
# Convert the response object to a dictionary.
response_dict = r.json()
print(f"total repositoris {response_dict['total_count']}")
print(f"complete resulte { not response_dict['incomplete_results']}")
# explore information about repositories
repo_dicts = response_dict['items']
print(f"repositories returned {len(repo_dicts)}")

# examine the first repository
repo_dict = repo_dicts[0]
""" print(f"\nkeys : {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key) """
print(f"\n Selected information about each repo")
for repo_dict in repo_dicts:
    print(f"\nName : {repo_dict['name']}")
    print(f"Owner : {repo_dict['owner']['login']}" )
    print(f"Stars : {repo_dict['stargazers_count']}")
    print(f"Repository : {repo_dict['html_url']}")
    print(f"Created : {repo_dict['created_at']}")
    print(f"Updated : {repo_dict['updated_at']}")
    print(f"Description : {repo_dict['description']}")