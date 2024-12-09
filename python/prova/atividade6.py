# 1. Crie uma função chamada contador que possui uma variável interna count inicializada em 0.
# 2. Dentro da função contador, crie uma outra função interna chamada incrementar:
# - Incremente o valor de count em 1 sempre que for chamada.
# - Retorne o valor atualizado de count.
# 3. A função contador deve retornar a função incrementar.
# 4. No código principal, crie uma instância da função contador e chame a função incrementar diversas vezes, imprimindo o valor retornado a cada chamada.

def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

incrementar = contador()
print(incrementar())
print(incrementar())
print(incrementar())
