#video7 - Polimorfismo
#primer ejemplo
"""
class Persona():
    def __init__(self):
        self.cedula = 12345678
    def mensaje(self):
        print("Mensaje desde la clase persona")

class Obrero(Persona):
    def __init__(self):
        self.especialista = 1
    def mensaje(self): #aqui implementamos polimorfismo
        print("Mensaje desde obrero")

persona1 = Persona()
persona1.mensaje()

obrero1 = Obrero()
obrero1.mensaje()



# EJEM DUCK TYPING
class Pato():
    def hablar(self):
        print("quak quak")

pato1 = Pato()
#pato1.hablar()

class Perro():
    def hablar(self):
        print("guau guau")
class Gato():
    def hablar(self):
        print("miau miau")

def llama_hablar(x):
    x.hablar()

 hacer esto o sino la proxima opcion
llama_hablar(pato1)
llama_hablar(Pato())
llama_hablar(Perro())
llama_hablar(Gato())

#ESta opcion
lista = [Pato(), Perro(), Gato()]
for animal in lista:
    animal.hablar()


#MICRODESAFIO
#crea una clase auto que tenga dos atributos de instancia. Con esta clase crea un auto y
#muestra los datos del auto creado

class Auto():
    #atributos de instancia:
    def __init__(self,marca,km):
        self.marca = marca
        self.km = km
    def mostrar_datos(self,):
        print(f"El auto es marca {self.marca} y tiene {self.km} kms")

auto1 = Auto("Peugeot","10000")



auto1 = Auto("Peugeot",10000)
auto1.mostrar_datos()
"""

#ACTIVIDADES DE CLASE
"""Implementar la Clase de Alumno, creada en la actividad anterior, directamente en Python.
Aclaraciones Generales:

El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
El método resultado, evalúa la nota correspondiente del estudiante. Si el estudiante saca menos o igual a 5 puntos desaprueba la materia, más de 5 puntos aprueba. Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.
Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno"""
"""
class Alumno():
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

  def imprimir(self):
    print(self.nombre, self.nota)

  def resultado(self):
    print('Aprobado' if self.nota > 5 else 'Desaprobado')

alumno1 = Alumno('Pepe', 3)
alumno2 = Alumno('Ricardo', 6)

alumno1.resultado()
"""
"""Crear una Clase Vehiculo de la cual van a heredar la clase Auto (del microdesafio) y la clase Lancha (nueva, tiene como atributo nombre de motor). Ademas, crear una clase MovimientosEmbarcacion de la cual tambien heredara Lancha.
Implementar los metodos arrancar, tocar_bocina, virar_a_estribor, virar_a_babor y abrir_capot en la clase que corresponda. Solo deben mostrar un mensaje que se ejecuto la accion."""

"""
class Vehiculo():
  def arrancar(self):
    print('Brrrum')
  def tocar_bocina(self):
    print('Piiii!!! Piiii!!!')

class MovimientosEmbarcacion():
  def virar_a_estribor(self):
    print('Virando a estribor.')
  def virar_a_babor(self):
    print('Virando a babor.')

class Auto(Vehiculo):
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
  def abrir_capot(self):
    print('Abriendo capot.')

class Lancha(Vehiculo, MovimientosEmbarcacion):
  def __init__(self, motor):
    self.motor = motor
"""
#EJERCICIO TELEVISORES
"""
Crear un programa que al pasarle una lista de televisores devuelva el total a pagar. Tener en cuenta los siguientes puntos sobre los televisores:

Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso.
Los colores disponibles son blanco, negro, rojo, azul y gris.
Por defecto, el color sera blanco, el consumo energético sera F, el precio_base es de 100 $ y el peso de 5 kg.
Tienen 3 funcionalidades:
Una para comprobar que la letra (consumo energético) es correcta, sino es correcta usara la letra por defecto. Se invocara al crear el objeto y sera privada.
Otra para comprobar que el color es correcto (no importa si el nombre esta en mayúsculas o en minúsculas), sino usa el color por defecto. Se invocara al crear el objeto y sera privada al igual que la anterior.
Y la ultima devolvera el precio final del televisor, que aumentara su precio según el tamaño y su consumo energético.
La lista de precios segun tamaño y consumo son:

Letra | Precio
  A   |   $100
  B   |    $80
  C   |    $60
  D   |    $50
  E   |    $30
  F   |    $10
Tamaño            | Precio
Entre 0 y 19 kg   |    $10
Entre 20 y 49 kg  |    $50
Entre 50 y 79 kg  |    $80
Mayor que 80 kg   |   $100
Probar con los siguientes televisores:

precio base 250, color rojo, consumo energético E y peso 10
precio base 143, color negro, consumo energético C y peso 13
precio base 54, color gris, consumo energético A y peso 7
precio base 300, color violeta, consumo energético B y peso 23
"""

class Televisor:

    #atributos de clase
  colores = ['blanco', 'negro', 'rojo', 'azul', 'gris'] #colores disponibles
  letras_costo = {'A': 100, 'B': 80, 'C': 60, 'D': 50, 'E': 30, 'F': 10}

    #constructor, LE MANDO DE ENTRADA LOS VALORES QUE QUIERO QUE TENGAN POR DEFECTO LAS DISTINTAS VARIABLES (O ARGUM)
  def __init__(self, precio_base=100, color='blanco', letra_consumo='F', peso=5):
    self.precio_base = precio_base
    self.color = self.__comprobar_color(color) #llamo a la func para comprobar el color, le paso como argum el color que ingrese el usuario en la lista de televisores. SE INVOCAN AL CREAR EL OBJ, O SEA AQUI!!
    self.letra_consumo = self.__comprobar_consumo(letra_consumo) #llamo a la func para comprobar la lista, paso como param la letra que ingrese el usuario
    self.peso = peso

    #empiezan aqui los METODOS
    #Este metodo es para comprobar que la letra que ingresan de consumo energetico es correcta
  def __comprobar_consumo(self, letra): #PRIVADA POR ESO LOS __
    return letra if letra.upper() in self.letras_costo.keys() else 'F'#si la letra ingresada no esta en la lista (dicc) devuelve la POR DEFECTO

  def __comprobar_color(self, color): #PRIVADA POR ESO LOS __
    return color if color.lower() in self.colores else 'blanco' #devuelvo blanco si lo ingresado no es correcto

    #metodo para calcular lo que me saldra en total el televisor
  def precio_final(self):
    if 0 <= self.peso <= 19: #empiezo con estos if para ver cuanto me costaria por el tamaño
      precio_x_tamanio = 10
    elif 20 <= self.peso <= 49:
      precio_x_tamanio = 50
    elif 50 <= self.peso <= 19:
      precio_x_tamanio = 80
    elif 80 <= self.peso:
      precio_x_tamanio = 100
      #ahora veo cuanto me cuesta por la letra. self.letra_consumo me trae UNA LETRA (porq llama a la func comprobar_consumo que devuelve una letra).  y luego uso letras_costo (que comparará con la letra que trajo la func que acabo de llamar) y me dara EL VALOR DEL COSTO de esa letra, y A eso lo guardo en precio_x_consumo
    precio_x_consumo = self.letras_costo.get(self.letra_consumo) 
    return self.precio_base + precio_x_consumo + precio_x_tamanio

#si compro mas de un televisor quiero ver cuanto me saldra todo, para eso los itero
def total_a_pagar(lista_teles): #le paso la lista de teles a comprar
    suma = 0
    for tele in lista_teles:
      suma += tele.precio_final() #llamo al metodo y voy acumulando los precios individuales en suma
    return suma

#pruebo con estos
#lista de televisores a comprar, paso los 4 argumentos que me pide el constructor
compras = [
    Televisor(250,'rojo', 'E', 10),
    Televisor(143,'negro', 'C', 13),
    Televisor(54,'gris', 'A', 7),
    Televisor(300,'violeta', 'B', 23),
]

#imprimo lo que me tira la funcion total a pagar, a la que le paso como argumento la lista que arme recien de televisores a comprar
print(total_a_pagar(compras))
