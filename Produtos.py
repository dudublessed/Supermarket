# Produtos do supermercado.


class Produtos:
    def __init__(self, name, value, type, quantity):   
        self.name = name
        self.value = value
        self.type = type
        self.quantity = quantity
    
    
    def __str__(self):
        return f"Produto: {self.name}, Valor: {self.value}, Tipo: {self.type}"

