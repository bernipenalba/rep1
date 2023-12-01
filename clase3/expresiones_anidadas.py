nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

cumple_condiciones = (nombre != "****") and (5<edad<20) and (4<=len(nombre)<8) and (edad *3 >35)

if cumple_condiciones:
    print("Se cumplen las condiciones")
else:
    print("No se cumplen las condiciones")
    