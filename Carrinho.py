from Produtos import Produtos 
        
    # Adding products to the cart
class Carrinho:
    
    
    def __init__(self, cart_value):
        self.itens_carrinho = []
        self.cart_value = cart_value
        
    def adicionar_produto_carrinho(self, produto):
        if isinstance(produto, Produtos):
            for i, item in enumerate(self.itens_carrinho):
                if item[0].name == produto.name:
                    self.itens_carrinho[i] = (item[0], item[1] + 1)
                    break
            else:
                self.itens_carrinho.append((produto, 1))
        else:
            print("O item deve ser um produto.")
            
            
    # Displaying the itens on the cart list
    def mostrar_carrinho(self):
        
        if not self.itens_carrinho:
            print("O carrinho está vazio...")
        else:
            print(" ")
            print("________________________")
            print(" ")
            print("Conteúdo do carrinho:")
            for produto, quantidade in self.itens_carrinho:
                print(f"- {produto.name}, R$ {produto.value:.2f}, Quantidade: {quantidade}")
                self.cart_value = produto.value * quantidade
            print("__")
            print(" ")
            print(f"Valor total do carrinho: R$ {self.cart_value:.2f}")
            print("__")
            print(" ")
            print("________________________")
            print(" ")
                
    def mostrar_valor_carrinho(self):
        return self.cart_value
                
                
    # Showing avaiable products and calling the funcion that adds products to the cart according to the user selection            
    def listar_produtos(self, produtos_disponiveis):
        
        while True:
            print(" ")
            print("________________________")
            print(" ")
            print("Produtos disponíveis: ")
            for produto in produtos_disponiveis:
                print(f"- {produto.name}, R$ {produto.value:.2f}, {produto.type}, {produto.quantity}")
            print(" ")
            print("________________________")
            print(" ")
            nome_escolhido = input("Digite o nome do produto que você deseja adicionar ao seu carrinho: \n")
        
            produto_encontrado = None
            
            for produto in produtos_disponiveis:
                if produto.name.lower() == nome_escolhido.lower():
                    produto_encontrado = produto
                    break
        
            if produto_encontrado:
                if produto_encontrado.quantity > 0:
                    self.adicionar_produto_carrinho(produto_encontrado)
                    produto_encontrado.quantity -= 1
                    print(f"{produto_encontrado.name} foi adicionado ao seu carrinho!")

                    if produto_encontrado.quantity == 0:
                        produtos_disponiveis.remove(produto_encontrado)
                        print(f"{produto_encontrado.name} está fora de estoque e foi removido da lista de produtos disponíveis.")
                else:
                    print(f"O produto {produto_encontrado.name} está fora de estoque.")
        
            else:
                print("Produto não encontrado, tente novamente.")
                continue
        
            while True: 
                want_decision = input("Deseja adicionar outro produto ao seu carrinho? Digite 'Sim' ou 'Não': \n")

                if want_decision.lower() == "sim":
                    break
                if want_decision.lower() == "não":
                    return
                elif want_decision.lower() != "sim":
                    print("Opção inválida...")
                    continue
                    

    def remover_produto(self):
        while True:
            prodName = input("Digite o nome do produto a ser removido: \n")
            prodName_lower = prodName.lower()
        

            item_found = False
        

            for i, (produto, quantidade) in enumerate(self.itens_carrinho):
                if produto.name.lower() == prodName_lower:
                    item_found = True
                    if quantidade > 1:
                        self.itens_carrinho[i] = (produto, quantidade - 1)
                    else:
                        del self.itens_carrinho[i]
                print(f"O produto '{prodName}' foi removido do seu carrinho.")
                break
        
            if not item_found:
                print("Item inexistente ou não se encontra no seu carrinho. Por favor, tente novamente.")
            else:
                break

                
