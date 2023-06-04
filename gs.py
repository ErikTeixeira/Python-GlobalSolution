#Usuário escolhe se já possui cadastro ou não
def cadastro():
    cadastro = input("Você já possui cadastro? (S/N) ")

    while cadastro != "S" and cadastro != "N":
        cadastro = input("Escolha inválida. Por favor, digite 'S' sé você já possui um cadastro ou 'N' sé você não possui: ")

    return cadastro


#Se o usuário colocar "S", ele precisa colocar o email e a senha
def cadastro_sim():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    return [email,senha]

#Se o usuário colocar "N", ele precisa fazer um cadastro com emal, senha, cep
def cadastro_nao():
    email = input("Digite seu email: ")
    senha = input("Digite a senha que você vai utilizar: ")
    cep =input("Digite o seu CEP: ")

    return [email,senha,cep]

#O usuário escolhe se ele vai ser um doador ou um donatário 
def escolher_tipo_usuario():
    tipo_usuario = int(input("Escolha se você deseja ser um doador ou um donatário ('1' para doador, '2' para donatário): "))

    while tipo_usuario != 1 and tipo_usuario != 2:
        tipo_usuario = int(input("Escolha inválida. Por favor, digite '1' para doador ou '2' para donatário: "))


    if tipo_usuario == 1:
        usuario = print("Você escolheu ser um doador, obrigado por nós ajudar!")
    elif tipo_usuario == 2:
        usuario = print("Você escolheu ser um donatário, ajudaremos você em breve!")

    return usuario


tem_cadastro = cadastro()
if tem_cadastro == "S":
    dados_cadastro = cadastro_sim()
elif tem_cadastro == "N":
    dados_cadastro = cadastro_nao()

escolher_tipo_usuario()