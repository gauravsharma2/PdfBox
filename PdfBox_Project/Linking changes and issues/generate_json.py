#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pydriller import Repository
import re
import json

dict = {}
for cmt in Repository("https://github.com/apache/pdfbox").traverse_commits():
        
        iss = []  
        pt = r'\bPDFBOX-\d+\b' 
        iss = re.findall(pt, cmt.msg)
        cmtd = {
                "cmt_hash":cmt.hash,
                "added_files" : 0,
                "deleted_files" : 0,
                "modified_files" : 0  
        }

        for file in cmt.modified_files:
            if file.change_type.name == "ADD":
                cmtd["added_files"]+=1
            if file.change_type.name == "DELETE":
                cmtd["deleted_files"]+=1
            if file.change_type.name == "MODIFY":
                cmtd["modified_files"]+=1
        
        for isd in iss:
            if isd in dict:
                dict[isd].append(cmtd)
            else:
                dict[isd] = [cmtd]

# saving the generated data in pr_data.json file
with open("issue.json", "w") as outfile: 
    json.dump(dict, outfile)

