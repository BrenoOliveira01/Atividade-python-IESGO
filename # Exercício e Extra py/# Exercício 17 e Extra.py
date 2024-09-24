# Exercício 17 e Extra
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def exercicio_17():
    num = int(input("Digite um número: "))
    print(f"Fatorial de {num}: {fatorial(num)}")
