class Alumno:
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

    def calificacion(self):
        #nota = input("Introduzca una nota de alumno: ")
        if self.nota >= 5:
            print("El alumno " + str(self.nombre) +" ha aprobado")
        else:
            print("El alumno " + str(self.nombre) + " ha suspendido")
    def __str__(self):
        return("Alumno con nombre: " + str(self.nombre) + " y nota: " + str(self.nota))
    



            