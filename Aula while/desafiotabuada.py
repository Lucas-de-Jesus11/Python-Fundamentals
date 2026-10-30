#Faça um programa que solicite ao usuário um número que ele queira treinar a tabuada.
#Irá solicitar ao mesmo a resposta do cálculo do número informado multiplicado por 1 até o 10.
#A cada resposta,você deverá validar e imprimir "CORRETO" ou "QUE PENA, VOCÊ ERROU, O VALOR CORRETO É X"
#No lugar de "x" coloque o valor correto.
#Ao final imprima"Total de aceros:y" e "Total de erros:z", onde "y" deverá ser o total de aceros e "z" o total de erros
#Ao final da sequência deve-se perguntar se deseja começão denovo.

print(
"""
+==========================================================================================================================+
| Olá, bem-Vindo ao Desafio da Tabuada!                                                                                    |
| Prepara-se para treinar suas habilidades matemáticas e se divertir enquanto aprende!                                     |
| Aqui você vai enfrentar desafios de multiplicação, testar sua velocidade e melhorar sua precisão nas tabuadas do 1 ao 10 |
| Você está pronto para começar? Então vamos lá!                                                                           |
| Boa sorte!                                                                                                               |
+==========================================================================================================================+
""")
from time import sleep
while True:
    numero = int(input('Qual tabuada você quer trinar? '))
    tot_acertos = 0
    tot_erros = 0
    i = 1
    while i <= 10:
      print('-' * 30)
      resposta = int(input(f'Quanto é {numero} x {i}? '))
      resultado_correto = numero * i
      if resposta == resultado_correto:
        print('Calculando...')
        sleep(1)
        print('CORRETO')
        tot_acertos += 1
      else:
        print('Calculando...')
        sleep(1)
        print(f'QUE PENA, VOCÊ ERROU , O VALOR CORRETO É {resultado_correto}')
        tot_erros += 1
      i += 1
    print('-' * 30)

    print(f'Total de acertos: \033[32m {tot_acertos}\033[m')
    print(f'Total de erros: \033[31m {tot_erros}\033[m')
    print('-' * 30)

    reiniciar = input('Deseja começar novamente? (s/n) ')
    if reiniciar.lower() != 's':
        print('ENCERRANDO...')
        sleep(2)
        print(
"""
+=======================================+
|Sessão Tabuada ENCERRADA. Volte sempre!|
+=======================================+
""")
        break
