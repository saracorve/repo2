print("Bienvenida a tu agenda personal Sara")
agenda = {"Celeste" : 958, "Gretta": 854, "Vannia" : 547}
añadir = 1
buscar = 2
editar = 3 
eliminar = 4
all = 5
lista = int(input("¿Que deseas realizar? 1. Añadir , 2. Buscar, 3. Editar, 4. Eliminar, 5. Mostrar todos los contactos." \
"Selecciona un número: "))
if lista == añadir:
    nom = input("Coloca el nombre: ")
    tel = input("Coloca el telefono: ")
    agenda[nom] = tel
    print("Agregaste a "+ nom + " a tu agenda personal")
    print(agenda)
if lista == buscar:
    nom1 = input("Coloca el nombre a buscar: ")
    if nom1 in agenda:
        print(agenda[nom1])
    else:
        print( nom1 + " no se encuetra registrado en la agenda")
if lista == editar:
    nom2 = input("Nombre de contacto a editar: ")
    if nom2 in agenda:
        tel1 = input("Nuevo telefono: ")
        agenda[nom2] = tel1
        print("Se cambio el telefono de "+ nom2 + " satisfactoriamente.")
        print(agenda)
if lista == eliminar:
    nom3 =  input("Nombre de contacto a eliminar: ")
    if nom3 in agenda:
        agenda.__delitem__(nom3)
        agenda.p
        print(agenda)
if lista == all:
    print(agenda.items())


    








