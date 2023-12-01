#microdesafio
"""En una lista encontraremos diferentes operaciones lógicas. Calcula mentalmente el resultado de cada expresión y almacénalo en una nueva lista, la cual contendrá únicamente valores lógicos True y False. 
"""
expresiones = [
    not False,
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23,
    12 > 7 and True < False
]
lista = [True,True,True,True,True,False]

#Actividad EXPRESIONES ANIDADAS
"""A partir de dos variables llamadas NOMBRE y EDAD (deben ser datos solicitados al usuario con input), debes crear una variable que almacene si se cumplen todas las siguientes condiciones, encadenando operadores lógicos en una sola línea:
NOMBRE sea diferente de cuatro asteriscos “****”
EDAD sea mayor que 5 y a su vez menor que 20
Que la longitud de NOMBRE sea mayor o igual a 4  pero a la vez menor que 8
EDAD multiplicada por 3 sea mayor que 35

Luego muestra el resultado. Si te animas, puedes mostrar, en lugar del resultado booleano, un mensaje que indique si se cumplen o no las condiciones.
"""
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if (nombre != '****') and (5<edad<20) and (4<=len(nombre)<8) and (edad*3 > 35):
    print("Si se cumplen todas las condiciones.")
else:
    print("No se cumplen todas las condiciones")


#Actividad de las GENERACIONES
"""Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado. 
Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: “No existe generación asociada”
"""
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

if 1920<=año_nacimiento<=1940:
    print("Usted pertenece a la generacion SILENCIOSA")
elif 1946<=año_nacimiento<=1964:
    print("Usted pertenece a la generacion BABY BOOMER")
elif 1965<=año_nacimiento<=1979:
    print("Usted pertenece a la generacion X")
elif 1980<=año_nacimiento<=2000:
    print("Usted pertenece a la generacion Y")
elif 2001<=año_nacimiento<=2010:
    print("Usted pertenece a la generacion Z")
else:
    print("No existe generacion asociada")


#Actividad CREDITO BANCARIO
"""Para aprobar un crédito, el cliente debe ser mayor de edad. Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.  En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. Si no cumple ninguna de las condiciones, no se aprueba el crédito

Datos iniciales
edad = 15
antigüedad = 10
ingreso = 1500
"""

edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Ingrese su antiguedad: "))
ingreso = int(input("Indique su ingreso mensual: "))

if edad >= 18:
    if antiguedad >= 3:
        if ingreso > 2500:
            print("Credito aprobado!")
        else:
            print("Credito denegado")
    else:
        if ingreso >= 4000:
            print("Credito aprobado!")
        else:
            print("Credito denegado")
else:
    print("Credito denegado")


