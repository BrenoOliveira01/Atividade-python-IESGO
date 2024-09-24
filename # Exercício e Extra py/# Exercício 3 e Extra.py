# Exercício 3 e Extra
def exercicio_3():
    num = int(input("Digite um número: "))
    divisores = [x for x in range(1, num + 1) if num % x == 0]
    print(f"Divisores de {num}: {divisores}")
    
    if len(divisores) == 2:
        print(f"{num} é primo.")