# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

# Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

# Exemplo de entrada:

# Digite a porcentagem de desconto: 10 

# Digite o valor da compra: 200 

# Saída esperada:
# Preço final com desconto: 180.0 

# def desconto(valor_desconto):
#     def valor_compra(preco_compra):
#         return preco_compra * (1 - (valor_desconto / 100))
#     return valor_compra

# valor_desconto_digitado = float(input('Digite a porcentagem de desconto: '))
# valor_compra_digitado = float(input('Digite o valor da compra: '))

# funcao_calculo = desconto(valor_desconto_digitado)
# resultado = funcao_calculo(valor_compra_digitado)

# print(f'Preço final com desconto: {resultado}')


def criar_desconto(porcentagem):  

   def calcular_preco(valor):  

       return valor - (valor * (porcentagem / 100))  

   return calcular_preco 

desconto = float(input("Digite a porcentagem de desconto: "))  

calcular_preco_final = criar_desconto(desconto) 

valor = float(input("Digite o valor da compra: "))  

print(f"Preço final com desconto: {calcular_preco_final(valor)}") 
