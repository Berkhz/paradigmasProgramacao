from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms('Funcionario, Projeto, Departamento, TrabalhaEm, ResponsavelPor, Experiencia, FuncionarioDepartamento')
pyDatalog.create_terms('ColegaDeProjeto, ContarColegas, X, Y, P, D1, D2, Count, sum_')

def ler_arquivo(caminho, separador=';'):
    with open(caminho, 'r') as f:
        linhas = f.readlines()
    return [linha.strip().split(separador) for linha in linhas[1:]]

funcionarios = ler_arquivo('python/avaliacaoDia2/arquivos/funcionarios.txt')
departamentos = ler_arquivo('python/avaliacaoDia2/arquivos/departamentos.txt')
projetos = ler_arquivo('python/avaliacaoDia2/arquivos/projetos.txt')
alocacoes = ler_arquivo('python/avaliacaoDia2/arquivos/alocacoes.txt')

for nome, depto, anos_exp in funcionarios:
    +Funcionario(nome)
    +FuncionarioDepartamento(nome, depto)
    +Experiencia(nome, int(anos_exp))

for nome_depto, qtd_func in departamentos:
    +Departamento(nome_depto)

for nome_proj, depto_responsavel in projetos:
    +Projeto(nome_proj)
    +ResponsavelPor(nome_proj, depto_responsavel)

for nome_func, nome_proj in alocacoes:
    +TrabalhaEm(nome_func, nome_proj)

ColegaDeProjeto(X, Y, P) <= (
    TrabalhaEm(X, P) & TrabalhaEm(Y, P) & (X != Y) & 
    FuncionarioDepartamento(X, D1) & FuncionarioDepartamento(Y, D2) & (D1 != D2)
)

ContarColegas(X, Count) <= (
    Count == sum_(1, for_each=(Y, P)) & ColegaDeProjeto(X, Y, P)
)

print("Pares de funcionários que são colegas de projeto (de departamentos diferentes):")
print(ColegaDeProjeto(X, Y, P))

print("\nContagem de colegas de projeto por funcionário:")
print(ContarColegas(X, Count))