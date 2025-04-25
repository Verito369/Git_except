#  Buscar una palabra en una lista ingresada por teclado usando args y un operador
#  ternario

def buscar_palabra(palabra, *args):
    resultado = "Palabra encontrada" if palabra in args else "Palabra no encontrada"
    print(resultado)

entrada = input("Ingrese varias palabras separadas por espacio: ").split()

palabra_a_buscar = input("Ingrese la palabra a buscar: ")

buscar_palabra(palabra_a_buscar, *entrada)
