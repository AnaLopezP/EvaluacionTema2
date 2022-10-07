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

    
try:
    print(numero)

except ZeroDivisionError:
    print("No se puede dividir entre 0")

