usuarios = []
def cadastrar_usuario():
    email = input("Digite o e-mail: ").strip().lower()

    for usuario in usuarios:
        if usuario["email"] == email:
            print("Erro: Este e-mail já está cadastrado!")
            return

    senha = input("Digite a senha: ")
    novo_usuario = {"email": email, "senha": senha}
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def fazer_login():
    email = input("E-mail: ").strip().lower()
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print(f"Bem-vindo de volta! Login realizado com sucesso para: {email}")
            return True

def menu():
 while True:
  try:
     sistema = int(input("1. Adicionar usuário\n2. Entrar no Sistema\n3. Sair\n: "))
  except ValueError:
     print("Digite somente números")
  if sistema == 1:
    cadastrar_usuario()
  elif sistema == 2:
    fazer_login()
  elif sistema == 3:
    print("ADEUS!")
    break
  else:
    print("Digite uma das três opções.")

def registro():
   nome = input("Nome do produto: ")
   preco = input("Preço do produto")
   descricao = input("Descriçao do produto")
   


