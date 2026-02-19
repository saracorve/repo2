def numero1():
    x = int(input("coloca tu numero a multiplicar: "))
    return x
def numero2():
    x = int(input("Hasta que numero vas a multiplicar: "))
    return x

def tablas():
    resultado = 1
    x = numero1()
    y= range(1, numero2()+1)
    for n in y:
        resultado = x * n
        print(f"{x} x {n} = {resultado}")


def multiplicar():
    while True:
        tablas()
        
        ot = input("Desea continuar: s/n: ")
        if ot != "s":
            break

multiplicar()

    

    






        


