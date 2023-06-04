#Usuário escolhe se já possui cadastro ou não
def cadastro():
    cadastro = input("Você já possui cadastro? (S/N) ")

    return cadastro


#Se o usuário colocar "S", ele precisa colocar o email e a senha
def cadastro_sim():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    return email,senha

#Se o usuário colocar "N", ele precisa fazer um cadastro com emal, senha, cep
    email = input("Digite seu email: ")
    senha = input("Digite a senha que você vai utilizar: ")
    cep =input("Digite o seu CEP")

    return email,senha,cep


resposta = cadastro()
if resposta == "S":
    cadastro_sim()
elif resposta == "N":
    cadastro_nao()