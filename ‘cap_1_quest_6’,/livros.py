class Livro:
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo 
        self.autor = autor
        self.ano_publicacao = ano_publicacao

livro1 = Livro ("Pai Rico, Pai Pobre", "Robert T. Kiyosaki", 1997)

print("Titulo:", livro1.titulo)
print("Autor:", livro1.autor)
print("Ano da Publicação:",livro1.ano_publicacao )