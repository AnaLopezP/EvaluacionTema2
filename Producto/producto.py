class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto se ha creado con exito")
    
    def getnombre(self):
        return self.nombre

    def setnombre(self,nombre):
        self.nombre = nombre

    def getcodigo(self):
        return self.codigo

    def setcodigo(self,codigo):
        self.codigo = codigo

    def getprecio(self):
        return self.precio

    def setprecio(self, precio):
        self.precio = precio

    def gettipo(self):
        return self.tipo

    def settipo(self,tipo):
        self.tipo = tipo

    def __str__(self):
        return("Producto con código: " + str(self.codigo) + ", nombre: "+ str(self.nombre) + ", precio: " + str(self.precio) + " y tipo: " + str(self.tipo))

