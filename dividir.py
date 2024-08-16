def division(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        return "Error, no puedes dividir por 0"
    return r