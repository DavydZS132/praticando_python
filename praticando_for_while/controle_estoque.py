for i in range(4, -1, -1):
    print(f'Venda realizada! Estoque: {i}')
print('Estoque esgotado')

estoque = 5

while estoque > 0:
    estoque -= 1 
    print(f"Venda realizada! Estoque restante: {estoque}")

print("Estoque esgotado")
