

class University (object):
    def __init__(self):
        super().__init__(object)
        self.name = 'Universidade'
        self.departments = [object]



    def update_departments(self,department):
        self.departments.append(department)
        return self

    def show_departments(self):
        print(f"Departamentos: {self.departments}")