# Exercício 18 e Extra
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def exercicio_18():
    celsius = float(input("Digite o valor em Celsius: "))
    print(f"{celsius} Celsius em Fahrenheit: {celsius_para_fahrenheit(celsius)}")
    
    fahrenheit = float(input("Digite o valor em Fahrenheit: "))
    print(f"{fahrenheit} Fahrenheit em Celsius: {fahrenheit_para_celsius(fahrenheit)}")
