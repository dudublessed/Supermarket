from Produtos import Produtos

class Carrinho:
    
    def __init__(self):
        self.itens_carrinho = []
        
    def adicionar_produto_carrinho(self, produto):
        if isinstance(produto, Produtos):
            self.itens_carrinho.append(produto)
        else:
            print("O item deve ser um produto.")
            
    def mostrar_carrinho(self):
        if not self.itens_carrinho:
            print("O carrinho está vazio...")
        else:
            print("Conteúdo do carrinho:")
            for item in self.itens_carrinho:
                print(item)
                
    def listar_produtos(self, produtos_disponiveis):
        want = True
        
        while want:
            print("Produtos disponíveis: ")
            for produto in produtos_disponiveis:
                print(f"- {produto.name}, {produto.value}, {produto.type}")
            
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
        
            want_decision = input("Deseja adicionar outro produto ao seu carrinho? Digite 'sim' ou 'não': \n")
        
            if want_decision.lower() == "não":
                want = False
            elif want_decision.lower() != "sim":
                print("Opção inválida...")
                want = False
