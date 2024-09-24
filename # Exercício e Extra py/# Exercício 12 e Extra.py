# Exercício 12 e Extra
import datetime

def exercicio_12():
    data = input("Digite uma data no formato DD/MM/AAAA: ")
    try:
        dia, mes, ano = map(int, data.split('/'))
        data_valida = datetime.datetime(ano, mes, dia)
        print(f"Data válida: {data_valida}")
        
        dias_passados = (datetime.datetime.now() - data_valida).days
        print(f"Dias passados desde {data}: {dias_passados}")
    except ValueError:
        print("Data inválida.")
