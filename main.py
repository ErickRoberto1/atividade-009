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
    return input('Comando: ').strip()
    
def comandos_departamento():
    print('''\n--- Menu Departamento ---
1 - Adicionar professor
2 - Remover professor
3 - Listar professores
4 - Voltar
0 - Fechar programa''')
    return input('Comando: ').strip()

def comandos_professor():
    print('''\n--- Menu Professor ---
1 - Adicionar disciplina
2 - Remover disciplina
3 - Listar disciplinas
4 - Voltar
0 - Fechar programa''')
    return input('Comando: ').strip()

universidade = Universidade('UEA')

running = True
nivel = 0 

while running:
    #system('cls')

    if nivel == 0:
        comando = comandos_universidade()
        if comando == '0':
            running = False
        elif comando in ['1', '2', '3']:
            if comando == '1':
                universidade.adicionar_departamento()
            if comando == '2':
                universidade.remover_departamento()
            if comando == '3':
                universidade.listar_departamentos()
            nivel += 1 
    
    elif nivel == 1:
        comando = comandos_departamento()
        if comando == '0':
            running = False
        elif comando == '4':
            nivel -= 1
        elif comando in ['1', '2', '3']:
            nivel += 1 
    
    elif nivel == 2:
        comando = comandos_professor()
        if comando == '0':
            running = False
        elif comando == '4':
            nivel -= 1 
        elif comando in ['1', '2', '3']:
            print('comando escolhido')

system('cls')
print('Programa encerrado')  