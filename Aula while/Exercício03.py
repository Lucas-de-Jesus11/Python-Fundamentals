#Faça um programa que calcule o número médio de alunos por turma.Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma
# As turmas não podem ter mais de 40 anos. 
'''num_turmas = int(input('Digite o número de turmas: '))
total_alunos = 0
turma = 1
while turma <= num_turmas:
    alunos_turmas = int(input(f'Digite o número de alunos da turma {turma} (máx 40): '))
    if alunos_turmas > 40:
        print('A turma não pode ter mais de 40 aluno. Tente novamente.')
    else:
        total_alunos += alunos_turmas
        turma += 1
média_alunos = total_alunos / num_turmas
print(f'A média de alunos por turmas é {média_alunos:.2f}')
'''


turmas = int(input('Digite a quantidade de turmas na unidade: '))
contador = 0
soma = 0
while contador < turmas:
    alunos = int(input(f'Digite a quantidade de alunos das turmas {contador+1}:  '))
    if alunos <= 40:
        contador += 1
        soma += alunos
    else:
        print('Os números de alunos não pode passar de 40')
print(f'A média das turmas é {soma/turmas:.0f}')
