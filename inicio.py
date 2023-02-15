# caso 1
print ("digite un numero entero positivo")
Numero = int(input())
i = 0
suma = 0
while Numero!=i:
    i = i+1
    suma = suma + i

print("La suma del rango es: " + str(suma))

# caso 2

print ("digite un numero entero positivo")
Numero = int(input())
i = 0
sumaPar = 0
sumaImpar = 0
while Numero!=i:
    i = i+1
    if i % 2 == 0:
        sumaPar = sumaPar + i
    else:
        sumaImpar = sumaImpar + i


print("La suma de los pares es: " + str(sumaPar))
print("La suma del rango es: " + str(sumaImpar))