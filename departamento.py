class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)

    def listar_professores(self):
        for professor in self.professores:
            print(professor.nome)
