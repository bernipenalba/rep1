#microdesafio
"""En la función de nuestro ejercicio hay un fallo potencial (aritmético), averigua cuándo sucede y retorna el valor None en ese caso especial, en cualquier otro caso devuelve el resultado normal de la función.

>>> def dividir(a, b):
return a/b

Pista😉 : El fallo es aritmético y se da por un valor que no podría pasarse por el parámetro b

a=float(input("Ingrese un numero: "))
b=float(input("Ingrese otro numero: "))

def dividir(a, b):
    try:
        resultado = a/b
        return resultado
    except ZeroDivisionError:
        return None # Manejar la división por cero retornando None

print("El resultado de la division es: ", dividir(a,b))
"""

"""Puede que algunos lo hayan encontrado, pero tomando el ejercicio anterior pareciera que la función no solo al dividir por cero pueda generar un error. ¿Qué pasa si pasamos strings a nuestra función como argumento? 

Deberás acomodar la solución del microdesafío para que devuelva el mensaje “El error encontrado es del tipo:” concatenado con el tipo de error que se encontró específico para cada caso.

Ejemplo:
El error encontrado es del tipo: ZeroDivisionError

a=(input("Ingrese un numero: "))
b=(input("Ingrese otro numero: "))

def dividir(a, b):
    a = int(a)
    b = int(b)
    try:
        resultado = a/b
        return resultado
    except ZeroDivisionError as e:
        print("Ha ocurrido un error del tipo ",type(e).__name__)
        return None # Manejar la división por cero retornando None
    except TypeError as e:
        print("Ha ocurrido un error del tipo ",type(e).__name__)
        return None 
    
print("El resultado de la division es: ", dividir(a,b))
"""
"""Crea un programa que muestre un menú con 4 opciones y, según la opción elegida por el usuario, muestre el tipo de error que se generaría si se ejecutara ese código en Python.

Usa las siguientes opciones:
‘Soy un string’ - 4
4/0
prnt(‘Mostrando codigo’)
int(‘Quiero ser un numero’)
"""
while True:
    print("Menú de Opciones:")
    print("1. 'Soy un string'")
    print("2. 4/0")
    print("3. prnt('Mostrando codigo')")
    print("4. int('Quiero ser un numero')")
    print("5. Salir")

    opcion = input("Elige una opción (1/2/3/4/5): ")

    if opcion == "1":
        try:
            resultado = 'Soy un string'
            print(type(resultado).__name__)
        except Exception as e:
            print(f"El error encontrado es del tipo: {type(e).__name__}")
    elif opcion == "2":
        try:
            resultado = 4 / 0
            print(resultado)
        except Exception as e:
            print(f"El error encontrado es del tipo: {type(e).__name__}")
    elif opcion == "3":
        try:
            resultado = prnt('Mostrando codigo')
            print(resultado)
        except Exception as e:
            print(f"El error encontrado es del tipo: {type(e).__name__}")
    elif opcion == "4":
        try:
            resultado = int('Quiero ser un numero')
            print(resultado)
        except Exception as e:
            print(f"El error encontrado es del tipo: {type(e).__name__}")
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida (1/2/3/4/5).")


