#primer codigo:
try:
    numero = 7/0
    print(numero)

except ZeroDivisionError:
    print("No se puede dividir entre 0")

#segundo codigo:
try:
    lista = [4, 7, 30, 23, 5]
    lista[10]
except IndexError:
    print("No hay tantos elementos en la lista.")

#tercer codigo:
try:
    paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
    paises["alemania"]
except KeyError:
    print("No existe la clave alemania en el diccionario")


#cuarto codigo:
try:
    resultado = "2" + 10
except TypeError:
    print("No puedes sumar dos tipos de variables distintas.")
    print("Usa la funcion int() para el 2, y convertirlo así en un numero.")





