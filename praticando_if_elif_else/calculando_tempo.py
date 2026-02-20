atividade_a = int(input('Informe os dias para a atividade A: '))
atividade_b = int(input('Informe os dias para a atividade B: '))
atividade_c = int(input('Informe os dias para a atividade C: '))

total = atividade_a + atividade_b + atividade_c

if atividade_a <= 0:
    print('Não pode ser Numero negativo Atividade A.')
elif atividade_b <= 0:
    print('Não pode ser Numero negativo Atividade B.')
elif atividade_c <= 0:
    print('Não pode ser Numero negativo Atividade C.')
else:
    print(f'O tempo da atividade A é {atividade_a} o tempo da atividade B é {atividade_b} e o tempo da atividade C é {atividade_c} o total de tempo é {total}')

atividade_A = int(input("Informe os dias para a atividade A: "))
atividade_B = int(input("Informe os dias para a atividade B: "))
atividade_C = int(input("Informe os dias para a atividade C: "))

if (atividade_A >= 0 and atividade_B >= 0 and atividade_C >= 0):
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"O tempo total do projeto é de {tempo_total} dias.")
else: 
    print("Erro: Os dias não podem ser negativos.")
