from pyDatalog import pyDatalog
pyDatalog.create_terms('Colaborador, Projeto, ParticipaDe, DepartamentoColaborador, Senior, count, NomeColaborador, NomeProjeto, NomeDepartamento, Idade')

# Leitura dos arquivos
with open("colaboradores.txt") as f:
    colaboradores = [line.strip().split(",") for line in f]

with open("projetos.txt") as f:
    projetos = [line.strip().split(",") for line in f]

with open("alocacoes.txt") as f:
    alocacoes = [line.strip().split(",") for line in f]

# Questão 1: Listagem de Colaboradores e Projetos
for nome, idade, departamento in colaboradores:
    +Colaborador(nome)
for nome, departamento in projetos:
    +Projeto(nome)

# Exibindo todos os colaboradores e projetos
print("Colaboradores:")
print(Colaborador(NomeColaborador))
print("Projetos:")
print(Projeto(NomeProjeto))

# Questão 2: Relações entre Colaboradores e Projetos
for nome, idade, departamento in colaboradores:
    +DepartamentoColaborador(nome, departamento)
for nome, projeto in alocacoes:
    +ParticipaDe(nome, projeto)

# Listando todos os colaboradores, seus projetos e departamentos
print("Colaboradores, Projetos e Departamentos:")
print((ParticipaDe(NomeColaborador, NomeProjeto) & DepartamentoColaborador(NomeColaborador, NomeDepartamento)))

# Questão 3: Identificação de Colaboradores Sêniores
for nome, idade, departamento in colaboradores:
    if int(idade) > 30:
        +Senior(nome)

# Listando colaboradores sêniores e seus departamentos
print("Colaboradores Sêniores e seus Departamentos:")
print((Senior(NomeColaborador) & DepartamentoColaborador(NomeColaborador, NomeDepartamento)))

# Contando colaboradores sêniores por departamento
print("Número de Colaboradores Sêniores por Departamento:")
print((Senior(NomeColaborador) & DepartamentoColaborador(NomeColaborador, NomeDepartamento)).count(NomeDepartamento))