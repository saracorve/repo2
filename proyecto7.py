import pandas as pd
ruta = "C:\\Users\\HP\\OneDrive\\Escritorio\\SARA_CORCUERA\\PYTHO UDEMY\\dia7\\Datos_Ventas_Tienda.csv"
ruta1 = "C:\\Users\\HP\\OneDrive\\Escritorio\\SARA_CORCUERA\\PYTHO UDEMY\\dia7\\Datos_Ventas_Tienda2.csv"
df = pd.read_csv(ruta)
df1 = pd.read_csv(ruta1)
dfgeneral = pd.concat([df,df1], ignore_index=True)
mejorproducto = dfgeneral.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)
print(mejorproducto)
dfgeneral["Fecha"] = pd.to_datetime(dfgeneral["Fecha"], format= "%m/%d/%Y")
dfgeneral["Mes"] = dfgeneral["Fecha"].dt.month
mejormes = dfgeneral.groupby("Mes")["Total Venta"].sum().sort_values(ascending=False)
print(mejormes)
