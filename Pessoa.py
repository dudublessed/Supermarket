

class Pessoa:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        
    def __str__(self):
        return f"Nome: {self.name}, Idade: {self.age}, Dinheiro: {self.money}"
    
    
    def pay_cart(self):
        print("a")