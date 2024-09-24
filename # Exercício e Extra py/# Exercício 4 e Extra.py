# Exercício 4 e Extra
def saudacao(nome):
    return f"Olá, {nome}!"

def contagem_letras(nome):
    return len(nome)

def exercicio_4():
    nome = input("Digite seu nome: ")
    print(saudacao(nome))
    print(f"O nome tem {contagem_letras(nome)} letras.")
