# Escreva uma função em Python chamada calcula_area_retangulo que:
# 1. Receba dois parâmetros, largura e altura.
# 2. Calcule a área do retângulo e armazene o resultado em uma variável local.
# 3. Imprima a área do retângulo dentro da função.
# 4. Tente acessar a variável que armazena a área fora da função e observe o que acontece. 

largura = float(input("Insira uma largura: "))
altura = float(input("Insira uma altura: "))

def calcula_area_retangulo(largura, altura):
    area = largura * altura
    print("Área: ", area)

calcula_area_retangulo(largura, altura)
#print(area) - Executar de fora da erro.