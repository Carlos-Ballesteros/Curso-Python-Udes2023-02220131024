def añadirCliente(tuplaCliente):
    
    listaCliente=list(tuplaCliente)
    print("Introduzca el cliente:")
    clienteAñadir = [
        [],
    ]
    print("Nombre")
    clienteAñadir[0].append(str(input()))
    print("Apellido")
    clienteAñadir[0].append(str(input()))
    print("Contraseña")
    clienteAñadir[0].append(str(input()))
    return clienteAñadir

def eliminarCliente(tuplaCliente):
    dato = str(input())
    nueva_tupla = tuple([fila for fila in tuplaCliente if dato not in fila])
    return nueva_tupla

def buscarCliente(tuplaCliente):  
    print("Que cliente quieres buscar")
    buscar = str(input())
    for fila in tuplaCliente:
        if buscar in fila:
            return fila.index(buscar), tuplaCliente.index(fila)
    return "No se a encontrado"
def organizarTupla(tuplaCliente): 
    nueva_tupla = list(tuplaCliente)
    nueva_tupla.sort(key=lambda x: x[1])
    return tuple(nueva_tupla)
def revertirTupla(tuplaCliente): 
    nueva_tupla = list(tuplaCliente)
    nueva_tupla.reverse()
    return tuple(nueva_tupla)

tuplaCliente = (
    ("Nombre", "Apellido", "Contraseña"),
    ("Maria", "Juan", "contra1"),
    ("Ana", "Catalina", "14423"),
    )
proceso=1
while proceso >0:
    print("Que quieres hacer con la tupla?:")
    print("""
            (0)Salir
            (1)Imprimir clientes
            (2) Añadir cliente
            (3) Eliminar cliente
            (4) Buscar cliente
            (5) Organizar la tupla
            (6) Invertir la tupla
            """)
    proceso = int(input())
    match proceso:
        case 1:
            for e in range(len(tuplaCliente)): 
                print(str(e)+ ": " + str(tuplaCliente[e]))
        case 2:
            tuplaCliente = tuplaCliente + tuple(añadirCliente(tuplaCliente))
        case 3:
            auxLista = eliminarCliente(tuplaCliente)            
            tuplaCliente = auxLista
        case 4: 
            auxLista = buscarCliente(tuplaCliente)
            print("el cliente que busca esta en las coordenadas: " + str(auxLista))
        case 5:
            auxLista = organizarTupla(tuplaCliente)
            tuplaCliente = auxLista
        case 6:
            auxLista = revertirTupla(tuplaCliente)
            tuplaCliente = auxLista
            

for e in range(len(tuplaCliente)): 
    print(str(e) + ": " + str(tuplaCliente[e]))
