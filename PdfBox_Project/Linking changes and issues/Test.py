import json
import pandas as pd

f = open('issue.json')
 
isd = json.load(f)

std = {"BUG":[],"cm":[],"Added":[], "Modified":[],"Deleted":[]}

for i in isd.keys():
    added = 0
    modified = 0
    deleted = 0
    cml = []
    cm = isd[i]
    for c in cm:
        cml.append(c["cmt_hash"])
        modified+=c["modified_files"]
        deleted+=c["deleted_files"]
        added+=c["added_files"]
    std["BUG"].append(i)
    std["cm"].append(cml)
    std["Added"].append(added)
    std["Modified"].append(modified)
    std["Deleted"].append(deleted)

df = pd.DataFrame(std)
df.to_csv("solution.csv",index=False)