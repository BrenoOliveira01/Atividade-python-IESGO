# Exercício 7 e Extra
def numeros_pares(lista):
    return [x for x in lista if x % 2 == 0]

def soma_pares(lista):
    return sum(numeros_pares(lista))

def exercicio_7():
    lista = list(map(int, input("Digite números separados por espaço: ").split()))
    print(f"Números pares: {numeros_pares(lista)}")
    print(f"Soma dos pares: {soma_pares(lista)}")