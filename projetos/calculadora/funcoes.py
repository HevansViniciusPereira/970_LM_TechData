def soma(a,b):
    try:
        a = float(a)
        b = float(b)
    except TypeError:
        print("a e b devem ser numeros")

    return a+b

def substracao(a,b):
    try:
        a = float(a)
        b = float(b)
    except TypeError:
        print("a e b devem ser numeros")

    return a-b