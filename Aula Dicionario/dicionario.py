#Criando uma lista
'''lista = ('Kaique', 31, 'Lucas', 28, 'marlon', 46)
print(type(lista))

#Criando uma tupla
tupla = ('Matheus', 15, 'Nycolas', 52, 'Sophia', 43)
print(type(tupla))
'''
#Criando um dicionário
'''aluno = {
    'nome': 'Lucas',
    'idade': 19,
    'curso': 'Desenvolvimento de Sistemas'
}
#temos que usar aspas simples no f-stings
print(f"Professor {aluno['nome']} que ministra o curso {aluno['curso']}")


#Acesando os valores dos dicionarios
print(aluno["nome"]) #Saida: Lucas
print(aluno["idade"]) #Saida:  19
'''
#Adicionando chave-valor no dicionário
'''aluno = {
    'nome': 'Lucas',
    'idade': 19,
    'curso': 'Desenvolvimento de Sistemas'
}
print(aluno)
#aluno["nota"] = 9.5
#aluno["nota"] = float(input('Digite sua nota: '))
nome_chave = input('Digite o que você quer adicionar: ')
aluno[nome_chave] = float(input('Digite sua nota: '))
print(aluno)

#Alterando o valor do dicionário
aluno['nome'] = "Valdinei"
print(aluno)

#Removendo um item do dicionario com del
print(aluno)
del aluno


#Removendo um intem do dicionario com pop
print(aluno)
idade = aluno.pop("idade")
print(idade)
print(aluno)
'''
#Obtendo itens do dicionario
'''carros = {'marca': 'VW', 'modelo': 'gol', 'ano_modelo': 2016}

#Ver todos os pares de chave-valor
print(f'itens do dicionário carros: \n {carros.items()}')

#Ver todas as chaves 
print(f'Chaves do dicionário carros: \n {carros.keys()}')

#Ver todos os valores
print(f'Valores do dicionário carros: \n {carros.values()}')
'''
#Percorrendo as chaves do dicionario
'''aluno = {
    'nome': 'Lucas',
    'idade': 19,
    'curso': 'Desenvolvimento de Sistemas'
}

for chave in aluno:
    print(chave)
print('--'*40)
#Percorrendo os valores do dicionario
for valor in aluno.values():
    print(valor)
print('--'*40)

#Percorrendo os itens do dicionário
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
'''
#Procurar um item no estoque
'''estoque = {
    'macbook': 1500,
    'camera': 1000,
    'celular': 4000,
    'monitor': 900
}
produto_procurado = input('Digite o produto que deseja: ').strip().lower()
if produto_procurado in estoque:
    print(f"O produto {produto_procurado} custa {estoque[produto_procurado]}")
else:
    print("Produto não encontrado")
'''