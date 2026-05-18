
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self, desconto_percentual=0):
        """Calcula o total do carrinho aplicando um desconto opcional."""

        if not (0 <= desconto_percentual <= 100):
            raise ValueError("Desconto deve estar entre 0 e 100")

        total = sum(produto.preco for produto in self.produtos)
        valor_desconto = total * (desconto_percentual / 100)

        return total - valor_desconto