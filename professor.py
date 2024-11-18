from subject import Subject

class Professor:
    def __init__(self, name):
        self.name = name
        self.subjects = []
        self.department = None


    def __str__(self):
        return f'{self.name}, Disciplinas: {self.subjects}'

    def add_subject(self, subject:Subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            subject.professor.append(self)

    def remove_subject(self, sub_name):
        for subject in self.subjects:
            if sub_name == subject.name:
                index = self.get_index(sub_name)
                self.subjects.remove(self.subjects[index])

    def list_subjects(self):
        return [sub.name for sub in self.subjects]

    def get_index(self, sub):
        for i in range(len(self.subjects)):
            if self.subjects[i].name == sub:
                return i


