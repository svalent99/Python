num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))
if num1 > num2 and num1 > num3:
    print(num1, "es el número mayor")
elif num2 > num1 and num2 > num3:
    print(num2, "es el número mayor")
else:
    print(num3, "es el número mayor")
