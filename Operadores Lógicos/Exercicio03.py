#Faça um programa que solicite dois números ao usuário (com decimais) 
# Em seguida solicite que o usuário informe a operação matemática (soma, subtração, multiplicação e divisão)

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
operação = input('Informe a operação matemática(soma, subtração, multiplicação, divisão): ').lower()
if operação == 'soma':
    print('n1 + n2')
elif operação == 'subtração':
    print('n1 - n2')
elif operação == 'multiplicação':
    print('n1 * n2')
elif operação == 'divisão':
    if n2 != 0:
        print('n1 / n2')
    else:
        print('Erro! Divisão por zero')
else:
    print('Operação Inválida!')