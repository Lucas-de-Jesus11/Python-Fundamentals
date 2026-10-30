''' else:
        tem_maiusculo = False
        tem_minusculo = False
        tem_numero = False
    for s in senha1:
        if s.isupper():
            tem_maiusculo = True
        elif s.islower():
            tem_minusculo = True
        elif s.isdigit():
            tem_numero = True

'''