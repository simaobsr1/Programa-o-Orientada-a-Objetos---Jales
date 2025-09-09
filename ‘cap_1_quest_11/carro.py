class Carro:
    def __init__(self):
        self.velocidade = 0 

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0

meu_carro = Carro()
print("Velocidade inicial:", meu_carro.velocidade)

meu_carro.acelerar(50)
print("Depois de acelerar:", meu_carro.velocidade)

meu_carro.frear(20)
print("Depois de frear:", meu_carro.velocidade)

meu_carro.frear(40)
print("Depois de frear mais:", meu_carro.velocidade) 
