import ejercicio5

if __name__ == "__main__":
    vehiculos = []
    vehiculo1 = ejercicio5.Vehiculo("Negro", 120)
    print(vehiculo1)
    vehiculo2 = ejercicio5.Vehiculo("Amarillo", 200)
    print(vehiculo2)
    coche1 = ejercicio5.Coche("Blanco", 280,  40, 90)
    print(coche1)
    coche2 = ejercicio5.Coche("Azul", 150, 90, 45)
    print(coche2)

    vehiculos.append(vehiculo1)
    vehiculos.append(vehiculo2)
    vehiculos.append(coche1)
    vehiculos.append(coche2)