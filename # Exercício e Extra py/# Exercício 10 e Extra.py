# Exercício 10 e Extra
def exercicio_10():
    valor = float(input("Digite o valor do produto: "))
    desconto = valor * 0.10
    print(f"Valor com desconto de 10%: {valor - desconto}")
    
    percentual = float(input("Digite o percentual de desconto: ")) / 100
    desconto = valor * percentual
    print(f"Valor com desconto de {percentual * 100}%: {valor - desconto}")
