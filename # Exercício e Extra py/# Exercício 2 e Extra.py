# Exercício 2 e Extra
def exercicio_2():
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("Número é par.")
    else:
        print("Número é ímpar.")
    
    if num % 4 == 0:
        print("Número é múltiplo de 4.")
    
    num1 = int(input("Digite outro número: "))
    num2 = int(input("Digite mais um número: "))
    
    if num1 % num2 == 0:
        print(f"{num1} é divisível por {num2}.")
    else:
        print(f"{num1} não é divisível por {num2}.")
