from motorBusqueda.MSRI.logica.logicOperators import logicOperators
import re
class busquedaAvanzada:
    def __init__(self, postingList, synonymsOperators):
        self.postingList = postingList
        self.synonymsOperators = synonymsOperators
    def formatoSalida(self, resDocs):
        res = []
        for doc in resDocs:
            doc=doc.replace('.txt','.png')
            time = int(doc.replace('.png','').replace('frame_',''))
            horas = (time*5) // 3600
            minutos = ((time*5) % 3600) // 60
            segundos = (time*5) % 60
            time = f'La imagen se encuentra en el tiempo {str(horas).zfill(2)}:{str(minutos).zfill(2)}:{segundos}'
            res.append((doc, [] ,time))
        return res
    def busquedaLogica(self,operator,query):
        res = []
        sinonimos = []
        correccion = []
        lo=logicOperators()
        query=query.split()
        if operator == 'OR' and len(query)==3:
            dic1 = self.postingList[query[0]]
            dic2 = self.postingList[query[2]]
            resDocs = lo.orOperator(dic1,dic2)
            print('here1')
            res = self.formatoSalida(resDocs)
        if operator == 'AND' and len(query)==3:
            dic1 = self.postingList[query[0]]
            dic2 = self.postingList[query[2]]
            resDocs = lo.andOperator(dic1,dic2)
            res = self.formatoSalida(resDocs)
        if operator == 'NOT' and len(query)==2:
            dic1 = self.postingList[query[1]]
            resDocs = lo.notOperator(dic1,self.postingList)
            res = self.formatoSalida(resDocs)
        return res, sinonimos, correccion
    def identificar(self,query):
        logicoperators = r"NOT|AND|OR"
        if re.search(logicoperators,query):
            oroperator="OR"
            andoperator="AND"
            notoperator="NOT"
            if re.search(oroperator,query):
                res=self.busquedaLogica('OR',query)
            if re.search(andoperator,query):
                res=self.busquedaLogica('AND',query)
            if re.search(notoperator,query):
                res=self.busquedaLogica('NOT',query)
            return res
        for key in self.synonymsOperators:
            if re.search(key, query):
                query = query.replace(key,self.synonymsOperators[key])
                res=self.busquedaLogica(self.synonymsOperators[key],query)
                return res
        comodin = r"[*]"
        if re.search(comodin,query):
            return self.busquedaComodin(query)