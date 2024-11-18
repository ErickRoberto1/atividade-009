from university import University
from departament import Department
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
    uni = University("-- Universidade --")

    department = [Department(name) for name in departments]
    professor = [Professor(name) for name in professors]
    sub = [Subject(name) for name in subs]

    #adcionar um professor a cada departamento
    for dep,prof in zip(department,professor):
        uni.add_new_department(dep)
        dep.add_new_professor(prof)

    #adicionar uma materia a cada professor
    for prof,sub in zip(professor,sub):
        prof.add_subject(sub)

    #lista de departamentos com os professores
    for dep in department:
        print(dep.list_professors())
    print('\n')

    #universidade sem remoções
    print(f'objeto Universidade sem as remoções: {uni}')

    #removendo departamentos da universidade
    print(f'Removendo departamentos da Universidade: Eng de Software')
    print('Antes:')
    print(uni.list_departments())
    department_to_be_removed = 'Departamento de Engenharia de Software'
    uni.remove_department(department_to_be_removed)
    print('Depois:')
    print(uni.list_departments())
    print('\n')

    #removendo disciplinas dos professores
    print(f'Removendo disciplinas de Professores: Cálculo I')
    print('Antes:')
    for prof in professor:
        print(f'{prof.name}: {prof.list_subjects()}')
    sub_to_be_removed = 'Cálculo I'
    for prof in professor:
        prof.remove_subject(sub_to_be_removed)
    print('Depois:')
    for prof in professor:
        print(f'{prof.name}: {prof.list_subjects()}')

    print('\n Imprimindo objetos diretamente: ')
    print(professor[1])
    print('Imprimindo objeto removido: ')
    print(professor[3])
    print('\n')
    print('Removendo professor de departamento:Professor4 ')
    print('Antes:')
    for dep in department:
        print(dep.list_professors())

    prof_to_be_removed = 'Professor4'
    for dep in department:
        dep.remove_professor(prof_to_be_removed)
    print('Depois:')
    for dep in department:
        print(dep.list_professors())

    # universidade com remoções
    print(f'objeto Universidade com as remoções: {uni}')

    # apagando o objeto
    del uni

    #tentando imprimir departamentos a partir de uma universidade
    try:
        print(uni.list_departments())
    except NameError:
        print('\nDepartamentos não existe!')

    #objetos professores ainda existem
    print('\nObjetos Professor ainda existe!')
    print(professor)















if __name__ == '__main__':
    main()



