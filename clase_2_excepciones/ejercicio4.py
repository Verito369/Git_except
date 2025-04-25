#  Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#  FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
#  embargo, también intenta crear el archivo si no existe.

nombre_archivo = "mi_archivo.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(f"Contenido del archivo '{nombre_archivo}': {contenido}")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Este es un nuevo archivo creado desde el bloque else.")
        print(f"Se ha creado el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error al intentar crear el archivo: {e}")
else:
    pass 