from subject import Subject

class Professor:
    def __init__(self, name):
        self.name = name
        self.subjects = []


    def __str__(self):
        return f'{self.name}, Disciplinas {self.subjects}'

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            subject.professor = self

    def remove_subject(self, subject_name):
        for subject in self.subjects:
            if subject.name == subject_name:
                index = self.get_index(self.subjects,subject_name)
                del self.subjects[index]



    def list_subjects(self):
        return [sub.name for sub in self.subjects]

    def get_index(self, subject_list,subject):
        for i in range(len(self.subjects)):
            if subject_list[i].name == subject:
                return i