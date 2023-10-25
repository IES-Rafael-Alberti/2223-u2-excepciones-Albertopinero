'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.'''
def NumeroImpar(num):
    for i in range(1, num+1, 2):
        return i
    
if __name__ == "__main__":
    try:
    #entrada
        num = int(input("Introduce un número entero positivo: "))
        for i in range(1, num+1, 2):
            print(i, end=", ")
    except:
    #salida
        print("Error, entrada no válida.")