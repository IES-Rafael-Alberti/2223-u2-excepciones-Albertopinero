'''Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"'''
def CompruebaContraseña(passsword):
    passw = "alberto23"
    if password != passw:
        return password
    
if __name__ == "__main__":   
    try: 
        passw = "alberto23"
    #entrada
        password = input("Escribe la contraseña: ")

    #proceso
        if password != passw:
            raise NameError("Incorrect Password!!")
        else:
            print("Contraseña Correcta!")
    except:
    #salida
        print("Incorrect Password!!")

        

