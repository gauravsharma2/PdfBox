from collections import defaultdict
from itertools import combinations

import json

import pandas as pd
f = open('input.json')
nf=1
cf = json.load(f)
cf=list(cf.items())
cf=sorted(cf,key=lambda x:x[0])
tf=set()
for commit,files in cf:
    for file in files:
        tf.add(file)
tf=list(tf)
tf=sorted(tf)
ccf = defaultdict(list)
for i in range(0,len(tf),nf):
    cuf=[]
    if i+nf>=len(tf):
        break
    for index in range(i,i+nf):
        cuf.append(tf[index])
    for commit,files in cf:
        files=set(files)
        flag=True 
        for file in cuf:
            if file not in files:
                flag=False 
        if(flag):
            ccf[tuple(cuf)].append(commit)

fls=[]
for tup in ccf:
    if len(ccf[tup])>=3:
        fls.append([tup,ccf[tup]])

fls=sorted(fls,key=lambda x:-len(x[1]))
fls = {files: commits for files, commits in fls}

fll = {"File changed" : [], "Commitid" : []}
for files, commits in fls.items():
    commit_str = ""
    file_str = ""
    for i,commit in enumerate(commits):
        commit_str += f"{i+1}.{commit} "
    for file_name in files:
        file_str+= f"{file_name} "
    fll["File changed"].append("\n".join(file_str.strip().split()))
    fll["Commitid"].append("\n".join(commit_str.strip().split()))

df = pd.DataFrame(fll)
df.to_csv(f"{nf}co-changed set.csv",index=False)
