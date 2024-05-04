# Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade = float(input('Velocidade registrada pelo radar: '))
multa = (velocidade - 80) * 20
if velocidade > 80:
    print('\033[1;30;41mMULTADO!!!!\033[m\nVocê foi multado em R${:.2f} por está dirigindo acima da velocidade permitida.'.format(multa))
