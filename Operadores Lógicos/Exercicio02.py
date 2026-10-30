#Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias:
#Infantil A = 5 a 7 anos, 
# Infantil B = 8 a 11 anos, 
# Juvenil A = 12 a 13 anos, 
# Juvenil B = 14 a 17 anos, 
# Adultos = Maiores de 18 anos

idade = int(input('Digite a idade do nadador: '))
if idade <= 5 or idade <= 7:
    print('Infantil A')
elif idade < 8 or idade <= 11:
    print('Infantil B')
elif idade <= 12 or idade <= 13:
    print('Juvenil A')
elif idade <= 14 or idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Adulto')
else:
    print('Idade fora das categorias')