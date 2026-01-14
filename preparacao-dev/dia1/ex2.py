# Exercício A (Manipulação de String): Crie uma função que receba uma frase e retorne a mesma frase, mas com a ordem das palavras invertida (Ex: "Eu amo Python" vira "Python amo Eu"). Dica: split e join

def invertexto(frase: str):
    
    palavras = frase.split()
    
    palavras.reverse()

    frase_invertida = " ".join(palavras)

    return print(frase_invertida)

invertexto(frase="amo python teste")

