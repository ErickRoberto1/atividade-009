

class Department:
    def __init__(self):
        self.name = None
        self.subjects = []
        self.professor_list = []

    def add_professor(self,professor):
        if professor not in self.professor_list:
            self.professor_list.append(professor)

    def remove_professor(self,professor):
        if professor in self.professor_list:
            self.professor_list.remove(professor)


    def set_name(self, name):
        if self.name is None:
            self.name = name

    def get_name(self):
        return self.name

    def show (self):
        print(f"Department :{self.name}"
              f"Disciplinas: {self.subjects}"
              f"Professores: {self.professor_list}")
