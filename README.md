# Sistema de Recuperación de Información basado en codificación Imagen-Texto para la Identificación de Escenas de Interés en Videos de Larga Duración

## Tesis de Maestría Edgar Padilla

# Estructura

Este repositorio contiene dos carpetas
  \
    SRI\
    documentos\

La carpeta documentos contiene los productos académicos que se generaron en la maestría en ciencias de la computación, acontinuación se enumeran estos documentos:

  - 1.- Tesis de maestría: Tesis_Maestría.
  - 2.- Artículos: English_Paper_SRI, EnglishArticuloCodificacionImageTxt.
  - 3.- Posters: PosterEdgarTXTtoImage, PosterEdgarYolo.

La carpeta SRI contiene el código para la ejecución de la apliación web.

# Requerimeintos para ejecutar la aplicación web

La aplicación web fue creada con el framework Django y para toda la lógica de programación se ocupó el lenguaje de programación Python 3. Por ello es necesario instalar las siguientes librerias usando pip.

  - super-gradients
  - opencv-python
  - pillow
  - numpy
  - torch
  - django
    
Si lo creen oportuno realizar todo en un entorno virtual.

# Ejecutando la aplicación web

Se debe seguir los siguientes pasos para ejecutar la apliación web.

1.- Abrir una terminal en la carpeta SRI

2.- Descargar el siguiente video de Yotube https://www.youtube.com/watch?v=-gV67VpzP5M y colocarlo en la carpeta SRI/appWeb/SRI/videoData.

3.- Ejecutar el archivo videoToText. Esta ejecución creará las imagenes y documentos de texto y las guardara en las rutas SRI/appWeb/motorBusqueda/static/images y SRI/appWeb/SRI/corpusText respectivamente.

4.- Después de crear los archivos de texto y las imágenes, abrir una nueva terminal en la ruta SRI/appWeb y ejecutar el siguiente comando python3 mnage.py runserver.

5.- Dar click en la dirección IP que aparece en la terminal, esto abrirá una página de internet y podrá realizar las busquedas.

# Ejemplos de búsqueda en la aplicación web.

En el siguiente enlace pueden ver los ejemplos de búsqueda que se realizan en la apliación web: https://www.youtube.com/watch?v=VgMcgrDdd7s

# Notas

Nota 1: No subí el video y las imágenes desde un inicio ya que github me marcaba error al cargar, lo más seguro es que se deba a los límites en cuanto al tamaño y número de documentos que puedo cargar. Por este motivo tuve que borrar las imágenes y video.

Nota 2: Si tienen algún problema con Cmake favor de contactarme para apoyarlos a solucionarlo.
