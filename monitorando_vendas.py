maca = int(input('Digite a quantidade de Maça vendidas: '))
banana = int(input('Digite a quantidade de Banana vendidas: '))

if maca > banana:
    print(f'Vendeu mais maça do que banana. Vendeu {maca} maça e vendeu {banana} banana')
elif banana > maca:
    print(f'Vendeu mais banana do que maça. Vendeu {maca} maça e vendeu {banana} banana')
else:
    print(f'Vendeu a mesma quantidade. Vendeu {maca} maça e vendeu {banana} banana')