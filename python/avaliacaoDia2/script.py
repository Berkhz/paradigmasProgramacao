# Exercício 6: Análise de Funcionários por Projeto e Departamento (1,0 Pontos) 
# Instrução:  Realize  uma  análise  de  quais  funcionários  de  diferentes  departamentos 
# trabalham nos mesmos projetos, estabelecendo relações entre eles. 
# 1. Crie  um  predicado  ColegaDeProjeto(X,  Y),  onde  X  e  Y  são  funcionários  de 
# departamentos diferentes que trabalham no mesmo projeto. 
# 2. Liste  os  pares  de  funcionários  que  são  colegas  de  projeto  e  seus  respectivos 
# projetos. 
# 3. Adicione uma contagem de quantos colegas de projeto cada funcionário possui.

import csv
from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('Funcionario, Projeto, Departamento, ColegaDeProjeto, ContarColegas, X, Y, P, Count')

def carregar_dados_arquivos():
    funcionarios = []
    projetos = []
    
    with open('funcionarios_projetos.txt', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  
        for row in reader:
            funcionarios.append((row[0], row[1]))  
    
    with open('funcionarios_departamento.txt', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  
        departamento_dict = {row[0]: row[1] for row in reader}  
    
    for nome, projeto in funcionarios:
        departamento = departamento_dict.get(nome, 'Desconhecido')
        +Funcionario(nome, projeto, departamento)
    
    with open('projetos.txt', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  
        for row in reader:
            projetos.append((row[0], row[1]))  
    
    return funcionarios, projetos

funcionarios, projetos = carregar_dados_arquivos()

ColegaDeProjeto(X, Y, P) <= (
    Funcionario(X, P, D1) &
    Funcionario(Y, P, D2) &
    (D1 != D2) &
    (X != Y)
)

ContarColegas(X, Count) <= (
    ColegaDeProjeto(X, Y, P) &
    Count == len_(Y)
)

print("Pares de Colegas de Projeto:")
for colega in ColegaDeProjeto(X, Y, P):
    print(f"{colega[X]} e {colega[Y]} no {colega[P]}")

print("\nNúmero de Colegas de Projeto por Funcionário:")
for contagem in ContarColegas(X, Count):
    print(f"{contagem[X]} tem {contagem[Count]} colegas de projeto")