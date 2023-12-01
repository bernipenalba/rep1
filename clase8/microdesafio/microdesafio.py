"""
#si yo qiuero usar la clase alumno en este modulo/script debo importarla!!!
import alumnos #esta es una forma de importar


alumno1 = alumnos.Alumno(43564980, "Luciana", "Fernandez", 20)   #primero llamo al modulo, y luego del punto ya hago referencia a cosas que estan dentro del modulo. En este caso adentro del modulo tengo la clase alumno. Entonces para crear un alumno debo: Alumno()

print(alumno1)
alumno1.estudiar()
"""
from alumnos import Alumno #Esta es otra forma de importar. Siempre me conviene aclarar bien que quiero que traiga en vez de usar *

alumno1 = Alumno(43564980, "Luciana", "Fernandez", 20)   #ya no debo llamar al modulo! Llamo directamente a la clase que importe porque yo no importe alumnos, yo importe DESDE alumnos a la CLASE Alumnos!!!!!!!!

print(alumno1)
alumno1.estudiar()