# 1. Solicite ao usuário dois números inteiros.
# 2. Calcule a soma, subtração, multiplicação e divisão dos números.
# 3. Imprima os resultados na tela.

um = int(input("Insira 1 (um) número inteiro: "))
dois = int(input("Insira outro número inteiro: "))

def soma(um, dois):
    return (um + dois)

def subtracao(um, dois):
    return (um - dois)

def multiplicacao(um, dois):
    return (um * dois)

def divisao(um, dois):
    return (um / dois)

print(soma(um, dois))
print(subtracao(um, dois))
print(multiplicacao(um, dois))
print(divisao(um, dois))