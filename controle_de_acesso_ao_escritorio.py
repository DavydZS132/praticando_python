# digite_a_hora = float(input('Digite a hora atual (formato 24 hora): '))

# if digite_a_hora < 8 or digite_a_hora >= 18:
#     print('Acesso Negado.')
# else:
#     print('Acesso Autorizado.')

hora_atual = int(input("Digite a hora atual (formato 24 horas): "))

if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")
