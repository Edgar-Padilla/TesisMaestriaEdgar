from motorBusqueda.MSRI.gramatica.leven import distance
class correccion:
    def __init__(self):
        pass
    def convertirPalabra(self,palabra):
        return "$"+palabra+"$"
    #Obtner lista de bigramas de $palabra$
    def crearListaBigramas(self,palabra):
        res=[]
        for i in range(len(palabra)-1):
            bigrama = palabra[i]+ palabra[i+1]
            res.append(bigrama)
        return res
    #Obtener diccionario de bigramas
    def extraerDicBigramas(self,bigramas, bigramDic):
        res={}
        for bigrama in bigramas:
            if bigrama in bigramDic:
                res[bigrama]=bigramDic[bigrama]
        return res
    #Extraer lista de palabras del diccionario de bigramas
    def extraerPalabras(self,dic):
        res=set()
        for key in dic:
            for item in dic[key]:
                res.add(item)
        return res
    #mide la distancia de leven* entre una palabra y un conjunto de palabras y crea
    #un diccionario cuayas claves son la distancia de levin* y los items las palabras
    #que tienen esta distancia
    def listLeven(self,palabra1,list_palabras):
        dic={}
        for palabra2 in list_palabras:
            dis=distance(palabra1,palabra2)
            if dis not in dic:
                dic[dis]=[]
            dic[dis].append(palabra2)
        res={}
        #ordenar por distancia de menor a mayor
        for key in sorted(dic.keys()):
            res[key]=dic[key]
        return res
