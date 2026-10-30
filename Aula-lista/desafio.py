#Escreva um programa que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero. 
#Armazene osnúmeros em uma lista, depois percorra esta lista alimentando outras duas listas,uma com números pares e outra com números ímpares. 
#Ordene e imprima os números em ordem crescente e some os valores e imprima o resultado.
numero = []
par = []
impar = []
while True:
     num = int(input('Digite um número inteiro (0 para sair): '))
     numero.append(num)
     if num == 0:
        break
     if num % 2 == 0:
        par.append(num)
     else:
        impar.append(num)
par.sort()
impar.sort()
print(f'\nNúmeros inseridos: {numero}')
print(f'Os números pares ordenados são: {par}')
print(f'Os números impares ordenados são: {impar}')
soma_par = sum(par)
soma_impar = sum(impar)
tot_soma = soma_par + soma_impar
print(f'A soma dos pares é: {soma_par}')
print(f'A soma dos impares é: {soma_impar}')
print(f'A soma total é: {tot_soma}')