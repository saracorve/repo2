import pandas as pd
librosdf = pd.DataFrame({"Título":["El Quijote", ""
"Cien años de soledad", "La Odisea"], "Autores": ["Miguel de Cervantes", "Gabriel Garcia Marquez","Homero"], "Año": [1605, 1967, -800]})
print(librosdf)
print ("-------------------------------------------")
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}
df = pd.DataFrame(data)
a = df[df["Edad"] > 25]
print(a)
print ("-------------------------------------------")

df["Edad_en_10 años"] = df["Edad"] +10
df["Ciudad"].str.upper()
df["Es mayor de 25"] = True > 25
print(df)
print ("-------------------------------------------")
datos = {
    'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D'],
    'año': [2001, 2000, 2005, 2010],
    'rating': [7.2, 6.5, 8.1, 7.5]}
df = pd.DataFrame(datos)
dfordenado = df.sort_values(by=["rating", "año"], ascending=[False,True])
print(dfordenado)
print ("-------------------------------------------")

datos = {
    'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D', 'Pelicula E'],
    'género': ['Acción', 'Drama', 'Acción', 'Comedia', 'Drama'],
    'rating': [7.2, 8.5, 9.1, 6.5, 7.8]
}
df = pd.DataFrame(datos)
promediortxgen = df.groupby("género")["rating"].mean()
print(promediortxgen)
print ("-------------------------------------------")
libros = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'titulo': ['El Quijote', 'La Odisea', 'Cien Años de Soledad', 'El Principito']
})
 
autores = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'nombre': ['Miguel de Cervantes', 'Homero', 'Gabriel García Márquez', 'J.K. Rowling']
})

libros_autores = pd.merge(libros,autores, how='outer', on="ID")
print(libros_autores)
print ("-------------------------------------------")
cursos = pd.DataFrame({
    'curso_id': [101, 102, 103],
    'nombre_curso': ['Introducción a Python', 'Data Science con Python', 'Machine Learning Avanzado']
})
 
inscripciones = pd.DataFrame({
    'curso_id': [102, 102, 101, 104],
    'fecha_inscripcion': ['2023-01-15', '2023-02-01', '2023-01-20', '2023-03-05']
})
cursos_inscripciones = pd.merge(inscripciones, cursos, how= 'outer', on= "curso_id")
pd.set_option('display.max_columns', 6)
print(cursos_inscripciones)
print ("-------------------------------------------")
productos = pd.DataFrame({
    'ID': [10, 11, 12],
    'Nombre': ['Teclado', 'Mouse', 'Monitor'],
    'Marca': ['Logitech', 'Razer', 'Dell']
})
 
reviews = pd.DataFrame({
    'ID': [10, 11, 12],
    'Calificación': [5, 4, 4],
    'Comentario': ['Excelente producto', 'Buen producto', 'Satisfecho']
})
productos_reviews = pd.merge(productos,reviews,on="ID", indicator=True)
print(productos_reviews)
print ("-------------------------------------------")
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'Nombre': ['Ana', 'Beto', 'Carla']
})
df_a.set_index('id', inplace=True)

# Creación del DataFrame df_b
df_b = pd.DataFrame({
    'id': [1, 2, 3],
    'Edad': [25, 30, 35]
})
df_b.set_index('id', inplace=True)
dfcombinado = df_a.join(df_b, how= 'left')
print(dfcombinado)
print ("-------------------------------------------")
productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
}).set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2],
    'NombreCategoria': ['Categoría 1', 'Categoría 2']
}).set_index('CategoriaID')
dfcombi = productos_df.join(categorias_df)
print(dfcombi)
print ("-------------------------------------------")
productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
})

productos_df = productos_df.set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2, 3],
    'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
}).set_index('CategoriaID')

produccombina = categorias_df.join(productos_df, how="right")
print(produccombina)
print ("-------------------------------------------")

ventas_enero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 'Cantidad': [300, 200, 150]})

ventas_febrero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 'Cantidad': [350, 210, 170]})
ventastotal = pd.concat([ventas_enero, ventas_febrero], ignore_index=True)
print(ventastotal)
print ("-------------------------------------------")
datos_cliente = pd.DataFrame({'Nombre': ["Ana", "Luis", "Marta"], 'Edad': [34, 45, 28]})
compras_cliente = pd.DataFrame({'Producto': ["Libro", "Lápiz", "Cuaderno"], 'Precio': [15.50, 0.50, 2.00]})
infoclientes = pd.concat([datos_cliente, compras_cliente], axis=1)
print(infoclientes)
print ("-------------------------------------------")
tienda_a = pd.DataFrame({'Producto': ["Manzanas", "Bananas"], 'Cantidad': [500, 300]})
tienda_b = pd.DataFrame({'Producto': ["Naranjas", "Peras"], 'Cantidad': [400, 250]})
vntastienda = pd.concat([tienda_a, tienda_b], keys=["Tienda A", "Tienda B"])
print(vntastienda)
print ("-------------------------------------------")
primerasemana2024 = pd.Series(pd.date_range("20240101", periods=7))
print(primerasemana2024)
print ("-------------------------------------------")
fechas =['2024-01-01', '2024-02-14', '2024-03-01']
df1= pd.Series(pd.to_datetime(fechas,format= '%Y-%m-%d'))
df2 = df1.dt.strftime("%d/%m/%Y")
print(df2)
print ("-------------------------------------------")
fechas1 =  ['01-01-2024', '14-02-2024', '01-03-2024'] 
dffechas = pd.Series(pd.to_datetime(fechas1, format="%d-%m-%Y"))
df3 = dffechas +pd.Timedelta(days=5)
print(df3)
print ("-------------------------------------------")
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carmen'],
    'Edad': [25, 30, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}, index=['fila1', 'fila2', 'fila3'])
resultado = df.loc[["fila2", "fila3"]]
print(resultado)
print ("-------------------------------------------")
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16]
})
resultado = df.iloc[0:2 , 2:4]
print(resultado)