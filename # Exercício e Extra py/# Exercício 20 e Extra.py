# Exercício 20 e Extra
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def exercicio_20():
    num = int(input("Digite um número: "))
    print(f"Sequência de Fibonacci até {num}: {fibonacci(num)}")
