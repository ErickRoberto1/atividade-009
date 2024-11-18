class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionar_departamento(self):
        if len(self.departamentos) < 5:
            nome_departamento = input('Nome do departamento: ')
            if nome_departamento not in self.departamentos:
                self.departamentos.append(nome_departamento)
                print('Departamento adicionado com sucesso')
            else:
                print('Departamento já foi adicionado')
        else:
            print('Departamento está cheio')

    def remover_departamento(self):
        nome_departamento = input('Nome do departamento: ')
        if nome_departamento in self.departamentos:
            self.departamentos.remove(nome_departamento)
        else: 
            print('Departamento inválido')

    def listar_departamentos(self):
        print(self.departamentos)
