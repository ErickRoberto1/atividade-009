from universidade import University
from professor import Professor
from departamento import Department
from disciplina import Subject

university = University()
running = True
while running:
    answer = input("1 para atualizar departamentos - \n")

    if answer == "1":
        departamento = input("Departamento: ")
        departamento = Department()
        university.update_departments(departamento)
        running = False
        break

