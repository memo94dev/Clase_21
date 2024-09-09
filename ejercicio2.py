import os

# Ejercitario numero 2

ejercicio = int(input("Cual ejercitario desea probar? elija del 1 al 7: "))
if (ejercicio == 1):

    """
    1- Hallar el promedio de tres números enteros 
    ingresados por teclado. 
    """
    num1 = int(input("Ingrese un valor"))
    num2 = int(input("Ingrese un valor"))
    num3 = int(input("Ingrese un valor"))
    promedio = (num1 + num2 + num3)
    print("El promedio de los 3 valores ingresados es: ",promedio)

elif (ejercicio == 2):
    
    # 2- Hallar el área de un cuadrado. 

    lado = int(input("Ingresa el valor del lado del cuadrado: "))
    area = lado**2
    print("El area del cuadrado es: ",area)

elif (ejercicio == 3):

    # 3- Hallar el perímetro de un cuadrado. 

    lado = int(input("Ingrese el valor del lado del cuadrado: "))
    perimetro = lado *4
    print("El perimetro del cuadrado es: ",perimetro)

elif (ejercicio == 4):

    """
    4- Un individuo desea invertir su capital en un banco y 
    desea saber cuánto dinero ganará después de un 
    mes, si el banco paga a 2% de interés mensual.
    """ 

    capital = int(input("Ingrese su capital a invertir: "))
    interes = capital * 0.02
    total = capital + interes
    print("Su interes al cabo de un mes sera de: ",interes)
    print("Su ganancia al cabo de un mes sera de: ",total)

elif (ejercicio == 5):
 
    """
    5- Programa que se lea un número entero por teclado y 
    se indique si el numero introducido es par o impar.
    """  

    numero = int(input("Ingrese un numero entero: "))
    if (numero == 0):
        print("El valor ingresado es nulo")
    elif (numero % 2 == 0):
        print("El valor es par")
    else:
        print("El valor es impar")

elif (ejercicio == 6):
 
    """
    6- Declara 2 variables numéricas (con el valor que 
    desees), he indica cual es mayor de los dos. Si son 
    iguales indicarlo también. Vas cambiando los valores 
    para comprobar que funciona.
    """

    numero1 = int(input("Ingrese un numero entero: "))
    numero2 = int(input("Ingrese un numero entero: "))
    if (numero1 == numero2):
        print("Los valores ingresasdos son iguales")
    elif (numero1 > numero2):
        print("El primer valor es el mayor: ",numero1)
    else:
        print("El segundo valor es mayor: ",numero2)

elif (ejercicio == 7):
 
    """
    7- Lee un número por teclado e indica si es divisible por 
    3. Si no lo es, también debemos indicarlo
    """

    numero = int(input("Ingrese un numero entero: "))
    if (numero % 3 == 0):
        print("El numero ingresado es divisible por 3")
    else:
        print("El valor ingresado NO es divisible por 3")

else:
    print("El valor ingresado es incorrecto!")
    
os.system("PAUSE")