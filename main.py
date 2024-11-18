from university import University
from departament import Department
from professor import Professor
from subject import Subject

#professors names
professors = ["Professor1", "Professor2", "Professor3","Professor4","Professor5","Professor6"]

#departments
departments = ["Departamento de Matemática Aplicada", "Departamento de Engenharia de Software",
               "Departamento de Física","Departamento de Química","Departamento de Materiais"]

#classes(subjects)
subs = ["Matemática Discreta", "Álgebra Linear I","Álgebra Linear II", "Cálculo I","Cálculo Numérico","Linguagem de Programação"]


def main():
    global professors, departments,sub
    uni = University("-- Universidade --")

    #criar departamentos com metodo da universidade
    for dep in departments:
        uni.create_new_department(dep)

    print(uni)
    for dep in departments:
        uni.remove_department(dep)

    print(uni)
















if __name__ == '__main__':
    main()



