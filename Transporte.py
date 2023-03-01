
print("Ingrese el nombre del conductor")
Nombre = input()
while not Nombre.isalpha():
    print("Por favor ingrese un nombre valido")
    Nombre = input()
    if  Nombre.isalpha():
        break
print("Ingrese los kilometros que recorrio")
Kms = str(input())
while not Kms.isnumeric() and not Kms < 0:
    print("Por favor ingrese una distancia valida")
    Kms = input()
    if Nombre.isnumeric() and Kms > 0:
        break
print(Nombre + " a recorrido " + Kms + "km esta semana")