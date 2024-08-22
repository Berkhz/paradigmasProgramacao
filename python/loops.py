numero = int(input("Insira um número para calcular seu fatorial: "))

fatorial = 1

for x in range(1, numero + 1):
    fatorial *= x

print(f"O fatorial de {numero} é {fatorial}")