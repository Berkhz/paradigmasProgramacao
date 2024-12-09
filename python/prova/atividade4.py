# 1. Solicite ao usuário um número inteiro positivo.
# 2. Implemente uma função chamada fatorial que calcule o fatorial do número usando um loop while.
# 3. Dentro do programa principal, verifique se o número é maior que 0 antes de chamar a função fatorial. Se não for, solicite ao usuário um novo número até que ele insira um valor válido.
# Dica: O fatorial de um número n é o produto de todos os números inteiros de 1 até n.

def fatorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

numero = int(input("Digite um número inteiro positivo: "))
while numero <= 0:
    numero = int(input("Número inválido. Digite um número inteiro positivo: "))

print(f"Fatorial de {numero}: {fatorial(numero)}")
