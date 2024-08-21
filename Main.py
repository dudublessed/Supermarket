from Produtos import Produtos
from Carrinho import Carrinho

produtos_disponiveis = [
    Produtos("Pão", 0.75, "Panificação", 12),
    Produtos("Bolo Formigueiro", 15.00, "Panificação", 2),
    Produtos("Bolo de Chocolate", 20.00, "Panificação", 4),
    Produtos("Carne Suína", 45.00, "Carnes", 7),
    Produtos("Carne Bovina", 50.00, "Carnes", 8),
    Produtos("Maça", 3.00, "Frutas", 25),
    Produtos("Banana da Terra", 2.00, "Frutas", 24),
    Produtos("Banana Prata", 2.50, "Frutas", 18)
]

if __name__ == "__main__":
    
    carrinho = Carrinho()
    
    print("Bem-vindo ao Python Market!")
    
    start_decision = input("Deseja ver os produtos disponíveis? Digite 'sim'\n")
    
    if start_decision.lower() == "sim":
        carrinho.listar_produtos(produtos_disponiveis)
        
        view_decision = input("Deseja ver o seu carrinho? Digite 'sim' \n")
        if view_decision.lower() == "sim":
            carrinho.mostrar_carrinho()

        else: 
            print("Muito obrigado por utilizar o Python Market!")
        
    
    else:
        print("Muito obrigado por utilizar o Python Market!")