usuario=input("Ingrese el nombre de usuario: ")
clave=input("Ingrese la clave de acceso: ")
if usuario=="svalent" and clave=="124":
    print("Acceso correcto.")
elif usuario=="svalent" and clave !="124":
    print("clave incorrecta")
elif usuario !="svalent" and clave=="124":
    print("usuario incorrecto")   
elif usuario !="svalent" and clave !="124":
    print("Acceso bloqueado,espere unos minutos e intente de nuevo")