

class Subject:
    def __init__(self,professor):
        self.subject = None
        self.subject_professor = professor


    def set_subject(self, subject):
        if self.subject is None:
            self.subject = subject

    def get_professor(self):
        return self.subject_professor

