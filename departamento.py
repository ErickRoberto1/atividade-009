

class Department:
    def __init__(self):
        self.name = None
        self.subjects = []
        self.professor_list = []

    def add_subject(self, subject, professor):
        self.subjects.append(subject)
        self.professor_list.append(professor)
        return self
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
