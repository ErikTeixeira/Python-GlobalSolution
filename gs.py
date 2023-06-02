#Usuário escolhe se já possui cadastro ou não
def cadastro():
    cadastro = input("Você já possui cadastro? (S/N) ")

    return cadastro


#Se o usuário colocar "S", ele precisa colocar o email e a senha
def cadastro_sim(cadastro):
    if cadastro == "S":
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

    return email,senha


cadastro_sim(cadastro())