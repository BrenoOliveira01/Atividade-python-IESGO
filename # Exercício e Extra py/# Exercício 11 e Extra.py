# Exercício 11 e Extra
def exercicio_11():
    numeros = list(map(int, input("Digite números separados por vírgula: ").split(',')))
    print(f"Números em ordem crescente: {sorted(numeros)}")
    
    repetidos = {num for num in numeros if numeros.count(num) > 1}
    if repetidos:
        print(f"Números repetidos: {repetidos}")
