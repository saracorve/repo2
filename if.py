edad = int(input("Coloca tu edad: "))
if edad >= 18:
    print ("Tienes " + str(edad) + " años, eres mayor de edad")
else:
    print ("Tienes " + str(edad) + " años, eres menor de edad")


calificacion = int(input("Coloca la nota del 0 al 10: "))
if calificacion > 10:
    print("Calificacion no válida")
elif calificacion >= 9:
    print("Sobresaliente")
elif calificacion >= 7:
    print("Notable")
elif calificacion >= 5:
    print("Aprobado")
else:
    print("Insuficiente")


x1 = int(input("Coloca un numero: "))
x2 = int(input("Coloca un numero: "))
x3 = int(input("Coloca un numero: "))
if x1 < x2 and x2 < x3:
    print(x1, x2, x3 )  
elif x1 < x2 and x3 < x2 and x1 < x3:
    print(x1, x3, x2)
elif x2 < x1 and x1 < x3:
    print(x2, x1, x3)
elif x2 < x1 and x3 < x1 and x3 > x2:
    print(x2, x3, x1)
elif x3 < x1 and x1 < x2 and x3 < x2:
    print(x3, x1, x2)
else: 
    print(x3, x2, x1)