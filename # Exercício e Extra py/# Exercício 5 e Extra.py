# Exercício 5 e Extra
def exercicio_5():
    palavra = input("Digite uma palavra: ")
    if palavra == palavra[::-1]:
        print(f"{palavra} é um palíndromo.")
    else:
        print(f"{palavra} não é um palíndromo.")
    
    extra_palavra = palavra.replace(" ", "").lower()
    if extra_palavra == extra_palavra[::-1]:
        print(f"Ignorando espaços e maiúsculas, {palavra} é um palíndromo.")