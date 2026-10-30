#Validação de nome (somente letras)
'''while True:
    nome = input('Digite o seu nome: ') #string
    if nome.replace(" ", " ").isalpha(): #substitui a palavra
        break
    else:
        print('Nome inválido. Use apenas letras e espaços')
'''

#Validação de CPF simples(Somente números e comprimento Fixo)
'''while True:
    cpf = input('Digite seu CPF (Apenas números): ')
    print(cpf.isdigit())
    if not cpf.isdigit() or len(cpf) != 11:
        print('CPF inválido. Digite apenas números!')
    else:
        break
print(f'CPF registrado: {cpf}')
'''

#Validação de E-mail (presença do @)
'''while True:
    email = input("Digite seu e-mail: ")
    if ("@" in email) and ("." in email) and email.index("@") < email.rindex("."):
        print(f'E-mail válido: {email}')
        break
    else:
        print("Email inválido. Tente novamente!")
'''
#Validação de opção no menu
'''while True:
    print('\nMenu:')
    print('1. Cadastro')
    print('2. Consulta')
    print('3. Quero chocolate')
    print('4. Sair')

    opcao = input('Escolha uma opção (1 - 2 - 3 - 4): ')

    if opcao not in('1', '2', '3', '4'):
        print('Opção Inválida')
    else:
        break
    
print(f'Tipo de variavel: {type(opcao)}')
opcao = int(opcao)
print(f'Tipo de variavel após converter: {type(opcao)}')

print(f'Você escolheu a opção: {opcao}')
'''

#Validação de resposta sim/não
'''while True:
    respota = input('Você deseja continuar (sim/não): ').strip().lower()
    if respota not in ('sim', 'não'):
        print('Resposta Inválida')
    else:
        break
print(f'Você escolheu: {respota}')
'''
