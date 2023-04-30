cadena1= input( " ingrese una cadena: ")
cadena2= input (" ingrese otra cadena: ")
if cadena1.count("a")>cadena2.count("a"):
    print("la palabra",cadena1,"es mas larga que ",cadena2)
elif cadena2.count("a")>cadena1.count("a"):
    print("la palabra",cadena2,"es mas larga que ",cadena1)
else:    
    print("ambas tienen la misma longitud")