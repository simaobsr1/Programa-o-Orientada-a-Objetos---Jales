class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []  

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco
        return total

produto1 = Produto("Camiseta", 50)
produto2 = Produto("Calça Jeans", 120)
produto3 = Produto("Tênis", 250)

pedido = Pedido("Simão")
pedido.adicionar_item(produto1)
pedido.adicionar_item(produto2)
pedido.adicionar_item(produto3)

print("Cliente:", pedido.cliente)
print("Total do pedido:", pedido.calcular_total())
