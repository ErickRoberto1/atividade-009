from departamento import Department
from professor import Professor

class University :
    def __init__(self):
        self.name = 'Universidade'
        self.departments = []



    def update_departments(self,department):
        if department not in self.departments:
         self.departments.append(department)


    def show_departments(self):
        print(f"Departamentos: {self.departments}")
