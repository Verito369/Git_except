#  Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#  de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

a = 35
b = "hola"
#b = 7

try:
    respuesta = a + b
    print(respuesta)
except TypeError:
    print(f"Revise que los datos que ingresó sean numéricos!")