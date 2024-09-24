# Exercício 6 e Extra
def exercicio_6():
    nums = [int(input(f"Digite o número {i+1}: ")) for i in range(3)]
    media = sum(nums) / 3
    print(f"Média: {media}")
    
    if any(num > 100 for num in nums):
        print("Algum número é maior que 100.")
