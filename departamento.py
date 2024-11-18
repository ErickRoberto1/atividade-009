from professor import Professor


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def __str__(self):
        return f'Departamento: {self.nome}, Professores: {self.professores}'

    def adicionar_professor(self, professor_nome):
        new_professor = Departamento.criar_professor(self,professor_nome)
        self.professores.append(new_professor)
        return self.professores

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)

    def listar_professores(self):
        print("Lista de Professores: \n")
        for professor in self.professores:
            print(f'-{professor.nome}')

    def criar_professor(self, nome):
        return Professor(nome)

departamento = Departamento('<NAME>')
for i in range(5):
    professor = input("Nome do professor: ")
    Departamento.adicionar_professor(departamento,professor)

departamento.listar_professores()