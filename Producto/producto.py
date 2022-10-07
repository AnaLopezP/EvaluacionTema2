class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto se ha creado con exito")
    
    def __str__(self):
        return("Producto con código: " + str(self.codigo) + ", nombre: "+ str(self.nombre) + ", precio: " + str(self.precio) + " y tipo: " + str(self.tipo))
        