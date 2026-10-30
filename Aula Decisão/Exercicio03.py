#Faça um programa que verifique o estado civil de uma pessoa
#Se a letra digitado é 'C' (Casado), 'S' (Solteiro), 'D' ('Divorciado), 'V' (Viúvo) ou  'O' (outros).
#Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil, exemplo:
#Usuário digita: C, seu programa deve responder: C - Casado

#estado_civil = input("Digite o estado civil \n('C' - Casado, 'S' - Solteiro, 'D' - Divorciado, 'V' - Viúvo, 'O' - Outros): ").upper()
estado_civil = input("Digite o estado civil: ").upper()
if estado_civil == 'C':
    print('C - Casado(a)')
elif estado_civil == 'S':
    print('S - Solteiro(a)')
elif estado_civil == 'D':
    print('D - Divorciado(a)')
elif estado_civil == 'V':
    print('V - Viúvo(a)')
elif estado_civil == 'O':
    print('O - Outro')
else:
    print('Opção inválida, por favor digite novamente!')