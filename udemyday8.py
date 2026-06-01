import numpy as np
import pandas as pd
datos = {
    "Ciudad": ["Ciudad de México", "Buenos Aires", "Río de Janeiro", "Lima", "Bogotá", "Santiago de Chile", "São Paulo", "La Habana", "Cancún", "Cartagena"],
    "País": ["México", "Argentina", "Brasil", "Perú", "Colombia", "Chile", "Brasil", "Cuba", "México", "Colombia"],
    "Población": [9265833, 3059574, 6748314, 9756020, 7181663, 6199241, 12333146, 2164182, 888124, 1036671],
    "Visitantes": [21000000, 15000000, 13000000, 9000000, 8000000, 7500000, 20000000, 4000000, 5000000, 3000000]}
df = pd.DataFrame(datos)
promediopobla = df["Población"].mean()
print(np.round(promediopobla))
min_visitantes = np.min(df["Visitantes"])
print(min_visitantes)
max_visitantes = np.max(df["Visitantes"])
print(max_visitantes)
array_enteros = np.array(range(1,11))
print(array_enteros)
forma_array = array_enteros.shape
print(forma_array)
array2d = np.array([[1,2,3],[4,5,6]])
largo_array2d = len(array2d)
print(largo_array2d)
array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])
arrayconcat = np.concatenate([array1, array2])
print(arrayconcat)
arrayorig = np.array([[1,2,3],[4,5,6]]).reshape(2,3)
print(arrayorig)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
sumaAB = a + b
multiAB = a * b
print(sumaAB)
print("---------------------------")
print(multiAB)
print("______________________________________________")
numeros = np.array([1,2,3,4,5,6,7,8,9,10])
quinto_elemento = numeros[5]
print(quinto_elemento)
print("______________________________________________")
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
segunda_fila = matriz[1, : ]
print(segunda_fila)
pares_impares = matriz % 2 == 0
print(pares_impares)
print("______________________________________________")
array_original = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array_reshape = array_original.reshape(3,4)
print(array_reshape)
print("______________________________________________")
array_original1 = np.array([[1,2,3], [4,5,6]])
array_modificado = array_original1.transpose()
print(array_modificado)
print("______________________________________________")
array_original2 = np.array([[1,2,3], [4,5,6]])
array_aplanado = array_original2.flatten()
print(array_aplanado)