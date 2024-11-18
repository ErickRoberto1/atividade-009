from professor import Professor

class Departament:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def __str__(self):
        return f'{self.name}'

    def add_new_professor(self, professor_name):
        if professor_name not in self.professors:
            self.professors.append(professor_name)

    def remove_professor(self, professor):
        if professor in self.professors:
            self.professors.remove(professor)
            index = self.professors.index(professor)
            del self.professors[index]

    def list_professors(self):
        print(f"Lista de Professores do Departamento {self.name}: ")
        return [prof.name for prof in self.professors]

    def get_index(self,professor_name):
        for i in range(len(self.professors)):
            if professor_name == self.professors[i].name:
                return i
