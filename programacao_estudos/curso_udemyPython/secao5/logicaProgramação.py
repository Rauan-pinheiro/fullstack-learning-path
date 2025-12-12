#desafio otávio miranda! UDEMY
import os

def limpar_terminal():
    os.system('cls')

def menu():
    print('Comandos: listar, desfazer, refazer, clear(limpar tela), sair')

tarefas = []
tarefas_refazer = []

while True:
    print()
    menu()
    
    escolha_comando_tarefa = input('Digite uma tarefa ou comando:').lower()
    
    if escolha_comando_tarefa == 'sair':
        print('Volte sempre!')
        break
    
    elif escolha_comando_tarefa == 'listar':
        
        if tarefas:
            print()
            print('TAREFAS:')
            for i,item in enumerate(tarefas, start= 1):
                print(f'{i}. {item}')
        else:
            print()
            print('Nenhuma tarefa no momento!')

    elif escolha_comando_tarefa == 'desfazer':
        # "APAGAR" o último item que foi adicionado na lista na ordem em que foi adicionado
        if tarefas:
            ultimo_item = tarefas.pop()
            tarefas_refazer.append(ultimo_item)
            print('Último item desfeito!')
        else:
            print('Não há o que desfazer!')
        
    elif escolha_comando_tarefa == 'refazer':
        # VOLTAR com o último item da lista que foi "apagado"
        if tarefas_refazer:
            refazer_tarefa = tarefas_refazer.pop()
            tarefas.append(refazer_tarefa)
            print('Último item restaurado!')
        else:
            print('Não há o que refazer!')

    elif escolha_comando_tarefa == 'clear':
        limpar_terminal()
        print('Terminal limpo com sucesso!\n')
    
    else:
        print()
        print('Tarefa salva com sucesso!')
        tarefas.append(escolha_comando_tarefa)
        tarefas_refazer.clear()
        