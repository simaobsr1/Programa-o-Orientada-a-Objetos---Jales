class Conversor_Simples:
    def real_para_dolar(self,valor):
        return valor / 5.25
    
    def dolar_para_real(self,valor):
        return  valor * 5.25
    
valorreal = Conversor_Simples ()

print (valorreal.real_para_dolar(10.5))
print (valorreal.dolar_para_real(10))