#Usuário escolhe se já possui cadastro ou não
def cadastro():
    cadastro = input("Você já possui cadastro? (S/N) ")

    while cadastro != "S" and cadastro != "N":
        cadastro = input("Escolha inválida. Por favor, digite 'S' se você já possui um cadastro ou 'N' se você não possui: ")

    return cadastro


#Se o usuário colocar "S", ele precisa colocar o email e a senha
def cadastro_sim():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    return [email, senha]

#Se o usuário colocar "N", ele precisa fazer um cadastro com email, senha, cep, cpf
def cadastro_nao():
    email = input("Digite seu email: ")
    senha = input("Digite a senha que você vai utilizar: ")
    cep = input("Digite o seu CEP: ")
    cpf = input("Digite o seu CPF: ")

    return [email, senha, cep, cpf]

#O usuário escolhe se ele vai ser um doador ou um donatário 
def escolher_tipo_usuario():
    tipo_usuario = int(input("Escolha se você deseja ser um doador ou um donatário ('1' para doador, '2' para donatário): "))

    while tipo_usuario != 1 and tipo_usuario != 2:
        tipo_usuario = int(input("Escolha inválida. Por favor, digite '1' para doador ou '2' para donatário: "))


    if tipo_usuario == 1:
        print("Você escolheu ser um doador, obrigado por nos ajudar!")
    elif tipo_usuario == 2:
        print("Você escolheu ser um donatário, ajudaremos você em breve!")

    return tipo_usuario

#Se o usuário escolher ser doador ele vai escolher se quer doar alimentos ou dinheiro
def doador():
    escolha = int(input("Você vai querer doar alimentos ou dinheiro? (1/2) "))
    while escolha != 1 and escolha != 2:
        escolha = int(input("Escolha inválida. Por favor, digite '1' para doar alimentos ou '2' para doar dinheiro: "))

    return escolha

#Usuário doar alimentos
def doacao_alimento():
    doar = input("Você escolheu doar alimentos. Você pode doar alimentos não perecíveis como: \nArroz, Macarrão, Feijão, Farinha de trigo, Açúcar, Sal.\nEntre outros alimentos. No seu email, uma mensagem será enviada para você saber como enviar.\nMuito obrigado por estar querendo ser um doador.")

    return doar

#Usuário doar dinheiro
def doacao_dinheiro():
    doar = float(input("Você escolheu doar dinheiro. Quanto você vai querer doar? "))

    return doar


#Se o usuário escolher ser donatário, ele vai ter que responder algumas perguntas para verificar se ele pode receber
def donatario():
    emprego = input("Você está trabalhando? (S/N) ")
    while emprego != "S" and emprego != "N":
        emprego = input("Digite apenas 'S' se você estiver trabalhando e 'N' se você não está trabalhando: ")

    familia = int(input("Digite quantas pessoas moram com você: "))

    renda = float(input("Digite sua renda mensal. Se não tiver renda, coloque '0': "))
    
    moradia = input("Você possui moradia? (S/N) ")
    while moradia != "S" and moradia != "N":
        moradia = input("Digite apenas 'S' se você tiver moradia e 'N' se você não tiver moradia: ")

    return [emprego, familia, renda, moradia]

#Se o usuário digitar "S" em "emprego", ele tem que falar qual o tipo de trabalho dele
def empregado():
    tipo_trabalho = input("Como é o seu trabalho hoje em dia? (autônomo, assalariado, temporário ...) ")
    print("Ok, obrigado pela sua resposta!")

    return tipo_trabalho

#Se o usuário digitar "S" em "moradia", ele tem que falar qual o tipo de moradia dele
def residencia():
    tipo_moradia = input("Como é a sua moradia hoje em dia? (alugada, própria ...) ")
    print("Ok, obrigado pela sua resposta!")

    return tipo_moradia

#Se o usuário for apto a receber a doação, ele vem para esta função
def pode_receber():
    print("Você é apto a receber doações")

#Se o usuário não for apto a receber a doação, ele vem para esta função
def nao_receber():
    print("Desculpe, mas você não é apto a receber doações")

#Sistema principal
tem_cadastro = cadastro()
if tem_cadastro == "S":
    dados_cadastro = cadastro_sim()
elif tem_cadastro == "N":
    dados_cadastro = cadastro_nao()

tipo_usuario = escolher_tipo_usuario()

if tipo_usuario == 1:
    escolha = doador()
    if escolha == 1:
        doacao_alimento()
    elif escolha == 2:
        doacao_dinheiro()
elif tipo_usuario == 2:
    dados_donatario = donatario()

    empregabilidade = dados_donatario[0]
    if empregabilidade == "S":
        empregado()

    moradias = dados_donatario[3]
    if moradias == "S":
        residencia()

    renda_mensal = dados_donatario[2]
    if renda_mensal <= 1500:
        pode_receber()
    elif renda_mensal > 1500:
        nao_receber()
