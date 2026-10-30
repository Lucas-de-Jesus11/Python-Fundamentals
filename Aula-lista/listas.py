'''
#criando uma lista
bancos = ['Banco do Brasil', 'Caixa', 'Santander' ]

#criando lista vazia
meu_vetor = []
print(type(bancos))
print(bancos)

#alterando um valor da lista
bancos[1] = 'Inter'

#alterando o último elemento da lista
bancos[-1] = 'C6'
print(bancos)
'''

'''
#percorrer os valores do vetor
for banco in bancos:
    print(banco)

bancos = bancos + ['Bradesco', 'Nubank']
#bancos += ['Bradesco', 'Nubank']
print(bancos)
'''


'''
#percorrendo os valores com for
cores = ['Vermelho', 'Azul', 'Verde']
for i in range(len(cores)):
    cor = cores [i]
    print(f'Cor no indice {i} é: {cor}')
'''


'''
#criando uma lista de frutas
frutas = ['Maça', 'banana', 'laranja', 'manga']
print(f'Lista original: {frutas}')

#adicionar uma fruta na lista no final da lista/vetor
frutas.append('uva')
print(f'Após adicionar a uva: {frutas}')

#inserindo uma fruta em uma posição
frutas.insert(2, 'Morango')
print(f'Após inserir o morango na posição 2: {frutas}')

#remover uma fruta
frutas.remove('banana')
print(f'Após remover a banana: {frutas}')

#ordernando as frutas em ordem alfabética
frutas.sort()
print(f'Lista ordenada em ordem alfabética: {frutas}')

#invertendo a ordem da lista
frutas.reverse()
print(f'Lista em ordem inversa: {frutas}')

#contar quantas vezes aparece uma fruta
qtd = frutas.count('maça')
print(f'A fruta maçã aparece {qtd} vezes na lista')

#removendo a última lista da lista e armazenando em uma variavel
ultima_fruta= frutas.pop()
print(f'Após usar o pop(): {frutas} ')
print(f'Fruta removida: {ultima_fruta} ')

#removendo frutas dentro de um intervalo de indices
del frutas[0: 2] #não inclui o indice 2
print(f'Após remover frutas do indice 0 a 1: {frutas}')

#limpando todos os itens da lista
frutas.clear()
print(f'Lista após ser limpa: {frutas}')

#adionar outros elementos de outra lista
frutas.extend(['Abacaxi', 'pera', 'melão', 'kiwi'])
print(f'Lista com frutas novas: {frutas}')

#usando index para encontrar a posição de um ite,
posicao = frutas.index('melão')
print(f'A fruta melão está na posição: {posicao}')
'''

'''
#lista dentro de uma lista
compras = [10.5, 3.50, 28.5, ['tomate', 'sabonete', 'arroz']]
print(compras)
produtos = compras[3]
print(produtos)

#somando os valores
total = compras[0] + compras[1] + compras[2]
print(total)
'''

'''
#para verificar uma existencia de um item na lista
letras = ['a', 'b', 'c', 'd', 'e']
var = input('Informe uma letra:').lower()
if var in letras:
    print(f'A letra {var} está na lista')
else:
    print(f'A letra {var} não está na lista')
'''

'''#Adicionar elementos na lista fornecido pelo usuário
tarefas = []
tarefa = input('Digite uma tarefa: ')
tarefas.append(tarefa)
print(tarefas)

while tarefa != '':
    tarefa = input('Digite uma tarefa: ')
    tarefas.append(tarefa)
print(tarefas)
'''

'''
nova = []
while True:
    num = int(input('Digite um número inteiro (0 para sair): '))
    if num == 0:
        break
    else:
        nova.append(num)
print(nova)

#somar itens da lista
print(sum(nova))
#maior valor da lista max()
print(max(nova))
#menor valor da lista min()
print(min(nova))
'''

'''
produtos = ['apple tv', 'air pods', 'mac', 'iphone 15', 'ipad']
novo_produto = produtos.append(input('Digite o produto: '))

#removendo um item
item_removido = input('Digite o produto que deseja remover: ').lower()
if item_removido in produtos:
    produtos.remove(item_removido)
    print('Produto removido!')
else:
    print(f'{item_removido} não existe na lista de produtos da apple.')
for i in produtos:
    print(i)
'''
