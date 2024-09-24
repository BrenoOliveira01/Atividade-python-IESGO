# Exercício 14 e Extra
import random

def exercicio_14():
    numero = random.randint(1, 10)
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    
    if palpite == numero:
        print("Você acertou!")
    else:
        print(f"Você errou. O número era {numero}.")
        if palpite > numero:
            print("Seu palpite foi maior.")
        else:
            print("Seu palpite foi menor.")