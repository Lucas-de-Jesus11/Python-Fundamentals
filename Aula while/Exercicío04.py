#Crie um programa em Linguagem Python que solicite a senha de um usuário e depois,peça pra digitar novamente até que as duas senhas sejam correspondentes

'''while True:
    senha = int(input('Digite sua senha: '))
    confirmação = int(input('Confirme sua senha: '))
    if senha == confirmação:
        print('Senha definida com sucesso! ')
        break
    else:
        print('Senha incorreta.Tente novamente!')
'''
senha1 = input('Digite a senha: ')
senha2 = input('Digite a senha novamente: ')
while senha1 != senha2:
    print('Senha errada')
    senha1 = input('Digite a senha: ')
    senha2 = input('Digite a senha novamente: ')
print('Senha confirmada')