
# Función de division simple de dos números con manejo de errores con la excepcion estándar ZeroDivisionError.
def division(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        return "Error, no puedes dividir por 0"
    return r