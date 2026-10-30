'''
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(len(matriz))
print(matriz[0][1]) #elemento da primeira linha, na segunda coluna: 2
print(matriz[1][2]) #elemento da segunda linha, na terceira coluna: 6
'''
#percorrendo uma matriz 3 x 3
'''matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(f'Tamanho da matriz: {len(matriz)}')
print('Elementos da matriz: ')
# I é a linha
# J é a coluna
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'Elemento [{i}][{j}] = {matriz [i][j]}')
'''

#criar uma matriz 3x3 com valores fornecidos pelo usuário
matriz = []
print('Preencha uma matriz 3x3')
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para posição: [{i}][{j}]'))
        linha.append(valor)
    matriz.append(linha)
print('Matriz: ')
for linha in matriz:
    print(linha)
