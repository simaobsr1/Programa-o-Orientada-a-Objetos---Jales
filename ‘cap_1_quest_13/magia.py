import math  

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio

circulo1 = Circulo(5)

print("Raio:", circulo1.raio)
print("Área:", circulo1.calcular_area())
print("Circunferência:", circulo1.calcular_circunferencia())
