

class Subject:
    def __init__(self):
        self.subject = None

    def set_subject(self, subject):
        if self.subject is None:
            self.subject = subject

    def get_subject(self):
        return self.subject

    def kill_subject(self):
        self.subject = None
