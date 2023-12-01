cantidad_de_numeros = int(input("Cuántos números quiere introducir?: "))

lista = [] #creo una lista vacía

for i in range(cantidad_de_numeros):
    numero = input ("Ingrese el numero: ") 
    lista.append(numero)

print("Lista de numeros: ", lista)

promedio = sum(lista) / cantidad_de_numeros #o podemos dividir por len(lista) o sino len(range(cantidad_de_numeros))

print("El promedio de los numeros ingresados es: ", promedio) #no hace falta pasar a float porque python en las div automaticamente las convierte a flotante