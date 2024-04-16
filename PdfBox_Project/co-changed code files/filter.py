from pydriller import Repository
import json

data = {}

for commit in Repository("https://github.com/apache/pdfbox").traverse_commits():
    for file in commit.modified_files:
        if file.change_type.name == "DELETE":
            if commit.hash in data:
                data[commit.hash].append(file.old_path)
            else:
                data[commit.hash] = [file.old_path]
        else:
            if commit.hash in data:
                data[commit.hash].append(file.new_path)
            else:
                data[commit.hash] = [file.new_path]

with open("input.json", "w") as output: 
    json.dump(data, output)