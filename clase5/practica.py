#VIDEOS CLASE 5
#return
"""
def saludar_con_nombre():
    nombre=input("Escribe tu nombre: ")
    saludo = "Hola {}!. Bienvenido al curso de python".format(nombre)
    return saludo

saludo_generalizado = saludar_con_nombre()
print(saludo_generalizado)
"""

#parametros a funciones
"""def suma(operando1,operando2):
    return operando1+operando2

r = suma(7,5)
print(r)"""

#microdesafio clase 5
"""
Escribe una función a la que se le pase una cadena del nombre de una ciudad <ciudad> y muestre por pantalla el saludo ¡¡Hola, te damos la bienvenida a <ciudad>!.
#una forma
nombre_ciudad = input("Escribe el nombre de tu ciudad: ")
def saludo (nombre):
    print("¡¡Hola, te damos la bienvenida a {}".format(nombre))

saludo(nombre_ciudad)

#otra forma
def bienvenida_ciudad(nombre_ciudad):
    saludo = f"Hola, te damos la bienvenida a {nombre_ciudad}!"
    return saludo
print(bienvenida_ciudad('Cordoba'))
"""

#actividad clase 5 - calculo de media
#Escribe una función que reciba una muestra de números en una lista y devuelva su media.
"""
muestra = [2,4,6,8,10]

def calcular_media(listas):
    suma = sum(listas)
    media = suma / len(listas)

    return media
media = float(calcular_media(muestra))
print("La media de la lista es: ",media)
"""
#actividad clse 5 - calculo multiplo
"""Crea un programa que le pida dos números enteros al usuario y diga por consola si alguno de ellos es múltiplo del otro. 
La función debe llamarse es_multiplo().

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

def es_multiplo(numero1,numero2):
    if numero1 % numero2 == 0 or numero2 % numero1 ==0:
        print("{} y {} son multiplos".format(numero1,numero2))
    else:
        print("{} y {} NO son multiplos".format(numero1,numero2))

es_multiplo(num1,num2)
"""

#Actividad en vivo: Año bisiesto
"""Realiza una función llamada año_bisiesto que le permita al usuario ingresar un año y verificar si es o no bisiesto:
Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

Información a tener en cuenta:

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

def año_bisiesto(año):
    #verificamos si el año es un número. isdigit devuelve un valor distinto de cero si c es un dígito decimal (0 - 9).
    if not año.isdigit():
        print("Por favor ingrese un año numérico válido")
        return
    
    #Convertimos el año a entero
    año = int(año)

    #Verificamos si el año es bisiesto
    if (año % 4 == 0 and año % 100 !=0) or (año % 400 == 0):
        print("El año {} es bisiesto".format(año))
    else:
        print("El año {} NO es bisiesto".format(año))

#solicitamos al usuario un año
año_ingresado = input("Ingrese un año: ")
año_bisiesto(año_ingresado)
"""

#Actividad pares e impares
"""Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares.
Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

def separar(lista):
    # Inicializar listas para números pares e impares
    numeros_pares = []
    numeros_impares = []

    # Iterar a través de la lista de números
    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)
    # Ordenar las listas resultantes
    numeros_pares.sort()
    numeros_impares.sort()

    print("La lista de numeros pares quedaría: ",numeros_pares)
    print ("La lista de numeros impares quedaría: ",numeros_impares)

separar([1,5,8,6,2,4,3])
"""
