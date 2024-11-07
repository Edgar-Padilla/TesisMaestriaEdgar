from motorBusqueda.MSRI.gramatica.correccion import correccion

class busqueda:
#-------------Metodos--------------------------------------------------------------
    #Cargar archivos
    def __init__(self,postingList, sinonimosDic, bigramDic):
        self.postingList = postingList
        self.sinonimosDic = sinonimosDic
        self.bigramDic = bigramDic

#-----------Buscador----------------------------------------------------
    def fomatoSalida(self, res, dic_res, palabra):
        for doc in dic_res:
            dic_doc=self.postingList[palabra][doc]
            doc=doc.replace('.txt','.png')
            time = int(doc.replace('.png','').replace('frame_',''))
            horas = (time*5) // 3600
            minutos = ((time*5) % 3600) // 60
            segundos = (time*5) % 60
            time = f'The image is located at time {str(horas).zfill(2)}:{str(minutos).zfill(2)}:{segundos}'
            res.append((doc, dic_doc,time))
        return res
    def buscarPalabra(self, palabra):
        res=[]
        sinonimos=[]
        corr=[]
        if palabra!="":
            palabra=palabra.lower()
            flag = False
            #busca si existe la palabra en el posting list
            if palabra in self.postingList:
                dic_res=self.postingList[palabra]
                self.fomatoSalida(res, dic_res, palabra)
                flag=True
            #busca si existe algun sinonimo de la palabra en el posting list
            elif palabra in self.sinonimosDic:
                sinonimo=self.sinonimosDic[palabra]
                if sinonimo in self.postingList:
                    dic_res=self.postingList[sinonimo]
                    self.fomatoSalida(res, dic_res, sinonimo)
                    flag=True
            #Si no encuentra ninguna de las anteriores realiza una corrección
            if not flag:
                cor=correccion()
                palabra_peso=cor.convertirPalabra(palabra)
                list_bigramas=cor.crearListaBigramas(palabra_peso)
                dic_list_bigramas=cor.extraerDicBigramas(list_bigramas,self.bigramDic)
                set_palabras=sorted(cor.extraerPalabras(dic_list_bigramas))
                listaLev=cor.listLeven(palabra_peso,set_palabras)
                if listaLev:
                    min_clave=min(listaLev.keys())
                    for palabra1 in listaLev[min_clave]:
                        aux=palabra1.replace("$","")
                        corr.append(aux)
                        dic_res=self.postingList[aux]
                        self.fomatoSalida(res, dic_res, aux)
        return res, sinonimos, corr
            
    def buscarFrase(self, ph):
        sinonimos=[]
        words=ph.split()
        keys=[]
        correccion=[]
        res=[]
        

    def identificar(self, entrada):
        aux=entrada.split()
        if len(aux)>1:
            return self.buscarFrase(entrada)
        else:
            return self.buscarPalabra(entrada)