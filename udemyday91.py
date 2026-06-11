import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\dev\\Ventas.csv")
print(df)
plt.hist(df["Producto"])
plt.show()
numeros = np.random.randn(1000)
plt.hist(numeros, bins=40, alpha=0.5, color="red", edgecolor="yellow", histtype="barstacked")
plt.show()
x1 = np.random.randn(1000)
x2 = np.random.randn(500)
x3 = np.random.randn(100)
plt.hist(x1, histtype="stepfilled", alpha=0.3, bins=40)
plt.hist(x2, histtype="stepfilled", alpha=0.3, bins=40)
plt.hist(x3, histtype="stepfilled", alpha=0.3, bins=40)
plt.show()
x = np.linspace(0,10,30)
y = np.sin(x)
plt.plot(x,y, "o")
plt.show()
aleatorio = np.random.RandomState(0)
marcadores = ["o", "x", "+","v","s","d"]
for marcador in marcadores:
    plt.plot(aleatorio.rand(5), aleatorio.rand(5), marcador)
plt.show()    
plt.scatter(x,y)
