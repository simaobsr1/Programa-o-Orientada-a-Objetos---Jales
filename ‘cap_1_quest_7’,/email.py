class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

usuario1 = Usuario("Simão Freires", "simao.santos@email.com")

print("Nome:", usuario1.nome)
print("Email:", usuario1.email)