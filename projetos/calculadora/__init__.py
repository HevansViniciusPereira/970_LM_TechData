from funcoes import *

def calcule():
    try:
        a = float(input("Digite um numero: "))
        b = float(input("Digite um numero: "))
    except:
        print("Digite um unico valor numerico")

    operacao = input("""
    Digite o numera operacao que quer realizar:
    1) soma
    2) subtracao
    3) multiplicacao
    4) divisao
    """)

    if operacao == '1':
        return soma
    elif operacao == '2':
        return subtracao
    elif operacao == '3':
        return multiplicacao
    elif operacao == '4':
        return divisao
    else:
        print("Operacao inválida")