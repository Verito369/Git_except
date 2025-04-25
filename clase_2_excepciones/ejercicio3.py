#  Escribe un programa que intente acceder a una clave que no existe en un
#  diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
#  un mensaje de error al usuario.

diccionario = {"hortaliza": "papa", "legumbre": "soja"}

try:
    diccionario
    print(diccionario["fruta"])
except Exception as e:
     print(f"Lo que solicita no se encuentra en el diccionario. {e}")
