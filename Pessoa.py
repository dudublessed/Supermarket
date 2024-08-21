from Carrinho import Carrinho

class Pessoa:
    def __init__(self, name, age, bank, money, carrinho):
        self.name = name
        self.age = age
        self.bank = bank
        self.money = money
        self.carrinho = carrinho
        
    def __str__(self):
        return f"Nome: {self.name}, Idade: {self.age}, Banco: {self.bank} Dinheiro: {self.money}"
    
    
    def pay_cart(self):
        valor_carrinho = self.carrinho.mostrar_valor_carrinho()
        
        while True:
            if self.money >= valor_carrinho:
                self.money -= valor_carrinho
                print(f"Pagamento efetuado com sucesso! Saldo restante: R$ {self.money:.2f}")
                break
            else:
                print(f"Dinheiro insuficiente para realizar a transação.")
                self.carrinho.mostrar_carrinho()
                self.carrinho.remover_produto()