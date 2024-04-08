class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    # Oque é definido nessa clase, esta apenas no escobo filho 
    def __init__(self,cor,placa,numero_rodas, carregado):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.esta_carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.esta_carregado else 'Não'} estou carregado")


# moto1 = Motocicleta("Preta", "AZT-1212", 2)
# moto1.ligar_motor()

caminhao1 = Caminhao("Roxo", "ABT-1234", 6, True)
print(caminhao1.cor)