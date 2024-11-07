import json

with open('SRI/files/postingList.json', 'r') as f:
    postingList = json.load(f)
with open('SRI/files/sinonimosDic.json', 'r') as f:
    sinonimosDic = json.load(f)
with open('SRI/files/dicBigram.json', 'r') as f:
    bigramDic = json.load(f)
with open('SRI/files/synonymsOperators.json', 'r') as f:
    synonymsOperators = json.load(f)