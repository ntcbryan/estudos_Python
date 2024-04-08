class bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        #Atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    #Métodos (funções dentro de uma classe)
    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("parando bike...")
        print("bike parada!")

    def correr(self):
        print("vrummm...!")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")       
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada")  
            else:
                print("Não foi possivel trocar de marcha...")


    #Método para pegar as infos de forma rapida
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

b1 = bicicleta("Vermelha", "Caloi", 2022, 600)
b2 = bicicleta("verde", "monark", 2000, 189)

