import super_gradients
import cv2
import json
import time
from PIL import Image, ImageDraw
import os
import numpy as np
from super_gradients.common.object_names import Models
from super_gradients.training import models
import torch

class generarCorpus:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print('-.-.-.-.-> ',self.device)
        self.model = models.get(Models.YOLO_NAS_S, pretrained_weights="coco").to(self.device)
        #Seleccion de camara con la que se trabajara
        print('Inicilizado')
    def extraerYGuardarCuadros(self,imagen, nombre,ruta, posiciones):
        for i,posicion in enumerate(posiciones):
            x = round(max(0,posicion[0]))
            y = round(max(0,posicion[1]))
            w = round(max(0,posicion[2]))
            h = round(max(0,posicion[3]))
            draw = ImageDraw.Draw(imagen)
            draw.rectangle([x,y,w,h], outline ="blue")
        ruta2=f"{ruta}/{nombre}.png"
        imagen.save(ruta2)
        print(f'imagen guardada en la ruta: {ruta2}')
    def crearTexto(self,imagenPath, imagen, rutaTextos, name):
        model_predictions  = self.model.predict(imagen, conf=0.60,fuse_model=False)
        prediction = model_predictions.prediction
        class_names = model_predictions.class_names
        class_name_indexes = prediction.labels.astype(int)
        bboxes = prediction.bboxes_xyxy # [Num Instances, 4] List of predicted bounding boxes for each object
        names = [class_names[i] for i in class_name_indexes]
        nombre=f'{rutaTextos}/{name}.txt'
        with open(nombre, 'w') as archivo:
                archivo.write('\n'.join(names))
        print(f'archivo  de texto guardado en la ruta: {nombre}')
        self.extraerYGuardarCuadros(imagen,name, imagenPath, bboxes)
    def splitVideoIntoFrames(self, videoPath, imagenPath, textosPath, intervalo, targetSize):
        '''
        videoPath: ruta del video
        imagenPath: ruta donde se alojaran los frames
        intervalo: intervalo en segundos para obtener frames del video
        targetSize: tupla de 2x2 con el tamaño de la imagen
        '''
        # Abre el video
        cap = cv2.VideoCapture(videoPath)
        # Asegúrate de que el video se haya abierto correctamente
        if not cap.isOpened():
            print("Error al abrir el video.")
            return
        # Intervalo de tiempo para extraer imágenes (5 segundos)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        print('frame/s----->',fps)
        contador = 1
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            tiempo_actual = int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
            if tiempo_actual % (intervalo * fps)== 0:
                imagen = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                #imagen = imagen.convert("L")  # Convertir a escala de grises
                imagen = imagen.resize(targetSize)
                name=f'frame_{contador}'
                self.crearTexto(imagenPath, imagen, textosPath, name)
                contador += 1
            if contador == 10:
                break
        cap.release()

    def main(self):
        videoPath = 'video/UISD Tax Office Lobby Vdeo Footage (1).mp4'
        imagenPath = 'images'
        textosPath = 'corpusText'
        inicio = time.time()
        self.splitVideoIntoFrames(videoPath, imagenPath, textosPath, 20, (680,680))
        fin = time.time()
        tiempo_transcurrido=fin-inicio
        print(f"Tiempo transcurrido para obtener imagenes: {tiempo_transcurrido/60} minutos")

run=generarCorpus()
run.main()