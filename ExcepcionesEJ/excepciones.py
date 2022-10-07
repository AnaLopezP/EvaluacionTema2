#primer codigo:
numero = 7/0

#segundo codigo:
lista = [4, 7, 30, 23, 5]

lista[10]

#tercer codigo:
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

paises["alemania"]

#cuarto codigo:
resultado = "2" + 10

class dividir_exception(BaseException):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def get_mensaje(self):
        return self.mensaje

    