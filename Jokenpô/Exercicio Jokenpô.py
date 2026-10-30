#Escreva um programa em Python que peça para o usuário fazer duas jogadas entre Pedra, papel ou tesoura.
#Uma para o primeiro jogador, outra para o segundo. Depois diga qual deles ganhou a disputa.

from random import randint
from time import sleep
itens = ('Pedra', ' Papel', 'Tesoura')
jogador = randint (0, 2)
print('-=-' * 20)
print('Vamos jogar Jokenpô?')
print('-=-' * 20)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador1 = int(input('Jogador 1. Qual é sua jogada: '))
jogador2 = int(input('Jogador 2. Qual é sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-='*12)
print(f'Jogador 1 jogou {itens[jogador1]}')
print(f'Jogador 2 jogou {itens[jogador2]}')
print('-='*12)
if jogador1 == jogador2:
    print('Empate')
elif (jogador1 == 0 and jogador2 == 2) or (jogador1 == 1 and jogador2 == 0) or  (jogador1 == 2 and jogador2 == 1):
     print('Jogador 1 venceu')
else:
     print('Jogador 2 venceu')