from departament import Departament
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def __str__(self):
        return f'{self.name}'

    def add_new_department(self,department):
        if department not in self.departments:
            self.departments.append(department)
        else:
            print('Este departamento Já existe na Universidade!')

    def remove_department(self,department):
        if department in self.departments:
            print(f'Departamento {department} removido com sucesso!')
            index = self.get_index(department)
            del self.departments[index]

    def get_index(self,department):
        for i in range(len(self.departments)):
            if department == self.departments[i]:
                return i



    def list_departments(self):
        return [dep.name for dep in self.departments]

        
