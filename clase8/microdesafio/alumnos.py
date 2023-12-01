#creo una clase
class Alumno:
    def __init__(self, nro_doc, nombre, apellido, edad):
        self.doc = nro_doc
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return self.nombre +" "+ self.apellido

    def estudiar(Self):
        print("El alumno:", Self.nombre, "esta estudiando")