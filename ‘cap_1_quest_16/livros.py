class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Livraria:
    def __init__(self):
        self.catalogo = {}  

    def adicionar_livro(self, livro):
        self.catalogo[livro.titulo] = livro

    def buscar_livro(self, titulo):
        return self.catalogo.get(titulo, None) 

livro1 = Livro("O Poder do Hábito", "Charles Duhigg")
livro2 = Livro("Como Fazer Amigos e Influenciar Pessoas", "Dale Carnegie")
livro3 = Livro("Mindset: A Nova Psicologia do Sucesso", "Carol S. Dweck")

livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)
livraria.adicionar_livro(livro3)

buscado = livraria.buscar_livro("O Poder do Hábito")
if buscado:
    print("Livro encontrado:")
    print("Título:", buscado.titulo)
    print("Autor:", buscado.autor)
else:
    print("Livro não encontrado.")
