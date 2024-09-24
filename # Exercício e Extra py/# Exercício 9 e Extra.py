# Exercício 9 e Extra
def exercicio_9():
    idades = []
    while True:
        idade = int(input("Digite a idade (ou negativo para parar): "))
        if idade < 0:
            break
        idades.append(idade)
    
    if idades:
        print(f"Média das idades: {sum(idades) / len(idades)}")
        print(f"Maior idade: {max(idades)}")
