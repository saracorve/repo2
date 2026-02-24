import pandas as pd
df = pd.read_csv("C:\\Users\\HP\\OneDrive\\Escritorio\\SARA_CORCUERA\\PYTHO UDEMY\\Día+6\\medallas.csv")
df1 = df.fillna({"Oro" : 0, "Plata" : 0, "Bronce" : 0})
x = df1.sort_values("Oro", ascending=False)
y = x.head(3)
print(y)
filtro = df1["Total"] > 10
z= df1[filtro].sort_values("Total", ascending=True)
print(" ")
#
print("Paises con mas de 10 medallas Olimpicas")
print(z)