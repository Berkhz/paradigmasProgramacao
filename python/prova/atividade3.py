# Escreva uma função em Python chamada calcular_media que:
# 1. Receba uma lista de números como parâmetro.
# 2. Calcule e retorne a média dos números.
# 3. Crie uma segunda função chamada media_aprovacao que receba a lista de notas dos alunos e imprima "Aprovado" se a média for maior ou igual a 7, e "Reprovado" caso contrário.

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def media_aprovacao(notas):
    print("Aprovado" if calcular_media(notas) >= 7 else "Reprovado")
