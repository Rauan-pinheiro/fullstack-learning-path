#salvar dados da classe em um arquivo json
import json

CAMINHO_ARQUIVO = 'dadosPOO.json'

class Pessoa:
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa('Rauan', 18)
p2 = Pessoa('pedro', 16)
p3 = Pessoa('jeovana', 17)

dados = [vars(p1),vars(p2),vars(p3)]

with open(CAMINHO_ARQUIVO, 'w',) as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    
