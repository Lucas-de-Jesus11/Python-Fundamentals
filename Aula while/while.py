#Imprimir gol da Alemanha 7 vezes
"""gols = 0
while gols < 7:
    gols += 1
    print('Gol da Alemanha')
print('Gol do Brasil')"""

"""valor = 0
while valor < 10:
    print(valor)
    valor += 1"""

'''contador = 1
soma = 0
while contador <= 5:
    soma = soma + contador 
    contador += 1  
print(f'A soma é {soma}')'''

#Usando else no while
'''x = 0
while x < 10:
    print(f'Valor de x nessa interação é {x}')
    print('X ainda é menor que 10, somando 1 a x')
    x += 1
else:
    print('Acabou o loop')
print(x)'''

'''valor = int(input('Quanto é 2 + 2: '))
while valor != 4:
    print('Errou')
    valor = int(input('Quanto é 2 + 2: '))
else:
    print('Certa a resposta')'''

#Pass, break
'''valor = 0
while valor < 10:
    if valor == 4:
        #break #Para o código
        continue #continua o código
    else:
        #Nenhuma ação especifica
        pass #Instrução nula
    print(valor)
    valor += 1 '''

#média da sala de aula usando o while
#Quando utilizar o while True tem que colocar o break
'''notas = 0
qtd_notas = 0
while True:
    nota = float(input('Informe a nota: (-1 para finalizar) '))
    if nota == -1:
        break
    notas += nota
    qtd_notas = qtd_notas + 1
    
if qtd_notas > 0:
    media = notas / qtd_notas
    print(f'Quantidade de notas informadas {qtd_notas}')
    print(f'Média das notas: {notas / qtd_notas:.2f}')
else:
    print('Nenhuma nota informada!')'''

#Desafio
'''while True:
    pergunta = str(input('Você gosta de Python? ')).upper()
    if pergunta == 'SIM':
        print('Resposta correta')
        break
    else:
        print('Esta não é a resposta correta')
'''
