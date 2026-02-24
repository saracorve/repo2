import pandas as pd
datos  = {"nombre": ["Pedro", "Juan", "Lorena"], "edad" : [25, 39, 33]}
df = pd.DataFrame(datos)
print(df)
print("---------------------------")
print(df.nombre)
print("---------------------------")

empleados = {"nombre": ["Ana", "Luis", "Carlos"], "edad": [30, 25, 40]}
dfempleados = pd.DataFrame(empleados)
print(dfempleados)
x = dfempleados.edad
print(x)
print(dfempleados.shape)
print(dfempleados.columns)
print(dfempleados.index)
print("---------------------------")
df1 = pd.read_csv("C:\\Users\\HP\\Downloads\\Precipitaciones.csv")
print(df1.head(5))
serie = df1.region
print(serie.head())
print("----------------------------------------------")
datos = [10, 20, 30 , 40 , 50]
indices = ["a", "b", "c", "d", "e"]
serie1 = pd.Series(datos, indices)
print(serie1)
serie1 = serie1 + 10
print(serie1)
print("----------------------------------------------")

datos_clima = pd.read_csv("C:\\Users\\HP\\Downloads\\Precipitaciones.csv")
print(datos_clima)
describe_df = datos_clima.describe()
print(describe_df)
headoff = datos_clima.head(1)
print(headoff)

print("----------------------------------------------")
miserie = pd.Series([4,7,-5,3])
print(miserie)
print("----------------------------------------------")

valor = [10, 20, 30, 40]
indi = ['a', 'b', 'c', 'd']
serie_con_indices = pd.Series(valor, indi)
print(serie_con_indices)
print("----------------------------------------------")

serie_desde_diccionario = pd.Series({'a': 30, 'b': 70, 'c': 160, 'd': 50})
va = serie_desde_diccionario["a"]
vd = serie_desde_diccionario["d"]
suma_ad = va + vd
print(suma_ad)
def imprimir_suma_ad():
    print(suma_ad)

print("----------------------------------------------")
serie11 = pd.Series([5,6,7,8,9])
serie12 =  pd.Series([0,1,2,3,4])
serie_sumada = serie11 + serie12
print(serie_sumada)
print("----------------------------------------------")

serie_numerica = pd.Series([2,3,4,5,6,7,8])
serie_doble = serie_numerica * 2
serie_dividida = serie_numerica / 10
print(serie_doble)
print(serie_dividida)
print("----------------------------------------------")

serie_grande = pd.Series([1,2,3,4,5,6,7,8,9,10])
item9 = serie_grande[9]
print(item9 ** 0.5)
print("----------------------------------------------")

data = {  'ID': [1, 2, 3, 4, 5],
    'Producto': ['Producto A', 'Producto B', None, 'Producto D', 'Producto E'],
    'Cantidad': [10, 20, 30, None, 50],
    'Precio': [100, 200, 300, 400, None] }

datas = pd.DataFrame(data)
datasnull = datas.isnull().sum()
print(datasnull)
print("----------------------------------------------")

data = {
    'ID': [1, 2, 3, 4, 1],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto A'],
    'Cantidad': [10, 20, 30, 40, 50],
    'Precio': [100, 200, 300, 400, 100]}
dfsinduplicados = pd.DataFrame(data).drop_duplicates(subset="ID")
print(dfsinduplicados)
print("----------------------------------------------")
data = {
    'ID': [1, 2, 3, 4],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Cantidad': [10, 20, 30, 40],
    'Precio': [100, None, 300, None]}
dfdata = pd.DataFrame(data)
valoresnew = {"Precio" : dfdata["Precio"].mean()}
datanew = dfdata.fillna(valoresnew)
print(datanew)
print("----------------------------------------------")

serie_numeros = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
filtro = serie_numeros > 10
seriefiltro = serie_numeros[filtro]
print(seriefiltro)
print("----------------------------------------------")
valores = pd.Series([18, 22, 7, 9, 15, 8])
condicion_valores_pares = valores %  2 == 0
serievalores = valores[condicion_valores_pares]
print(serievalores)
print("----------------------------------------------")

frutas = pd.Series(["manzana", "banana", "cereza", "durazno", "frambuesa"])
condic_frutas = frutas.str.contains("e")
frutas_con_e = frutas[condic_frutas]
print(frutas_con_e)
print("----------------------------------------------")
edades = pd.Series([23, 30, 26, 27, 22, 24, 25, 28])
promedio_edades = edades.mean()
print(promedio_edades)
print("----------------------------------------------")
ventas = [120, 150, 90, 200, 210, 130, 160]
dias =["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
ventas_semana = pd.Series(ventas, dias)
suma_total_ventas = ventas_semana.sum()
dia_mayores_ventas = ventas_semana.max()
promedio_ventas = ventas_semana.mean()
print(ventas_semana)
print(suma_total_ventas)
print(dia_mayores_ventas)
print(promedio_ventas)
print("----------------------------------------------")
ventas_mes = pd.Series([220, 235, 260, 213, 202, 298, 265, 198, 220, 230, 190, 215, 275, 222, 218, 245, 233, 210, 290, 210,
                        215, 220, 225, 230, 245, 250, 260, 270, 280, 295])
total_ventas_mes = ventas_mes.sum()
print(total_ventas_mes)
dia_ventas_mas_bajas =ventas_mes.min()
print(dia_ventas_mas_bajas)
promedio_ventas_mes = ventas_mes.mean()
print(promedio_ventas_mes)