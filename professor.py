

class Professor:
    def __init__(self, name):
        self.name = name
        self.disciplinas = []


    def set_name (self, name):
        self.name = name
    def add_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        return
    def get_disciplinas(self):
        return self.disciplinas
