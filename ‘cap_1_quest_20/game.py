class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar_oponente(self, alvo):
        alvo.receber_dano(self.ataque)
        print(f"{self.nome} ataca {alvo.nome} Vida de {alvo.nome} agora é {alvo.vida}.")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0

class Arena:
    def iniciar_batalha(self, personagem1, personagem2):
        rodada = 1
        print(f"A batalha entre {personagem1.nome} e {personagem2.nome} começa!\n")
        while personagem1.esta_vivo() and personagem2.esta_vivo():
            print(f"--- Rodada {rodada} ---")
            personagem1.atacar_oponente(personagem2)
            if personagem2.esta_vivo():
                personagem2.atacar_oponente(personagem1)
            rodada += 1
            print()

        if personagem1.esta_vivo():
            print(f"{personagem1.nome} venceu a batalha!")
        else:
            print(f"{personagem2.nome} venceu a batalha!")

kratos = Personagem("Kratos", 120, 25)
zeus = Personagem("Zeus", 100, 30)

arena = Arena()
arena.iniciar_batalha(kratos, zeus)
