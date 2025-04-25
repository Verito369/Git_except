#  Imprimir un mensaje de error si no se pasan suficientes argumentos

def calcular_promedio(*args):
    if len(args) < 2:
        print("Error: No se pasaron suficientes argumentos")
    else:
        promedio = sum(args) / len(args) if len(args) > 0 else 0
        print(f"El promedio es: {promedio}")

entrada = input("Ingrese números separados por espacio: ").split()

numeros = [int(x) for x in entrada]

calcular_promedio(*numeros)

