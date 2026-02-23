while True:
    nome_usuario = ('Digite seu nome do usuario: ')
    senha_usuario = ('Digite sua senha: ')

    if len(nome_usuario) < 5:
        print('O nome do usuario precisa ter pelo menos 5 caracteristicas.')
        continue
    
    if len(senha_usuario) < 8:
        print('A senha precisa ter pelo menos 8 caracteristicas.')
        continue
    
    print("Cadastro realizado com sucesso!")
    break