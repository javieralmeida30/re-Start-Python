Cesta = []
Condicion = "Si"
Total = 0
while Condicion == "Si":
    Producto = str(input("¿Qué producto desea?"))
    Cesta.append(Producto)
    Precio = int(input("¿Cuánto cuesta el producto?"))
    Cesta.append(Precio)
    Total = Total + Precio
    Condicion = str(input("¿Desea comprar otro producto? digite: Si/No"))

print(Cesta)
print("El precio total de tus compras es =", Total)