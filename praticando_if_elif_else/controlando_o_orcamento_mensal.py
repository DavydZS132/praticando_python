total = 0

while True:
    valor_digitado = input('Digite cada valor gasto (Digite (sair) para sair ): ')

    if valor_digitado == 'sair':
        print('App encerrado.')
        break
    else:
        valor_digitado = float(valor_digitado)
        total = total + valor_digitado

if total < 3000:
    print('Você está dentro do orçamento previsto.')
elif total == 3000:
    print('Você atingiu exatamente o limite do orçamento.')
else:
    print('Atenção! Você ultrapassou o limite do orçameto.')