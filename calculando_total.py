# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

# Exemplo de entrada:

# Digite os valores das vendas: 100 250 300 

# Saída esperada:

# O total de vendas foi: 650 

# total = 0

# def calcular_valor(valor_despesas):
#     return int(valor_despesas)

# while True:
#     total_digitado = input('Digite os valores das vendas (Digite Sair para sair): ')

#     if total_digitado == 'Sair':
#         print('Finalizando app')
#         break
#     else:
#         valor_convertido = calcular_valor(total_digitado)
#         total = total + valor_convertido

# print(f'O total de vendas foi: {total}')


valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) 
print(f"O total de vendas foi: {total}") 