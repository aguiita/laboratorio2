from skimage import io
import numpy as np
import os
import plotly.graph_objects as go

# Carpeta donde están las imágenes
ruta_imagenes = "/Users/user/Desktop/sistemitas/python/labo/mondea3d/"

# Buscar archivos de imagen
archivos = [os.path.join(ruta_imagenes, f) 
            for f in os.listdir(ruta_imagenes) 
            if f.lower().endswith((".tif", ".png", ".jpg"))]

# Leer imágenes en escala de grises
imagenes = []
for archivo in archivos:
    try:
        img = io.imread(archivo, as_gray=True)
        imagenes.append(img)
        print(f"Leída correctamente: {archivo}")
    except Exception as e:
        print(f"No se pudo leer {archivo}: {e}")

# Crear volumen 3D (Z, Y, X)
volumen = np.stack(imagenes, axis=0)
print("Dimensiones del volumen:", volumen.shape)

# Crear grilla de coordenadas
Z, Y, X = np.indices(volumen.shape)
x = X.flatten()
y = Y.flatten()
z = Z.flatten()
C = volumen.flatten()  # intensidades

# Umbral, un valor bandera ponele, q. me hace filtrar los puntos
# para quedarme con los más brillantes
#podria ser un valor fijo, pero lo hago relativo al volumen
#por ejemplo el percentil 90, o sea me quedo con el 10% de los puntos más brillantes
umbral = np.percentile(volumen, 90)  # top 10% de intensidades
print("Usando umbral:", umbral)
mask = volumen > umbral
mask = mask.flatten()  # importante: aplanar la máscara

# Filtrar voxeles por intensidad
x = x[mask]
y = y[mask]
z = z[mask]
C = C[mask]

# --- GRAFICADO CON PLOTLY ---
fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode="markers",
    marker=dict(
        size=3,
        color=C,
        colorscale="Gray",
        opacity=0.5
    )
)])

fig.update_layout(
    scene=dict(
        xaxis_title="Eje X",
        yaxis_title="Eje Y",
        zaxis_title="Eje Z"
    ),
    title="Reconstrucción 3D interactiva"
)

fig.show()

print("Valor mínimo:", volumen.min())
print("Valor máximo:", volumen.max())
print("Tipo de datos:", volumen.dtype)
