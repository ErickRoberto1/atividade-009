from universidade import Universidade
from departamento import Departamento
from professor import Professor
from disciplina import Disciplina
from os import system

def comandos_universidade():
    print('''\n--- Menu Universidade ---
1 - Adicionar departamento
2 - Remover departamento
3 - Listar departamentos
0 - Fechar programa''')
    
def comandos_departamento():
    print('''\n--- Menu Departamento ---
1 - Adicionar professor
2 - Remover professor
3 - Listar professores
4 - Voltar
0 - Fechar programa''')

def comandos_professor():
    print('''\n--- Menu Professor ---
1 - Adicionar disciplina
2 - Remover disciplina
3 - Listar disciplinas
4 - Voltar
0 - Fechar programa''')


running = True
nivel = 0 

while running:
    system('cls')

    if nivel == 0:
        comandos_universidade()
        comando = input('Comando: ')
        if comando == '0':
            running = False
        elif comando in ['1', '2', '3']:
            print('comando escolhido')
            nivel += 1 
    
    elif nivel == 1:
        comandos_departamento()
        comando = input('Comando: ')
        if comando == '0':
            running = False
        elif comando == '4':
            nivel -= 1
        elif comando in ['1', '2', '3']:
            print('comando escolhido')
            nivel += 1 
    
    elif nivel == 2:
        comandos_professor()
        comando = input('Comando: ')
        if comando == '0':
            running = False
        elif comando == '4':
            nivel -= 1 
        elif comando in ['1', '2', '3']:
            print('comando escolhido')

system('cls')
print('Programa encerrado')  