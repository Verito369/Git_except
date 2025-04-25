#  Calcular el promedio de una lista de números usando args y un operador ternario
def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    return promedio

resultado = calcular_promedio(5, 10, 15, 20)

print(f"El promedio es: {resultado}")

