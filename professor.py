

class Professor:
    def __init__(self, name):
        self.name = name
        self.subjects = []


    def set_name (self, name):
        self.name = name
    def add_subject(self, disciplina):
        self.subjects.append(disciplina)
        return
    def get_subject(self):
        return self.subjects


    def show(self):
        print(f"Professor: {self.name}"
              f"Disciplinas: {self.subjects}")
