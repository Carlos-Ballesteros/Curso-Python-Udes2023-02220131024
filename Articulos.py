print("Ingrese los precios de los 5 articulos y la cantidad vendida de cada uno segun la sucursal")

print("Articulo 1")
print("Precio: ")
precio1 = (input())
print("Cantidad:")
print("Cantidad en sucursal 1: ")
cantSuc1_1 = (input())
print("Cantidad en sucursal 2: ")
cantSuc2_1 = (input())
print("Cantidad en sucursal 3: ")
cantSuc3_1 = (input())
print("Cantidad en sucursal 4: ")
cantSuc4_1 = (input())
cantidad1 = cantSuc1_1 + cantSuc2_1 + cantSuc3_1 + cantSuc4_1

print("Articulo 2")
print("Precio: ")
precio2 = (input())
print("Cantidad:")
print("Cantidad en sucursal 1: ")
cantSuc1_2 = (input())
print("Cantidad en sucursal 2: ")
cantSuc2_2 = (input())
print("Cantidad en sucursal 3: ")
cantSuc3_2 = (input())
print("Cantidad en sucursal 4: ")
cantSuc4_2 = (input())
cantidad2 = cantSuc1_2 + cantSuc2_2 + cantSuc3_2 + cantSuc4_2

print("Articulo 3")
print("Precio:")
precio3 = (input())
print("Cantidad:")
print("Cantidad en sucursal 1: ")
cantSuc1_3 = (input())
print("Cantidad en sucursal 2: ")
cantSuc2_3 = (input())
print("Cantidad en sucursal 3: ")
cantSuc3_3 = (input())
print("Cantidad en sucursal 4: ")
cantSuc4_3 = (input())
cantidad3 = cantSuc1_3 + cantSuc2_3 + cantSuc3_3 + cantSuc4_3

print("Articulo 4")
print("Precio: ")
precio4 = (input())
print("Cantidad:")
print("Cantidad en sucursal 1: ")
cantSuc1_4 = (input())
print("Cantidad en sucursal 2: ")
cantSuc2_4 = (input())
print("Cantidad en sucursal 3: ")
cantSuc3_4 = (input())
print("Cantidad en sucursal 4: ")
cantSuc4_4 = (input())
cantidad4 = cantSuc1_4 + cantSuc2_4 + cantSuc3_4 + cantSuc4_4

print("Articulo 5")
print("Precio: ")
precio5 = (input())
print("Cantidad:")
print("Cantidad en sucursal 1: ")
cantSuc1_5 = (input())
print("Cantidad en sucursal 2: ")
cantSuc2_5 = (input())
print("Cantidad en sucursal 3: ")
cantSuc3_5 = (input())
print("Cantidad en sucursal 4: ")
cantSuc4_5 = (input())
cantidad5 = cantSuc1_5 + cantSuc2_5 + cantSuc3_5 + cantSuc4_5

print("Articulo 1 Precio: " + str(precio1) + "Cantidad total: " + str(cantidad1) + "\n"+ "Articulo 2 Precio: " + str(precio2) + "Cantidad total: " + str(cantidad2) + "\n"+ "Articulo 3 Precio: " + str(precio3) + " la cantidad de la sucursal 3 es " + str(cantSuc3_3) +"Cantidad total: " + str(cantidad3) + "\n"+ "Articulo 4 Precio: " + str(precio4) + "Cantidad total: " + str(cantidad4) + "\n"+ "Articulo 5 Precio: " + str(precio5) + "Cantidad total: " + str(cantidad5) + "\n"+ "La cantidad total recaudada por la sucursal 1 es: " + str(precio1*int(cantSuc1_1+cantSuc1_2+cantSuc1_3+cantSuc1_4+cantSuc1_5)) + "\n"+ "La cantidad de articulos en la sucursal 2 es " + str(int(cantSuc2_1 + cantSuc2_2 + cantSuc2_3 + cantSuc2_4 + cantSuc2_5)) + "total recaudada por la sucursal 2 es: " + str(precio2*int(cantSuc2_1+cantSuc2_2+cantSuc2_3+cantSuc2_4+cantSuc2_5)) + "\n"+ "La cantidad total recaudada por la sucursal 3 es: " + str(precio3*int(cantSuc3_1+cantSuc3_2+cantSuc3_3+cantSuc3_4+cantSuc3_5)) + "\n"+ "La cantidad total recaudada por la sucursal 4 es: " + str(precio4*int(cantSuc4_1+cantSuc4_2+cantSuc4_3+cantSuc4_4+cantSuc4_5)) + "\n"+ "La recaudacion total de la empresa es: " + str(precio1*int(cantSuc1_1+cantSuc2_1+cantSuc3_1+cantSuc4_1 + precio2*cantSuc1_2+cantSuc2_2+cantSuc3_2+cantSuc4_2) + precio3*int(cantSuc1_3+cantSuc2_3+cantSuc3_3+cantSuc4_3) + precio4*int(cantSuc1_4+cantSuc2_4+cantSuc3_4+cantSuc4_4) + precio5*int(cantSuc1_5+cantSuc2_5+cantSuc3_5+cantSuc4_5)))