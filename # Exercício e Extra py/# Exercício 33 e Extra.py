# Exercício 33
def exercicio_33():
    nums = [int(input(f"Digite o número {i+1}: ")) for i in range(3)]
    resultado = nums[0] * nums[1] * nums[2]
    print(f"Resultado da multiplicação: {resultado}")
