# Exercício B (Lógica de Dados): Dado uma lista de números [1, 2, 2, 3, 3, 3, 4], crie uma função que retorne o número mais frequente (neste caso, o 3).


def numero_mais_frequente(lista):
    contagem = {} # 1. Cria o dicionário vazio

    # 2. Percorre a lista para contar
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1 # Se já existe, soma 1
        else:
            contagem[numero] = 1  # Se não existe, começa com 1
    
    # Neste ponto, contagem seria: {1: 1, 2: 2, 3: 3, 4: 1}

    # 3. Agora precisamos descobrir qual chave tem o maior valor
    numero_vencedor = None
    maior_repeticao = 0

    for numero, qtd in contagem.items():
        if qtd > maior_repeticao:
            maior_repeticao = qtd
            numero_vencedor = numero
            
    return numero_vencedor

# Testando
lista_teste = [1, 2, 2, 3, 3, 3, 4]
resultado = numero_mais_frequente(lista_teste)
print(f"O número mais frequente é: {resultado}")