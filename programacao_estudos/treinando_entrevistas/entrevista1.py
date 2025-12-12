def verifica_duplicata(lista: list):
    len(lista) != len(set(lista))

print(verifica_duplicata([1,2,3,4,5,]))




def verificar(lista:list):
    if len(lista) != len(set(lista)):
        return True

    return False