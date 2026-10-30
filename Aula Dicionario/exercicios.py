
#Crie um sistema de consulta de preços
#seu sistema deve:
# -Pedir para o usuário o nome de um produto
# -Caso o produto exista no dicionário de produtos, o programa deve retornar o preço do produto como resposta
# -Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente

'''
while True:
    comida = {
        'água': 3.00 ,
        'salada de frutas': 3.50,
        'sanduiche': 4.00,
        'cachorro-quente': 4.50
    }
    produto_procurado = input('Digite o produto que deseja: ').strip().lower()
    if produto_procurado in comida:
        print(f"O produto {produto_procurado} custa: R${comida[produto_procurado]}")
        break
    else:
        print("Produto não encontrado. Digite novamente: ")
'''

#Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto.
#Se ele responder sim, o programa deve pedir o nome do produto e o preço do produto e cadastrar no dicionário de preçoes
#Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de preços atualizado
'''comida = {
        'água': 3.00 ,
        'salada de frutas': 3.50,
        'sanduiche': 4.00,
        'cachorro-quente': 4.50
    }
while True:
    produto_procurado = input('Digite o produto que deseja: ').strip().lower()
    if produto_procurado in comida:
        print(f"O produto {produto_procurado} custa: R${comida[produto_procurado]}")
        break
    else:
        resposta = input("Produto não encontrado. Deseja cadastrar esse produto? (sim/não):  ").strip().lower()
        if resposta  == 'sim':
            novo_produto = input('Digite o novo produto: ').strip().lower()
            preco_produto = float(input('Digite o preço do produto: R$'))
            comida[novo_produto] = preco_produto
            print('Produto cadastrado com sucesso!')
            print('Dicionário de preços atualizados: ')
            print(comida)
            break
        else:
            print('Produto não cadastrado. Tente novamente!')
'''

#Edite o programa para que ele também permita remover produtos existentes
#Caso o usuário escolha essa opção , o programa deve pedir o nome do produto a ser removido
#Se o produto não existir, uma mensaem deve ser exibida
#Após a remoção bem-sucedida, mostre uma mensagem de sucesso.
print(" Menu de opções: \n"
        "1- Consultar produtos\n"
        "2- Adicionar produtos\n "  
    "3- Excluir produtos\n ")

comida = {
        'água': 3.00 ,
        'salada de frutas': 3.50,
        'sanduiche': 4.00,
        'cachorro-quente': 4.50
    }
opção = input('Informe sua opção: ')
while True:
    if opção == 1:
        produto_procurado = input('Digite o produto que deseja: ').strip().lower()
    if produto_procurado in comida:
        print(f"O produto {produto_procurado} custa: R${comida[produto_procurado]}")
        break
    else:
        if opção == 2:
            resposta = input("Produto não encontrado. Deseja cadastrar esse produto? (sim/não):  ").strip().lower()
        if resposta  == 'sim':
            novo_produto = input('Digite o novo produto: ').strip().lower()
            preco_produto = float(input('Digite o preço do produto: R$'))
            comida[novo_produto] = preco_produto
            print('Produto cadastrado com sucesso!')
            print('Dicionário de preços atualizados: ')
            print(comida)
            break
        else:
            print('Produto não cadastrado. Tente novamente!')