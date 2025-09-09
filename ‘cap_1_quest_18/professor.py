class Disciplina:
    def __init__(self, nome):
        self.nome = nome

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas_lecionadas = []  

    def lecionar_disciplina(self, disciplina):
        self.disciplinas_lecionadas.append(disciplina)

disc1 = Disciplina("Matemática")
disc2 = Disciplina("Física")
disc3 = Disciplina("Programação Orientada  a Objetos")

prof = Professor(" Jales Monteiro")
prof.lecionar_disciplina(disc3)


print(f"Professor: {prof.nome}")
print("Disciplinas lecionadas:")
for d in prof.disciplinas_lecionadas:
    print("-", d.nome)
