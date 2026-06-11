import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
numeros = [10, 15, 7, 10, 22]
plt.figure(facecolor= "pink")
plt.plot(numeros)
plt.savefig("Grafico verde")
plt.show()
fig, axs = plt.subplots(2,2)
plt.show()
datos = np.random.randn(1000)
x1 = plt.hist(np.random.randn(1000), bins=40, color="blue", edgecolor="black", histtype="stepfilled", alpha= 0.5)
x2 = plt.hist(np.random.randn(500), bins=40, color="blue", edgecolor="black", histtype="stepfilled", alpha= 0.5)
x3 = plt.hist(np.random.randn(100), bins=40, color="blue", edgecolor="black", histtype="stepfilled", alpha= 0.5)
plt.show()
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.scatter(x,y, c="blue",marker= "o" ,s=50 )
x2 = [1, 2, 3, 4, 5] 
y2 = [1, 4, 9, 16, 25]
plt.scatter(x2,y2, c="green",marker= "*" ,s=50 ) 
plt.show()
df = pd.DataFrame({    "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
    "cantidades": [40, 25, 15, 20]})
plt.pie(df["cantidades"], labels= df["frutas"], autopct= "%1.1f%%", colors = ["red", "yellow","darkred","orange"], shadow=True, explode=(0,0,0.5,0))
plt.show()
fig, axes = plt.subplots(1,2)
ax1 = axes[0]
ax2 = axes[1]
ax1.plot([1, 2, 3, 4], [2, 4, 8, 16], "g")
ax1.set_title("Gráfico de línea")
ax2.scatter([1, 2, 3, 4], [2, 4, 8, 16],c="red")
ax2.set_title("Grafico de scatter")
plt.show()
plt.style.use("ggplot")
df = pd.DataFrame({    "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
    "cantidades": [40, 25, 15, 20]})
plt.bar(df["frutas"], df["cantidades"])
plt.title("Distribucion de frutas en el almacén")
plt.show()
plt.style.use("dark_background")
df = pd.DataFrame({    "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
    "cantidades": [40, 25, 15, 20]})
plt.pie(df["cantidades"], labels=df["frutas"], autopct="%1.0f%%", explode=(0.2,0.2,0.2,0.2))
plt.title("Distribución de frutas en el almacén")
plt.show()
x = np.arange(10)
y = x**2
plt.stem(x, y)
plt.title("Relación entre números y sus Cuadrados")
plt.xlabel("Número (x)")
plt.ylabel("Cuadrado del número x^2")
plt.show()
plt.style.use('_mpl-gallery')
y1 = [6,1,4,4,8]
y2 = [4,6,3,5,8]
y3 = [7,9,9,2,7]
x = [1,2,3,4,5]
yy = np.vstack([y1,y2,y3])
plt.stackplot(x,y1,y2,y3, colors=["red", "blue", "green"], labels=["Serie y1", "Serie y2", "Serie y3"])
plt.legend(loc="upper left")
plt.title("Distribución acumulativa de valores por serie de tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Valores Acumulados")
plt.show()
plt.style.use('_mpl-gallery')
np.random.seed(0)
data1 = np.random.normal(loc=0, scale=0.5, size=100)
data2 = np.random.normal(loc=2, scale=1, size=100)
data3 = np.random.normal(loc=-2, scale=1.5, size=100)
plt.violinplot(data1, data2, data3,)
plt.xlabel("Muestra1","Muestra2", "Muestra3")
plt.title("Comparación de distribuciones en Violin plot")
plt.show()