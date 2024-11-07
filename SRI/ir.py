import os
import glob

# Ruta de la carpeta que contiene los archivos .txt
carpeta = 'corpusText'

# Crear una lista de todos los archivos .txt en la carpeta
archivos_txt = glob.glob(os.path.join(carpeta, '*.txt'))

#Crear diccionario

postingList={}
# Iterar sobre cada archivo .txt y leer su contenido
for archivo in archivos_txt:
    with open(archivo, 'r') as f:
        contenido = f.read()
        print(type(contenido))
        print(f'Contenido de {archivo}:')
        print(contenido)
    break