import os

# Ejercitario numero 1

ejercicio = int(input("Cual ejercitario desea probar? elija del 1 al 6: "))
if (ejercicio == 1):

    # 1-  Leer los tres lados de un triángulo escaleno. Calcular su perímetro 

    lado1 = int(input("Ingrese el lado 1: "))
    lado2 = int(input("Ingrese el lado 2: "))
    lado3 = int(input("Ingrese el lado 3: "))
    perimetro = lado1 + lado2 + lado3
    print("El perimetro del triangulo es igual a: ",perimetro)

elif (ejercicio == 2):

    """
    2-  Leer un número cualquiera y emitir el siguiente mensaje nulo(si es 
    cero), o positivo o negativo según sea el valor del número 
    """

    numero = int(input("Ingrese un numero cualquiera: "))
    if(numero == 0):
        print("El valor del numero es nulo")
    elif(numero < 0):
        print("El valor del numero es negativo")
    else:
        print("El valor del numero es positivo")

elif (ejercicio == 3):
    """
    3-  Leer dos variables N1 y N2. Ver si N1 es positivo, si lo es elevarlo 
    al cuadrado e imprimir el resultado. Y si N1 es 0 ó negativo sumarlo 
    a N2 y entonces elevar al cuadrado la suma para imprimir el 
    resultado
    """
    n1 = int(input("Ingrese un valor: "))
    n2 = int(input("Ingrese otro valor: "))
    if (n1 > 0):
        print("El cuadrado del primer valor es: ",n1**2)
    else:
        suma = (n1 + n2)**2
        print("El valor es 0 o negativo, el cuadrado de la suma de ambos valores es: ",suma)

elif (ejercicio == 4):

    """
    4-  Elaborar un programa que permita leer un solo número e imprima 
    su cubo
    """ 
    numero = int(input("Ingrese un valor: "))
    cubo = numero**3
    print("El cubo del valor ingresado es: ",cubo)

elif (ejercicio == 5):

    """
    5-  Escriba un programa que lea un número negativo e imprima el 
    número y el positivo del mismo
    """ 
    negativo = int(input("Ingrese un valor negativo: "))
    if (negativo < 0):
        print("El valor ingresado fue: ",negativo)
        print("y su valor absoluto es: ",abs(negativo))
    else:
        print("El valor ingresado es incorrecto!")

elif (ejercicio == 6):

    """
    6-  Se desea un programa para convertir metros a pies y pulgadas  
    (1 metro = 39.37 pulgadas, 1 pie = 12 pulgadas)
    """ 
    numero = int(input("Ingrese un valor en metros: "))
    pulgadas = numero * 39.37
    pies = pulgadas / 12
    print("El valor en pulgadas es: ",pulgadas)
    print("El valor en pies es: ",pies)

else:
    print("El valor ingresado no es valido!")

os.system("PAUSE")