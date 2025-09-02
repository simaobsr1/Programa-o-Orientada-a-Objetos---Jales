class CalculadoraGeometrica:
    def calcular_area_quadrado(self,lado):
        return lado * lado 

    def calcular_area_circulo (self,raio):
        pi = 3.1415
        return pi * (raio * raio )

calculo = CalculadoraGeometrica()

print ("area do quadrado",calculo.calcular_area_quadrado(5))
print ("area do circulo",calculo.calcular_area_circulo(2))