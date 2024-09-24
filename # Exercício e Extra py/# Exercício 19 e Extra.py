# Exercício 19 e Extra
def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Divisão por zero não permitida."
        return num1 / num2
    else:
        return "Operação inválida."

def exercicio_19():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    print(f"Resultado: {calcular(num1, num2, operacao)}")
