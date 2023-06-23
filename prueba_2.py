def opcion1():
    print("Santiago")

def opcion2():
    print("Burany")

def opcion3():
    print("20")

def opcion4():
    print("")

def salir():
    print("Saliendo del programa...")

def change_password():
    global contraseña  # Declarar la variable como global para poder modificarla
    nueva_contraseña = input("Introduzca la nueva contraseña: ")
    contraseña = nueva_contraseña  # Actualizar la contraseña con la nueva

def change_user():
    usuario = input("Introduzca el nuevo usuario: ")
    return

def change_name():
    nuevo_nombre = input("Introduzca el nuevo nombre: ")
    return

menu_2 = {
    "1": change_password,
    "2": change_name,
    "3": change_user,
    "0": salir
}

menu = {
    "1": opcion1,
    "2": opcion2,
    "3": opcion3,
    "4": opcion4,
    "0": salir
}

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")
passw="123"
max_intentos = 3
intentos = 0

while usuario != "Santi" and contraseña != "123" and intentos < max_intentos:
    intentos += 1
    if intentos == max_intentos:
        break
    print("Usuario o Contraseña invalidos.")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

if intentos == max_intentos:
    print("Se han alcanzado el máximo de intentos permitidos.")
else:
    print("Bienvenido")

while True:
    print("----- MENÚ -----")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Cambio de datos")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion in menu:
        menu[opcion]()  # Ejecuta la función correspondiente a la opción seleccionada
    else:
        print("Opción inválida. Inténtalo nuevamente.")

    if opcion == "0":
        break
    if opcion == "4":
        while True:
            print("----- MENÚ pag 2-----")
            print("1. Contraseña")
            print("2. Cambiar usuario")
            print("3. Cambiar nombre")
            print("0. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion in menu_2:
                menu_2[opcion]()  # Ejecuta la función correspondiente a la opción seleccionada del submenú
            else:
                print("Opción inválida. Inténtalo nuevamente.")

            if opcion == "0":
                break