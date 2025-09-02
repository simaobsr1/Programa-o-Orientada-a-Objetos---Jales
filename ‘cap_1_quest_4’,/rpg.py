import random

class Rolo_de_Dados:
    def D6 (self):
      return random.randint (1,6)

    def D12 (self):
      return random.randint (1,12)
   
    def D20 (self): 
       return random.randint(1,220)
    
rolar = Rolo_de_Dados ()

print( rolar.D6 ())
print(rolar.D12 ())
print(rolar.D20())