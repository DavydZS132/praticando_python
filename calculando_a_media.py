nota_1 = int(input('Digite a primeira nota: '))
nota_2 = int(input('Digite a segunda nota: '))
nota_3 = int(input('Digite a terceira nota: '))

resultado = (nota_1 + nota_2 + nota_3) / 3

if resultado >= 7:
    print('Aprovado')
elif 5 <= resultado < 7:
    print('Recuperação')
else:
    print('Reprovado')    