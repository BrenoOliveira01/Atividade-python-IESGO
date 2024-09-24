# Exercício 28 e Extra
def exercicio_28():
    for i in range(1, 6):
        print(i)
    
    extra = input("Quer ver até 1000? (sim/não): ")
    if extra.lower() == "sim":
        for i in range(1, 1001):
            print(i)
