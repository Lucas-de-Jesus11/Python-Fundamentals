filmes = [['Até o Último Homem','Drama', 2016],['O Milagre na Sela 7','Comédia', 2019],['IT a Coisa','Terror', 2017],['Tropa de Elite 1','Ação',2007 ]]

#Adicionando Menu Principal
print('Menu de Opções:')
print(
"""
+=====================+
| 1- Cadastrar Filmes |
| 2- Listar Filmes    |
| 3- Buscar por Gênero|
| 4- Excluir Filmes   |
| 5- Sair do Menu     | 
+=====================+
""")

#Função para Cadastar Filmes
opcao = int(input('Escolha sua opção: '))
while True:
    if opcao == 1:
         matriz = []
    for i in range(1):
        linha = []
        for j in range(3):
            filme = str(input('Adicione o nome do filme: ')).strip()
            gênero = str(input('Digite o gênero do filme: ')).strip()
            ano = int(input('Agora informe o ano de lançamento do filme: '))
            filme.append(filmes)
            gênero.append(filmes)
            ano.append(filmes)
        filmes.append(linha)
    print('Filme Adicionado com Sucesso! ')
    for linha in filmes:
        print(linha)



#Função para Listar Filmes

#Função para buscar filmes por gênero

#Função para excluir filmes

#Função para sair do menu
    if opcao == 5:
         print(
"""
+===============================+
|Sessão ENCERRADA. Volte sempre!|
+===============================+
""")
    break
     