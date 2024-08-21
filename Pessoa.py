

class Pessoa:
    def __init__(self, name, age, bank,money):
        self.name = name
        self.age = age
        self.bank = bank
        self.money = money
        
    def __str__(self):
        return f"Nome: {self.name}, Idade: {self.age}, Banco: {self.bank} Dinheiro: {self.money}"
    
    
    def pay_cart(self):
        print("a")