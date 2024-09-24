# Exercício 15 e Extra
def validar_senha(senha):
    erros = []
    if len(senha) < 8:
        erros.append("Senha precisa ter pelo menos 8 caracteres.")
    if not any(c.isupper() for c in senha):
        erros.append("Senha precisa ter pelo menos uma letra maiúscula.")
    if not any(c.isdigit() for c in senha):
        erros.append("Senha precisa ter pelo menos um número.")
    
    return erros

def exercicio_15():
    senha = input("Digite uma senha: ")
    erros = validar_senha(senha)
    
    if erros:
        print("Erros na senha:")
        for erro in erros:
            print(erro)
    else:
        print("Senha válida!")