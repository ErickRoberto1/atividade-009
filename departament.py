from professor import Professor

class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def __str__(self):
        return f'{self.name}'

    def add_new_professor(self, professor:Professor):
        if professor not in self.professors:
            self.professors.append(professor)

    def remove_professor(self, professor:Professor):
        if professor in self.professors:
            self.professors.remove(professor)

    def list_professors(self):
        print(f"Lista de Professores do Departamento {self.name}: ")
        return [prof.name for prof in self.professors]


