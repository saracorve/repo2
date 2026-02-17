ciudades = ["New York", "Paris", "Tokyo", "London", "Sydney"]
print(ciudades[0])
print(ciudades[1])
print(ciudades[2])
print(ciudades[3])
print(ciudades[4])

#------------------------------
numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros.append(6)
print(numeros)
numeros.remove(1)
print(numeros)
numeros.insert(1, 7)
print(numeros)
numeros.sort()
print(numeros)
#-------------------------------

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2
print(combinada)
repetida = lista1 * 3
print(repetida)
sublista = combinada[1:4]
print(sublista)

mi_primera_tupla =("sara", 30, "Enero")
print(mi_primera_tupla[1])

datos_personales = ("Maria", "Perez", 35, "Ingeniera")
(Nombre, Apellidos, Edad, Profesión) = datos_personales
print(Nombre + " " + "es" + " " + Profesión)

info_ciudades = (("Buenos Aires", 3000000, "Argentina"), ("Madrid", 3200000, "España"), ("Tokio", 13929286, "Japón"))
a, b, c = info_ciudades
print("La ciudad de " + a[0] + " en " + a[2]+ " tiene una poblacion de " + str(a[1]) + " habitantes")
print("La ciudad de " + b[0] + " en " + b[2]+ " tiene una poblacion de " + str(b[1]) + " habitantes")
print("La ciudad de " + c[0] + " en " + c[2]+ " tiene una poblacion de " + str(c[1]) + " habitantes")

mi_diccionario = {"manzana" : "roja", "banana" : "amarilla", "naranja" : "naranja"}
print(mi_diccionario)

edades = {"Juan": 28, "Elena": 32, "Marcos": 17}
print(edades["Elena"])
edades["Juan"] = 29
print(edades)
edades["Luisa"] = 25
print(edades)

productos = {"manzana": 0.40, "banana": 0.50, "cereza": 0.80} 
claves = productos.keys()
print(claves)
valores = productos.values()
print(valores)
productos ["naranaja"] = 0.60
print(productos)
nuevo = productos.update({"banana" : 0.75})
print(nuevo)
print(productos)

num1 = 10
num2 = 8
a = num1 == num2
print(a)

x = 1
y = 2
z = 3
condicion1= x != y
condicion2 = y < x
condicion3 = z > y
b =  (condicion1 and condicion3) or condicion2
print(b)

edad = int(input("Coloca tu edad: "))
if edad >= 18:
    print("Tienes "  + str(edad) +   " años. Eres mayor de edad" )


usuario = input("Colcoa tu ususario:")
contraseña = input("Coloca tu contraseña:")
if usuario == "admin" and contraseña == "abc123":
    print("Acceso concedido")

amigos = ["Juan", "Ana", "Laura"]
nombre = input("Coloca tu nombre: ")
if nombre in amigos:
    print(nombre + " está en mi grupo de amigos")   


