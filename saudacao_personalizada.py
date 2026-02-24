# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:
#     Se for antes das 12h, exibir "Bom dia";
#     Entre 12h e 18h, exibir "Boa tarde";
#     Após 18h, exibir "Boa noite".
# Exemplo de entrada:
# Digite a hora atual (0-23): 15 
# Saída esperada:
# Boa tarde! 

# def saudacao_personalizada(horas):
#     if horas < 12:
#         print('Bom dia.')
#     elif 12 <= horas < 18:
#         print('Boa tarde.')
#     else:
#         print('Boa noite.')

# horas_digitadas = int(input('Digite a hora atual (0-23): '))

# saudacao_personalizada(horas_digitadas)


def saudacao(hora): 
    if hora < 12: 
        return "Bom dia!" 
    elif hora < 18: 
        return "Boa tarde!" 
    else: 
        return "Boa noite!" 
 
hora_atual = int(input("Digite a hora atual (0-23): ")) 
print(saudacao(hora_atual)) 
