peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

resultado = peso / (altura * altura)
print(f'Seu IMC é: {resultado:.2f}')

if resultado < 18.5:
    print('Você está abaixo do Peso')
elif resultado <= 24.9:
    print('Você está no peso Normal')
elif resultado <=39.9:
    print('Você está com Sobrepeso')
else:
    print('Você está com Obesidade Grave')