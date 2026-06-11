import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ruta = "C:\\dev\\Datos+Meteorológicos_Arg_2023.csv"
df = pd.read_csv(ruta)
df["Fecha"] = pd.to_datetime(df["Fecha"],format="%d/%m/%Y")
listciudades = [] 
for c in df["Ciudad"]:
    if c not in listciudades:
        listciudades.append(c)
    
meses = {1:"Enero", 2:"Febrero",  3:"Marzo", 4:"Abril", 5:"MAyo", 6:"Junio",7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"OCtubre", 11:"Noviembre",12:"Diciembre"}

def Consulta():
    while True:
       ciudad =  input(f"Selecciona la ciudad que desee ({listciudades}): ").title()           
            
       mes = int(input(f"Seleccione el mes, (Ejem: 1: Enero): "))
       if ciudad not in listciudades or mes not in range(1,13):
           print("Seleccione datos validos")
           continue
       
       nuevodf = df[(df["Ciudad"] == ciudad) & (df["Fecha"].dt.month == mes)]
       plt.plot(nuevodf["Fecha"],nuevodf["Temperatura Maxima"], color="red", label= "Temp. Maxima")
       plt.plot(nuevodf["Fecha"],nuevodf["Temperatura Minima"], color="blue", label="Temp Minima")
       plt.title(f"Temperatura de {ciudad} en {meses[mes]}")
       plt.legend()
       plt.xlabel("Fecha")
       plt.ylabel("Temperatura °C")
       plt.xticks(rotation=45)
       plt.show()

       final = input("Desea continuar (s/n):  ").lower()
       if final != "s":
           break
                    
       

print(Consulta())
     

