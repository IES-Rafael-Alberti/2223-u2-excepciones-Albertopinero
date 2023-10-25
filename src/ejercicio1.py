'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''
def CumplirAños(años):
    for i in range(años):
        return i

if __name__ == "__main__":
    try:
    #entrada
        años = int(input("Escribe tu edad: "))

    #proceso
        for i in range(años):
            print("Has cumplido", i, "años")
    except:
        print("Edad no válida.")        

    #salida