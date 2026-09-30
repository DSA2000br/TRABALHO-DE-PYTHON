import os
usuarios = []
def cadastrar_usuario():
    email = input("Digite o e-mail: ").strip().lower()

    for usuario in usuarios:
     if usuario["email"] == email:
      print("Erro: Este e-mail já está cadastrado!")
      return

    senha = input("Digite a senha: ")
    novo_usuario = {"email": email, "senha": senha, "produtos": []}
    usuarios.append(novo_usuario)
    _ = os.system("cls")
    print("Usuário cadastrado com sucesso!")
def fazer_login():
    email = input("E-mail: ").strip().lower()
    senha = input("Senha: ")
    _ = os.system("cls")
    for usuario in usuarios:
     if usuario["email"] == email and usuario["senha"] == senha:
      print(f"Bem-vindo de volta! Login realizado com sucesso para: {email}")
      return usuario

    print("E-mail ou senha incorretos ou não cadastrados.")
    return False          
def menu():
 while True:
  try:
     sistema = int(input("1. Adicionar usuário\n2. Entrar no Sistema\n3. Sair\n: "))
  except ValueError:
     print("Digite somente números")
  if sistema == 1:
    cadastrar_usuario()
  elif sistema == 2:
     login = fazer_login()
     if login != False:
       registro(login)
       break
  elif sistema == 3:
    _ = os.system("cls")
    print("ADEUS!")
    break
  else:
    print("Digite uma das três opções.")
def registro(usuario):
 while True:
    while True:
        nome = input("Nome do produto: ")
        if len(nome) >= 2:
         break
        print("Erro: O nome do produto deve ter no mínimo 2 letras.")
    preco = input("Preço do produto: ")
    while True:
            descricao = input("Descrição do produto: ")
            if len(descricao) >= 5:
                break
            print("Erro: A descrição deve ter no mínimo 5 caracteres.")

    produto = {"Nome": nome, "preço": preco, "descrição": descricao}

    usuario["produtos"].append(produto)
    novo = input("Deseja adicionar um novo produto? [S/N]\n").upper()
    if novo == "N":
        os.system("cls")
        print("Produtos do usuário:")
        print(usuario["produtos"])
        break

menu()
