BD = {}

def registrar_usuarios(usuario,contrasena):
    BD[usuario] = contrasena
    print(f"Usuario '{usuario}' registrado con éxito.")


def login(usuario,contrasena):
    if usuario in BD and BD[usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrecta.")

def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario, contrasena in BD.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")

#Menu para elegir que funcion ejecuto
while True:
    print("\nMenú ")
    print("1. Registrar un usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios registrados")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        contrasena_usuario = input("Ingrese una contraseña: ")
        registrar_usuarios(nombre_usuario, contrasena_usuario)
    if opcion == "2":
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contrasena_usuario = input("Ingrese su contraseña: ")
        login(nombre_usuario, contrasena_usuario)
    if opcion == "3":
        mostrar_usuarios()
    if opcion == "4":
        print("Saliendo")
        break


