renda = float(input('Digite o valor da sua renda mensal: '))
valor_parcela = float(input('Digite o valor da parcela desejada: '))

if renda > 2000 and valor_parcela <= renda * 0.30:
    print('Emprestimo Aprovado.')
elif renda <= 200:
    print('Valor da renda menor que o desejado.')
else:
    print('Empretimo negado: parcela acima de 30% da renda')
