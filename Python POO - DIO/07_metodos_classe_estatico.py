#Somos acostumados a fazer dessa forma:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Guilherme", 28)


# Com métodos de classe vamos fazer da seguinte forma:
class Pessoa:
    def __init__(self, nome = None ,idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod #Alem de usar o @classmethod, por convensão n vamos usar self e sim o CLS
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
    #e para criar um método estatico
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
p2 = Pessoa().criar_apartir_data_nascimento(1994, 3,21, "Guilherme")
print(p2.nome, p2.idade)


print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(9))