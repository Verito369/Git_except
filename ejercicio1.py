#  Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#  captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

a = 35
b = 0
#b = 5

try:
    respuesta = a/b
    print(respuesta)
except ZeroDivisionError:
    print(f"El divisor no puede ser 0, intente con otro nro!")
