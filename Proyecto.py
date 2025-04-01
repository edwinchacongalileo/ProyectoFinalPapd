import numpy as np

# Cargar el archivo npy
file_path = "C:\PythonWs\Proyecto\proyecto_training_data.npy"
data = np.load(file_path, allow_pickle=True)

# Ver la estructura de los datos
print(type(data))
print(data.shape)
