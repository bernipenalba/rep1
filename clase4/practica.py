"""Desafío 04
Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
"""
num = int(input("Ingrese un numero impar: "))

while num%2 == 0: #Es decir, mientras es par sigue en el bucle, cuando ingrese un par sale del bucle
    print("El numero ingresado no es correcto")
    num = int(input("Por favor ingrese un numero IMPAR nuevamente: "))

print("EL numero impar {} es correcto".format(num))


#Ejercicio en vivo CALCULADORA
"""Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""

# Solicitar al usuario ingresar dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
    
while True:
    # Mostrar el menú de opciones
    print("\nMenú de Opciones:")
    print("1. Mostrar suma de los dos números")
    print("2. Mostrar resta (primer número - segundo número)")
    print("3. Mostrar multiplicación de los dos números")
    print("4. Salir del programa")
        
    opcion = input("Elige una opción (1/2/3/4): ")
        
    if opcion == "1":
        suma = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es {suma}.") #como el while sigue siendo true, vuelve a empezar el bucle, es decir, vuelve a mostrar el menu
    elif opcion == "2":
        resta = numero1 - numero2
        print(f"La resta de {numero1} y {numero2} es {resta}.")
    elif opcion == "3":
        multiplicacion = numero1 * numero2
        print(f"La multiplicación de {numero1} y {numero2} es {multiplicacion}.")
    elif opcion == "4":
        print("¡Hasta luego!")
        break  # Salir del bucle y finalizar el programa
    else:
        print("Opción no válida. Por favor, elige una opción válida (1/2/3/4).")


#Ejemplo de que pasa en cada caso:

#caso 1
c = 0
while c < 10:
    c += 1
    if c == 2:
        pass #No hace nada con PASS
    print('c vale', c)

#caso 2
c = 0
while c < 10:
    c += 1
    if c == 2:
        continue #Lo saltea con CONTINUE
    print('c vale', c)

#caso 3
c = 0
while c < 10:
    c += 1
    if c == 2:
        break #Rompe el bucle con BREAK
    print('c vale', c)

#Ejemplo con RANGE EN VIVO
"""Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))
"""

mi_lista1 = list(range(11))
mi_lista2 = list(range(-10,1))
mi_lista3 = list(range(0,21,2))
mi_lista4 = list(range(-19,1,2))
mi_lista5 = list(range(0,51,5))

print(mi_lista1)
print(mi_lista2)
print(mi_lista3)
print(mi_lista4)
print(mi_lista5)

#Actividad de HASTA EL EXIT
#  
"""Solicita al usuario números enteros para sumarlos.
Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit. El programa debe validar dicha acción y dejar de solicitar números. 
Finalmente, el algoritmo debe mostrar la suma obtenida.

isdigit() en Python para verificar si una cadena (string) contiene solo caracteres numéricos. Esta función retorna True si todos los caracteres en la cadena son dígitos numéricos y False en caso contrario
"""
suma = 0

while True :
    entrada = input("Ingrese un numero entero o 'exit' para finalizar: ")
    
    if entrada.lower() == "exit":
        break #salir del bucle si el usuario ingrsa exit
    else:
        try: 
            num = int(entrada)
            suma = suma + num
        except ValueError: #En caso que ingrese otra cosa que no sea un num o la palabra exit, imprime ese msj de error y comienza el bucle de nuevo
            print("Entrada no válida. Por favor, ingrese un número entero o 'exit'.")

print(f"La suma de todos los numeros ingresados es: {suma}")

#Actividad de la MEDIA
"""Escribe un programa que pida al usuario cuantos números quiere introducir. Luego, lee todos los números, guardándolos en una lista, y realiza una media aritmética de todos los valores.
Ayuda: Puedes utilizar la funciones sum() entre paréntesis se le pasa un iterable (lista, tupla, range) y devuelve la suma de todos sus elementos (sirve solo con valores numéricos)
"""

cant = int(input("Cuantos numeros quiere introducir: "))
i=0
lista = []
while i < cant:
    a = int(input("Ingrese un numero: "))
    lista.append(a)
    i = i + 1

media = sum(lista) / cant
print(f"La media de los {cant} elementos introducidos es {media} ")

#Actividad en vivo EL TOTAL O EXIT
"""Reformulemos un poquito el enunciado del ejemplo “Hasta el exit”.

Solicita al usuario la cantidad de números enteros a sumar.
Luego, permítele ingresarlos uno por uno hasta que se ingresen todos o el usuario escriba la palabra ‘exit’.
El programa debe validar que se ingresó ‘exit’ y dejar de solicitar números. 

Finalmente, el algoritmo debe mostrar la suma obtenida con un mensaje que resalte si fue total la carga de datos o parcial (debido al ingreso de ‘exit’)."""
#Una forma de hacerlo: con while

cant = int(input("Cuantos numeros enteros quiere sumar: "))
lista = []
i = 0

while i < cant:
    a = (input("Ingrese un numero o exit: "))

    if a.lower() == "exit":
        break
    else:
        try: 
            a = int(a)
            lista.append(a)
            i = i + 1
        except ValueError: #En caso de que no ingrese un numero o exit lo manda al inicio del bucle de nuevo
            print("Ingreso no válido, vuelva a intentarlo")

suma = sum(lista)
print(f"El resultado de haber sumado {i} de los {cant} numeros a ingresar es: {suma}")

#otra forma de hacerlo con for y range
cant_de_ingresos = int(input("Ingrese la cantidad de numeros a sumar:"))
suma = 0
for iteracion in range(cant_de_ingresos):
  valor = input("Ingrese un numero:")
  if valor == 'exit':
    print('La suma parcial da:', suma)
    break
  suma += int(valor)
else:
  print('La suma total da:', suma)

"""cant_de_ingresos es una variable que contiene un número entero ingresado por el usuario utilizando input(). Este número representa cuántos números se sumarán en total.

range(cant_de_ingresos) crea una secuencia de números desde 0 hasta cant_de_ingresos - 1. En otras palabras, si el usuario ingresa 5 en cant_de_ingresos, range(5) generará la secuencia (0, 1, 2, 3, 4)."""

#Actividad instrucciones e iteracion
"""1) Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:
Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.
2) Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).
"""
#Primero creo el programa que sume todo
lista = list(range(1,100,2))
suma = sum(lista)

#Ahora pido al usuario
while True:
    entrada = int(input("Ingrese un numero entero del 0 al 9: "))
    if (0<entrada<=9) :
        if entrada in lista:
            print(f"El valor {entrada} se encuentra en la lista de números")
            break 
        else:
            print(f"El valor {entrada} no se encuentra en la lista de numeros")
            break
    else:
        print("El numero ingresado no es correcto. Ingrese un numero entre 0 y 9: ")
    

    




