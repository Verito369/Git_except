#  Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#  captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
#  captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

try:
    primer_numero_str = input("Ingrese el primer número: ")
    segundo_numero_str = input("Ingrese el segundo número: ")

    primer_numero = float(primer_numero_str)
    segundo_numero = float(segundo_numero_str)

    resultado = primer_numero / segundo_numero
    print("El resultado de la división es:", resultado)

except ValueError:
    print("Error: Uno de los valores ingresados no es un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")