#definicion de la clase Vehiculo de la cual van a heredar todos los vehiculos
class Vehiculo:
    #constructor
    def __init__(self, marca, modelo, capacidad_combustible):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_combustible = capacidad_combustible #el nombre que ponga despues del .self es el nombre que toma la variable! Si yo cuando en el init nombro al argumento capacidad_combustible hubiera puesto comb y luego del = hubiera puesto comb funciona igual! Pero su nombre verdadero es capacidad_combustible
    
    #para que si yo pongo print a un vehiculo me aparezca ESTE MSJ y no uno raro
    def __str__(self):
        return "Marca: " + self.marca + " Modelo: " + self.modelo
    
    def moverse(self):
        print("El vehiculo de la marca", self.marca, "modelo", self.modelo, "esta en movimiento")

#esta clase solo da funcionalidad a los objetos de tipo embarcacion, es decir si lancha hereda de esta clase, va a tenr integrado los metodos virar
class MovimientoEmbarcacion:
    def virar_estribor(self):
        print("Esta embarcacion esta virando a estribor")
    def virar_babor(self):
        print("Esta embarcacion esta virando a babor")  

#--------------------DEFINICION DE VEHICULOS------------------
class Auto(Vehiculo):
    def __init__(self, marca, modelo, comb, color, nro_puertas): #Le agrego color y nro_puertas
        super().__init__(marca, modelo, comb)  #agrego el constructor de la clase padre, SIN SELF!!!
        self.color = color 
        self.puertas = nro_puertas #aqui la variable se llamara realmente puertas, no nro_puertas
    def tocar_bocina(self):
        print("Este auto esta haciendo piiii piiiiiiii") 
    #Los autos van a tener entonces los metodos moverse (heredado) y tocar_bocina

class Lancha(Vehiculo, MovimientoEmbarcacion): #hereda de las dos clases
    def __init__(self, marca ,modelo, comb, asientos, calado):
        super().__init__(marca, modelo, comb)
        self.nro_asientos = asientos
        self.calado = calado
    #Las lanchas tendran entonces los metodos moverse (heredado de vehiculo) y virar a babor y estribor (heredados de movEmbarc)

#----------------------------------------------

automovil1 = Auto("Toyota", "Corolla", 50, "Verde musgo", 3)
automovil2 = Auto("Audi", "A4", 50, "Azul espacial", 4)

lancha1 = Lancha("Yamaha", "125", 100, 5, 1.5)

print(automovil1)
print(automovil2) #printeo la info completa 

automovil2.moverse()
lancha1.virar_babor()
lancha1.virar_estribor()
automovil1.tocar_bocina()


        