#  Determinar si un número es par o impar

def par_o_impar(num):
    return "Es par" if num % 2 == 0 else "Es impar"

numero = int(input("Ingrese un número: "))
print(par_o_impar(numero))
