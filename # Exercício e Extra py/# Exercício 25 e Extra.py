# Exercício 25 e Extra
def exercicio_25():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"Soma: {soma}")
    
    if soma.is_integer():
        print("O resultado é inteiro.")
    else:
        print("O resultado é racional.")
