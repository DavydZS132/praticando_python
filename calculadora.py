soma = lambda x, y: x + y

subtrai = lambda x, y: x - y

multiplicacao = lambda x, y: x * y

divisao = lambda x, y: x / y if y != 0 else 'Erro: Divisão por zero'

x = float(input("Digite o primeiro número: ")) 

y = float(input("Digite o segundo número: ")) 

operacao = input("Escolha a operação (| + | - | * | / |): ")

operacoes = { 

    '+': soma,  

   '-': subtrai, 

    '*': multiplicacao, 

    '/': divisao 

} 

if operacao in operacoes:  

   resultado = operacoes[operacao](x, y)  

   print(f"O resultado é: {resultado}")  

else:  

   print("Operação inválida") 
