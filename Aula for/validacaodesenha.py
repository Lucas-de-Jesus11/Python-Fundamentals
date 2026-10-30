#Peça ao usuário para digitar uma senha e depois que confirme a senha, digitado-a novamente. O programa deve verificar se:
#As dua senhas digitadas são iguais
#A senha tem pelo menos 8 caracteres
#A senha contém pelo menos uma letra maiuscula, uma minuscula e um número
#Caso as senhas não sejam iguais, exiba a mensagem:
#Se a senha não atender aos critérios de comprimento ou conteúdo, exiba a mensagem 
#caso a senha esteja correta, exiba "Senha confirmada é valida"
#Usar os métodos len(), isupper(), islower() e isdigit() para ajudar na validação da senha


#senha e confirmação de senha
print("Cadastre sua senha com os seguintes critérios: \n"
      "         Ao menos 8 caracteres\n"
      "         Ao menos uma letra MAIÚSCULA\n"
      "         Ao menos uma letra MINUSCULA\n"
      "         Ao menos um número\n")

senha = input('Digite sua senha: ')
confirmacao = input('Agora confirme sua senha: ')
while True:
     if senha != confirmacao:
         senha = input('\033[31mAs senhas não são iguais. Tente novamente:\033[m ') #Adicionando cor
         confirmacao = input('Agora confirme sua senha: ')
    #confirmação dos critérios
     else: 
        #verifica se a senha tem 8 caracteres
        if len(senha) < 8:
            print('\033[31mA senha deve conter pelo menos 8 caracteres\033[m')
            senha = input('Digite sua senha novamente: ')
            confirmacao = input('Agora confirme sua senha: ')
        #verifica se a senha tem letra maiuscula
        if senha.islower():
            print('\033[31mA senha deve ter pelo menos um caracter maiusculo:\033[m')
            senha = input('Digite sua senha novamente: ')
            confirmacao = input('Agora confirme sua senha: ')
        #verifica se a senha tem letra minuscula
        if  senha.isupper():
            print('\033[31mA senha deve ter pelo menos um caracter minusculo:\033[m ') 
            senha = input('Digite sua senha novamente: ')
            confirmacao = input('Agora confirme sua senha: ')
        #verifica se a senha tem número
        if senha.isalpha():
            print(f'\033[31mA senha deve ter um número:\033[m ')
            senha = input('Digite sua senha novamente: ')
            confirmacao = input('Agora confirme sua senha: ')  
            #verifica se todos os critérios forem atendidos
        break

print('\033[32mSenha confirmada com sucesso!\033[m') 
