import json
import os
import time
class sistemaIR:
    def __init__(self):
        pass
    def createPostingList(self, pathFiles):
        postingList={}
        docs=os.listdir(pathFiles)
        for  doc in docs:
            pathDoc=pathFiles+'/'+doc
            with open(pathDoc, 'r') as f:
                txt=f.read()
                words=txt.split()
            for i, word in enumerate(words):
                if word not in postingList:
                    postingList[word] = {}
                if doc not in postingList[word]:
                    postingList[word][doc]=[]
                postingList[word][doc].append(i)
        with open('appWeb/SRI/files/postingList.json','w') as f:
            json.dump(postingList,f, ensure_ascii=False)
run=sistemaIR()
print('creando postingList')
inicio = time.time()
run.createPostingList('appWeb/SRI/corpusText1')
fin = time.time()
print(f'El posting list fue creado en {fin - inicio} segundos')