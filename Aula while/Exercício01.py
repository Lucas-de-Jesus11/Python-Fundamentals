#Desafio
'''while True:
    pergunta = str(input('Você gosta de Python? ')).upper()
    if pergunta == 'SIM':
        print('Resposta correta')
        break
    else:
        print('Esta não é a resposta correta')'''

#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido...
#opção 1:
'''while True:
    nota = float(input('Informe uma nota de 0 a 10: '))
    if nota > 0 and nota < 10:
        print('Valor válido')
        break
    else:
        print('Valor invalido.Tente novamente') '''
#opção 2:
'''while True:
    nota = float(input('Digite um número de 0 a 10: '))
    if 0 <= nota <= 10:
        print(f"Nota válida: {nota}")
        break
    else:
        print("Valor inválido! A nota deve estar entre 0 e 10.")
'''
