numeros = [1, 2, 3, 4]
for n in numeros:
    print(n)


paises = ['Francia', 'Alemania', 'España', 'Italia', 'Chile']
for p in paises:
    if "a" in p:
        print(p)
    else:
        print(f"{p} no contiene a")

colores = ['rojo', 'azul', 'verde']
prendas = ['camisa', 'pantalones', 'sombrero']
for c in colores:
    for ps in prendas:
        print(f"{ps} {c}")

rango_numeros_pares = [2,4,6,8,10,12,14,16,18,20]
for r in rango_numeros_pares:
    print(r)

print("-----------------------------------------------------------")

suma = 0
iteracion = range (1,101)
for n in iteracion:
    suma = suma + n
print(f"LA suma de todos los números del 1 al 100 es: {suma}")
print("-------------------------------------------------------------------------")
cadena = "aprendizaje"
index = range(len(cadena))
for n in index:
    c = cadena[n]
    print(f"Indice {n}: {c} ")

contador = 0
while contador < 10:
    contador += 1
    print(contador)
    
print("-----------------------------------------------")
numero = 0
while numero < 15:
    numero += 1
    if numero == 5:
        continue
    if numero == 10:
        continue
    print (numero)
print("-----------------------------------------------")

x = 0
while x < 10:
    x += 1
    if x % 4 == 0:
        break
    print(x)

def imprimir_mensaje():
    print("¡Estoy aprendiendo funciones en python")

imprimir_mensaje()

print("-----------------------------------------------------")
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

saludar_usuario("Sara")
print("-----------------------------------------------------")

def calcular_area_rectangulo(l, a):
    resultado = l * a
    return resultado
car =calcular_area_rectangulo(5,2)
print(car)
print("-----------------------------------------------------")

def solicitar_nombre():
    nom = input("Coloca tu nombre: ")
    return nom

def saludar():
    saludo = f"Hola {solicitar_nombre()}"
    print(saludo)

print(saludar())
print("-----------------------------------------------------")

def pedir_numero():
    a = int(input())
    b = int(input())
    return a, b

def sumar():
    c, d = pedir_numero()
    resultado = c + d  
    print(f"La suma es {resultado}")


print("-----------------------------------------------------")

def solicitar_numero():
    x = int(input("Ingrese un número entero positivo: "))
    return x

def calcular_factorial(x):
    multi = 1
    for n in range(1, x + 1 ):
        multi = multi * n
    return multi
    
def mostrar_resultado():
    y = solicitar_numero()
    resultado = calcular_factorial(y) 
    print(f"El factorial de {y} es {resultado}")

print(mostrar_resultado())




       



