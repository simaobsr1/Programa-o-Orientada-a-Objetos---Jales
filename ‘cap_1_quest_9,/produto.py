class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = float(preco) 
        self.estoque = int(estoque)

produto1 = Produto("Notebook", 4500.00, 110)

print("Nome:", produto1.nome)
print("Preço:", produto1.preco)
print("Estoque:", produto1.estoque)

