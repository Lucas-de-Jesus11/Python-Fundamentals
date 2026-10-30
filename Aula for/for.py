'''
for i in range(7):
    print('Gol da Alemanha')
'''

#Usando range
'''
for i in range(3):
    print(i)'''

#Imprimir os valores no intervalo de 0 a 11 :
'''
#range (inicio, fim, salto)
for contador in range(0, 11 , 2):
    print(contador)
'''

#for (para cada) i (item) in(dentro) lista
'''
notas_alunos = [10,9,8,9,3]
for i in notas_alunos:
    print(i)'''

'''nome = 'Lucas'
for i in nome:
    print(i)
'''

#Usando break para o for
'''
for gol in range(1000):
    print('Gol da Alemanha')
    if gol == 6:
        break
print('Chega de gol :(')
print('Gol do Brasil')
'''
#Usando o comando continue e else
'''
for i in [1,10,20,30,35,40,50]:
    if i == 35:
        continue
    print(i)
else:
    print('Acabou')
'''
#Somando os valores limitados a 50.
'''inicio = int(input('Digite o primeiro número: '))
fim = int(input('Digite o último número: '))
salto = int(input('Digite o  salto: '))
total = 0
texto = 'Cálculo: 5 + '
for numero in range(inicio,fim,salto):
    total += numero
    texto = texto + str(numero)
    if numero >= 50:
        break
    if numero != fim-1:
        texto = texto + ' + '
print(texto)
print(total)
'''
#média de sala
'''qtd_alunos = int(input('Quantidade de alunos da turma: '))
total = 0
for aluno in range(qtd_alunos):
    nota = float(input(f'Digite a nota do {aluno+1}º aluno:'))
    total += nota
print(f'A média  da turma é {total/qtd_alunos:.1f}')
'''