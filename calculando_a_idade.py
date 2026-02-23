# def calcular_idade():
#     ano_nacimento = int(input('Digite o ano de nacimento: '))
#     ano_atual = int(input('Digite o ano atual: '))

#     total = ano_atual - ano_nacimento

#     print(f'A idade é {total} ano')

# calcular_idade()


def calcular_idade(ano_nascimento, ano_atual): 
    return ano_atual - ano_nascimento 
 
nascimento = int(input("Digite o ano de nascimento: ")) 
atual = int(input("Digite o ano atual: ")) 
idade = calcular_idade(nascimento, atual) 
print(f"A idade é {idade} anos.") 
