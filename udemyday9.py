import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
numeros = [2,4,7,8]
plt.plot(numeros)
plt.savefig("Mi 1er Gráfico")
plt.show()
numeros1 = [10, 15, 7, 10, 22]
plt.figure(facecolor="green")
plt.plot(numeros1)
plt.savefig("grafico numeros")
plt.show()
fig, axes = plt.subplots(ncols=2, nrows=2)
axes[0,0].set_title("first")
plt.show()
x = [1,2,3,4,5,6,7]
y = [1,6,3,4,5,6,7]
plt.plot(x,y, "ro-")
plt.axis([0,8,0,8])
plt.grid()
plt.xticks(rotation=45)
plt.show()
np.random.normal().round