from university import University
from departament import Departament
from professor import Professor
from subject import Subject

#professors names
professors = ["Professor1", "Professor2", "Professor3","Professor4","Professor5","Professor6"]

#departments
departments = ["Departamento de Matemática Aplicada", "Departamento de Engenharia de Software",
               "Departamento de Física","Departamento de Química"]

#classes(subjects)
subs = ["Matemática Discreta", "Álgebra Linear I","Álgebra Linear II", "Cálculo I","Cálculo Numérico"]


def main():
    global professors, departments,sub
    uni = University("Universidade")

    department = [Departament(name) for name in departments]
    professor = [Professor(name) for name in professors]
    sub = [Subject(name,professor) for name in subs]

    for dep,prof in zip(department,professor):
        uni.add_new_department(dep)
        dep.add_new_professor(prof)

    print(f'Departamentos: \n')
    print(uni.list_departments())
    print('\n')
    for dep in department:
        print(dep.list_professors())

    for prof in professor:
        print(prof.list_subjects())







if __name__ == '__main__':
    main()



