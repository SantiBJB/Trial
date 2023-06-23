usuario = input("Ingrese su usuario: ")
contraseña= input ("Ingrese su contraseña: ")
max_intentos= 3
intentos= 0

while usuario !="Santi" and contraseña != "123" and intentos < max_intentos:
    intentos +=1
    if intentos == max_intentos:
        break
    print("Usuario o Contraseña invalidos.")
    usuario = input("Ingrese su usuario: ")
    contraseña= input ("Ingrese su contraseña: ")
if intentos==max_intentos:
   print("Se han alcanzado el máximo de intentos permitidos.")
else:
    print("Bienvenido")
