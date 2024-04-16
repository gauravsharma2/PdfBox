import git
import json


# specify the path to the Git repository
repo_path = "/Users/gauravsharma/Desktop/pdfbox"

# create a Git repo object
repo = git.Repo(repo_path)

commits = repo.iter_commits()

commit_data = {}


for c in commits:
    commit_data[c.hexsha] = [item.a_path for item in c.diff()]

with open("data.json", "w") as o: 
    json.dump(commit_data, o)
