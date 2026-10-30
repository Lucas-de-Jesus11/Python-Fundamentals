#Calcule a obrigatoriedade do voto para uma pessoa dependendo de sua idade
#(16, 18 e 70)
#voto é facultativo:
#maiores de 16 anos e menores de 18 anos;
#maiores ou igual a 70 anos

idade = int(input('Digite sua idade: '))
if idade <= 16 or idade < 18 or idade >= 70:
    print('O voto é facultativo')
elif idade <= 18 or idade < 70:
    print('Voto obrigatório')
else:
    print('Não vota')