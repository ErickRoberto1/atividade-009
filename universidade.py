class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def remover_departamento(self, departamento):
        if departamento in self.departamentos:
            self.departamentos.remove(departamento)

    def listar_departamentos(self):
        return [dep.nome for dep in self.departamentos]
