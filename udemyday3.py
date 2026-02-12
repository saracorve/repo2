palabra = "pantalla"
palabramay = palabra.upper()
print(palabramay)

string1= "aprender"
string2 = "python"
resultado = str.capitalize(string1) +  " " + str.capitalize(string2)
print(resultado)

frase = "Python es divertido"
frasemodificada = frase.replace("divertido","genial")
print(frasemodificada)

palabra = "computadora"
print(palabra[4])

palabra = "computadora"
print(palabra[5:9])

palabra = "aventura"
print(palabra[1:-1:2].upper())

palabra = "mouse"
letra = "o"
print(palabra.count(letra))

frase = "Sara está estudiando Python en sus vacaciones"
print(frase.count(" ") + 1)

frase = " aqui vamos de nuevo "
palabraenfrase = (frase.rstrip().count(" "))
print(palabraenfrase)

escribenombre = input("Dame tu nombre: ")
naciminiento = int(input("¿En que año naciste?: ")) +1
print(naciminiento)

kilometros = int(input("Kilometros a convertir: ")) * 0.621371
millas = input("Es igual a: " + str(kilometros)  + " millas")

nombre = "Sara"
edad = 30
frase1 = "Hola {}, tienes {} años".format(nombre, edad)
print(frase1)

producto = "tele"
cantidad = 5
precio = 100
total = cantidad * precio
frase2 = f"Hay {cantidad} {producto} con un precio total de {total}"
print(frase2)

nombre = "Maria"
actividad = "nadar"
hora_dia = "4pm"
frase3 = f"{nombre} prefiere {actividad} a las {hora_dia}"
print(frase3)