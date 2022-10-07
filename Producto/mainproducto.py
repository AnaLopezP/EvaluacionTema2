import producto

if __name__ == "__main__":
    producto1 = producto.Producto(1234, "MAXIDENT", 45, "Album")
    print(producto1)
    print("Voy a modificar el producto creado")
    producto1 = producto.Producto(2345, "MAXIDENT - Skz", 45, "Album")
    print(producto1)