# Exercício 16 e Extra
def exercicio_16():
    dias = int(input("Digite a quantidade de dias trabalhados: "))
    valor_diario = float(input("Digite o valor diário: "))
    
    salario = dias * valor_diario
    print(f"Salário sem desconto: R$ {salario}")
    
    imposto = salario * 0.05
    print(f"Salário com desconto de imposto: R$ {salario - imposto}")