'''Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, 
mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.'''
def NumeroEntero(num):
    if num >= 0:
        return num
    
if __name__ == "__main__":
    try:
    #entrada
        num = int(input("Escribe un número: "))
    #proceso
        if num >= 0:
            print("Correcto, este número es entero")
    except:
    #salida
        print("La entrada no es correcta.")