from Produtos import Produtos
from Carrinho import Carrinho

produtos_disponiveis = [
    Produtos("Pão", 0.75, "Panificação"),
    Produtos("Bolo", 20.00, "Panificação"),
    Produtos("Carne Suína", 45.00, "Carnes"),
    Produtos("Carne Bovina", 50.00, "Carnes"),
    Produtos("Maça", 3.00, "Frutas"),
    Produtos("Banana", 2.00, "Frutas")
]

if __name__ == "__main__":
    
    carrinho = Carrinho()
    
    print("Bem-vindo ao Python Market!")
    
    start_decision = input("Deseja ver os produtos disponíveis? Digite 'sim' ou 'não' \n")
    
    if start_decision.lower() == "sim":
        carrinho.listar_produtos(produtos_disponiveis)
        
        view_decision = input("Deseja ver o seu carrinho? Digite 'sim' ou 'não' \n")
        if view_decision.lower() == "sim":
            carrinho.mostrar_carrinho()
            
        
    
    else:
        print("Muito obrigado por utilizar o Python Market!")