# 1. Implemente uma função chamada encontrar_maximo que receba uma lista de números inteiros e retorne o maior valor da lista.
# 2. Dentro do programa principal, crie uma lista de números aleatórios gerada automaticamente com 10 elementos (entre 1 e 100).
# 3. Utilize a função encontrar_maximo para encontrar e imprimir o maior valor da lista gerada.
# Dica: Utilize a biblioteca random para gerar os números aleatórios com a função random.randint().

import random

def encontrar_maximo(lista):
    return max(lista)

numeros = [random.randint(1, 100) for _ in range(10)]
print(f"Lista: {numeros}")
print(f"Maior valor: {encontrar_maximo(numeros)}")
