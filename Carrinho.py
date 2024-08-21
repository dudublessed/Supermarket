from Produtos import Produtos

class Carrinho:
    
    # Creating the cart list
    def __init__(self):
        self.itens_carrinho = []
        
        
        
    # Adding products to the cart
class Carrinho:
    def __init__(self):
        self.itens_carrinho = []
        
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
        cart_value = 0

        if not self.itens_carrinho:
            print("O carrinho está vazio...")
        else:
            print(" ")
            print("________________________")
            print(" ")
            print("Conteúdo do carrinho:")
            for produto, quantidade in self.itens_carrinho:
                print(f"- {produto.name}, R$ {produto.value:.2f}, Quantidade: {quantidade}")
                cart_value += produto.value * quantidade
            print("__")
            print(" ")
            print(f"Valor total do carrinho: R$ {cart_value:.2f}")
            print("__")
            print(" ")
            print("________________________")
                
                
                
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
                self.adicionar_produto_carrinho(produto_encontrado)
                print(f"{produto_encontrado.name} foi adicionado ao seu carrinho!")
            else:
                print("Produto não encontrado, tente novamente.")
        
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


            item_found = False
            for i, (produto, quantidade) in enumerate(self.itens_carrinho):
                if produto.name.lower() == prodName.lower():
                    if quantidade > 1:
                        self.itens_carrinho[i] = (produto, quantidade - 1)
                else: 
                    del self.itens_carrinho[i]
                print(f"O produto '{prodName}' foi removido do seu carrinho.")
                break
            else:
                print("Item inexistente ou não se encontra no seu carrinho. Por favor, tente novamente.")
            break
                
