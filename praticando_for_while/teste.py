numero_digitada = int(input('Digite um numero para a taboada: '))

for numero in range(2, 11, 2):
    resultado = numero_digitada * numero

    print(f'{numero_digitada} x {numero} = {resultado}')