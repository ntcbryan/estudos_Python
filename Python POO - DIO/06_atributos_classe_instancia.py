class Estudante:
    escola = 'DIO'
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno_1 = Estudante("Bryan", 123)
aluno_2 = Estudante("Giovanna", 233)
print(aluno_1, aluno_2)