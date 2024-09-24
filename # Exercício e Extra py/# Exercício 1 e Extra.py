# Exercício 1 e Extra
def exercicio_1():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    ano_atual = 2024
    ano_100 = ano_atual + (100 - idade)
    print(f"{nome}, você completará 100 anos em {ano_100}.")

    extra = input("Digite outro número: ")
    print((f"{nome}, você completará 100 anos em {ano_100}.\n") * int(extra))
