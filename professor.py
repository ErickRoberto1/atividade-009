class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def __str__(self):
        return f'Professor: {self.nome}'


    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)

    def listar_disciplinas(self):
        return [disc.nome for disc in self.disciplinas]

