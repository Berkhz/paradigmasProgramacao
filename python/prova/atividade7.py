# 1. Implemente uma função geradora chamada gerador_de_quadrados que: 
# - Receba um números inteiro n como parâmetro.
# - Gere os quadrados de números de 1 até n.
# 2. No código principal, solicite ao usuário um número inteiro positivo.
# 3. Use a função geradora para imprimir os quadrados dos números de 1 até o número fornecido pelo usuário.

def gerador_de_quadrados(n):
    for i in range(1, n + 1):
        yield i ** 2

numero = int(input("Digite um número inteiro positivo: "))
while numero <= 0:
    numero = int(input("Número inválido. Digite um número inteiro positivo: "))

for quadrado in gerador_de_quadrados(numero):
    print(quadrado)
