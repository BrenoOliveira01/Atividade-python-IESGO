# Exercício 8 e Extra
def exercicio_8():
    frase = input("Digite uma frase: ")
    palavras = frase.split()
    print(f"Número de palavras: {len(palavras)}")
    
    palavras_longas = [p for p in palavras if len(p) > 5]
    print(f"Número de palavras com mais de 5 letras: {len(palavras_longas)}")
