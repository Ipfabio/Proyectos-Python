import sys
import  socket

objetivo = socket.gethostbyname(input("Inserte la dirección IP: "))

# Acá ingresamos (por ej) la dirección ip obtenida anteriormente
print("Escaneando objetivo: " + objetivo)

try: # Recorremos uno a uno por lo que la búsqueda va a ser lenta
    for port in range (1, 150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print(f"El puerto {port} está abierto")
        s.close()
except:
    print("\n Saliendo...")
    sys.exit(0)