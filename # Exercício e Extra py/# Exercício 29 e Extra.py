# Exercício 29 e Extra
def exercicio_29():
    num = int(input("Digite um número: "))
    if num > 10:
        print(f"{num} é maior que 10.")
    
    divisores = [x for x in range(1, num + 1) if num % x == 0]
    print(f"Divisores de {num}: {divisores}")
