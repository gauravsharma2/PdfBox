#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import git
import csv
import tqdm
import re


# specify the path to the Git repository
repo_path = "/Users/gauravsharma/Desktop/pdfbox"

# create a Git repo object
repo = git.Repo(repo_path)

commits = repo.iter_commits()

lookup = {}
output = []

issue_pattern = r'\bPDFBOX-\d+\b'
counter = 0


counter=0
for c in commits:
    print(counter)
    issues_addressed = re.findall(issue_pattern, c.message)
    
    commit_details = {
        "commit_hash" : c.hexsha,
        "M" : 0,
        "A" : 0,
        "D" : 0
    }
    modified_files = [item.a_path for item in c.diff() if item.change_type == "M"]
    num_modified_files = len(modified_files)
    commit_details["M"]+= num_modified_files

    added_files = [item.a_path for item in c.diff() if item.change_type == "A"]
    num_added_files = len(added_files)
    commit_details["A"]+= num_added_files

    deleted_files = [item.a_path for item in c.diff() if item.change_type == "D"]
    num_deleted_files = len(deleted_files)
    commit_details["D"]+= num_deleted_files

    for issue in issues_addressed:
        if issue not in lookup:
            lookup[issue] = [commit_details]
        else:
            lookup[issue].append(commit_details)
    counter+=1


for key in lookup.keys():
    c_details = lookup[key]
    for c in c_details:
        output.append([key,  c["commit_hash"], c["M"], c["A"], c["D"]])



with open('final_output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['issue_id', 'commit_hash', 'M', 'A', 'D'])
    writer.writerows(output)
