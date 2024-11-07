class logicOperators:
    def __init__(self):
        pass
    def andOperator(self, dic1, dic2):
        c1=set()
        for key in dic1:
            c1.add(key)
        c2=set()
        for key in dic2:
            c2.add(key)
        res = c1.intersection(c2)
        return res
    def orOperator(self, dic1, dic2):
        c1=set()
        for key in dic1:
            c1.add(key)
        c2=set()
        for key in dic2:
            c2.add(key)
        res = c1.union(c2)
        return res
    def notOperator(self,dic1,postingList):
        c=set()
        dic1=set(dic1)
        for key in postingList:
            for doc in postingList[key]:
                c.add(doc)
        res = set()
        for doc in c:
            if doc not in dic1:
                res.add(doc)
        return res
