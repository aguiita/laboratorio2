from skimage import io
#para leer imagenes

import numpy as np
#para trabajar con arreglos y matrices

import glob
import os
#para buscar archivos en carpetas

# Para gráficos
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  # para gráficos 3D

# carpeta donde estan las fots

ruta_imagenes= "mondea3d/"

#busco todos los png en la carpta y los ordeno
#igual ya son todos png
archivos=sorted(glob.glob(os.path.join(ruta_imagenes, "*.png")))
# os.path.join("mondea3d/", "*.png") en esa carpeta busca todo lo que termine en .png


#printeo la cantidad y el primero para probar
print("Cantidad de imágenes encontradas:", len(archivos))
print("Primer archivo:", archivos[0] if archivos else "Ninguno")

# ahora que encontre las imagenes, las voy a leer y guardar en una lista
imagenes=[]
for archivo in archivos:
    img=io.imread(archivo, as_gray=True)
    imagenes.append(img) #agrego la imagen a la lista

#printeo para ver que onda
#eso lo puedo sacar despues
    print(f"Imagen {archivo} leída con forma {img.shape} y tipo {img.dtype}")
   
  #imagenes es una lista de matrices 
  #Cada matriz es una “rebanada” del volumen.

#ahora la lista de matrices la hago 3d
#Eje Z = número de imágenes
#Eje Y = altura de la imagen
#Eje X = ancho de la imagen
