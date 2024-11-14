from pyDatalog import pyDatalog

pyDatalog.create_terms('Colaborador, Projeto, ParticipaDe, DepartamentoColaborador, Senior, count, NomeColaborador, NomeProjeto, NomeDepartamento, Idade')

# Exercício 3: Identificação de Funcionários Experientes (1,0 Pontos) 
# Instrução:  Utilizando  os  fatos  da  base  de  dados,  crie  um  predicado  para  identificar 
# funcionários  considerados  experientes.  Um  funcionário  é  considerado  experiente  se 
# possui mais de 5 anos de experiência. 
# 1. Crie o predicado Experiente(X), onde X é um funcionário. 
# 2. Liste todos os funcionários experientes e o departamento ao qual pertencem. 
# 3. Conte quantos funcionários experientes existem em cada departamento e exiba 
# essa informação. 

# Leitura dos arquivos
with open("funcionarios.txt") as f:
    funcionarios = [line.strip().split(",") for line in f]

for nome, idade, departamento in funcionarios:
    if int(idade) > 5:
        +Experiente(nome)


# Listando colaboradores sêniores e seus departamentos
print("Funcionários Experientes e seus Departamentos:")
print((Senior(NomeColaborador) & DepartamentoColaborador(NomeColaborador, NomeDepartamento)))