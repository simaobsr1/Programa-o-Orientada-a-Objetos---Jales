class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar_oponente(self, alvo):
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

heroi = Personagem("Kratos", 100, 20)
monstro = Personagem("Zeus", 50, 10)

print("Vida inicial do monstro:", monstro.vida)

heroi.atacar_oponente(monstro)
print("Vida do monstro após ataque:", monstro.vida)

monstro.atacar_oponente(heroi)
print("Vida do herói após ataque:", heroi.vida)
