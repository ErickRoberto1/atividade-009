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

    def remove_professor(self, professor_name):
        for professor in self.professors:
            if professor.name == professor_name:
                index = self.get_index(professor_name)
                self.professors.remove(self.professors[index])


    def list_professors(self):
        print(f"Lista de Professores do Departamento {self.name}: ")
        return [prof.name for prof in self.professors]

    def get_index(self,professor_name):
        for i in range(len(self.professors)):
            if self.professors[i].name == professor_name:
                return i
