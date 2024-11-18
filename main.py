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
subs = ["Matemática Discreta", "Álgebra Linear I","Álgebra Linear II", "Cálculo I","Cálculo Numérico","Linguagem de Programação"]


def main():
    global professors, departments,sub
    uni = University("Universidade")

    department = [Departament(name) for name in departments]
    professor = [Professor(name) for name in professors]
    sub = [Subject(name,professor) for name in subs]

    for dep,prof in zip(department,professor):
        uni.add_new_department(dep)
        dep.add_new_professor(prof)

    for prof,sub in zip(professor,sub):
        prof.add_subject(sub)

    for dep in department:
        print(dep.list_professors())
    print('\n')

    print('Removendo Disciplinas de Professores: Cálculo I')
    print('Antes:')
    for prof in professor:
        print(f'Professor: {prof.name}')
        print(f'Disciplinas: {prof.list_subjects()}')

    print('\n')

    sub_to_be_removed = 'Cálculo I'
    for prof in professor:
        prof.remove_subject(sub_to_be_removed)


    print('Depois:')
    for prof in professor:
        print(f'Professor: {prof.name}')
        print(f'Disciplinas: {prof.list_subjects()}')

    print('\n')

    print(f'Removendo departamentos da Universidade: Eng de Software')
    print('Antes:')
    print(uni.list_departments())
    department_to_be_removed = 'Departamento de Engenharia de Software'
    uni.remove_department(department_to_be_removed)
    print('Depois:')
    print(uni.list_departments())

    print('\n')











if __name__ == '__main__':
    main()



