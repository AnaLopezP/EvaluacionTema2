from typing_extensions import Self


class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno ha sido creado con éxito.")
    
    def getnombre(self):
        return self.nombre

    def setnombre(self,nombre):
        self.nombre = nombre

    def getnota(self):
        return self.nota

    def setnota(self,nota):
        self.nota = nota

    def calificacion(nota):
        nota = input("Introduzca una nota de alumno: ")
        if nota >= 5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")

    

            