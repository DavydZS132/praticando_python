distancia_percorrida = float(input('Digite a distância percorrida (em km): '))

if distancia_percorrida <= 100:
    print('Pagar R$ 10,00')
elif 100 < distancia_percorrida <= 200:
    print('Pagar R$ 20,00')
else:
    print('Pagar R$ 30,00')