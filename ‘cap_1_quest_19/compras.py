class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {} 

    def adicionar_produto(self, produto, quantidade):
        if quantidade > produto.estoque:
            print(f"Erro: Estoque insuficiente para {produto.nome}. Disponível: {produto.estoque}")
            return 
        
        self.itens[produto] = self.itens.get(produto, 0) + quantidade
        produto.estoque -= quantidade
        print(f"{quantidade}x {produto.nome} adicionado(s) ao carrinho.")

    def finalizar_compra(self):
        return sum(produto.preco * quantidade for produto, quantidade in self.itens.items())

produto1 = Produto("Camiseta", 50, 10)
produto2 = Produto("Calça Jeans", 120, 5)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(produto1, 3)
carrinho.adicionar_produto(produto2, 2)
carrinho.adicionar_produto(produto2, 5)  

print("Total da compra:", carrinho.finalizar_compra())
