from src.ejercicio5 import CompruebaContraseña

def test_CompruebaContraseña():
    password = "alberto23"
    assert CompruebaContraseña(password) == "Contraseña Correcta!"