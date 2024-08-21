import random

from Produtos import Produtos
from Carrinho import Carrinho
from Pessoa import Pessoa

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
        
    # Generates a random value of the user money
    nubank = random.randint(5, 800)
    itau = random.randint(5, 200)
    bradesco = random.randint(5, 100)
    santander = random.randint(5, 300)
    
    banks = [
        ["NuBank", nubank],
        ["Itaú", itau],
        ["Bradesco", bradesco],
        ["Santander", santander]
    ]
    
    print("")
    print("________________________")
    print("")
    print("Bem-vindo ao Python Market!")
    
    print("Antes de tudo, é necessário que você se cadastre em nosso sistema.")
    
    print(" ")
    print("________________________")
    print(" ")
    print("Cadastro: ")
    userName = input("Qual o seu nome? ")
    
    while True:
        try:
            userAge = int(input("Qual a sua idade? "))
            break
        except ValueError:
            print("Entrada inválida. A idade deve ser um valor inteiro.")
    
    while True:
        userBank = input("Qual o seu banco? (NuBank), (Itaú), (Bradesco), (Santander) \n")
        
        for banco in banks:
            if userBank.lower() == banco[0].lower(): 
                userMoney = banco[1]
                print(" ")
                print(f"Banco: {banco[0]}")
                print(f"Saldo: R$ {userMoney}")
                print(" ")
                print("________________________")
                print(" ")
                break
        else:
            print("Opção inválida. Selecione um dentre os bancos existentes.")
            continue
        break
    
    pessoa = Pessoa(userName, userAge, userBank, userMoney)
    
    print(f"Olá {pessoa.name}!")
    start_decision = input("Deseja ver os produtos disponíveis? Digite 'Sim' \n")
    
    if start_decision.lower() == "sim":
        carrinho.listar_produtos(produtos_disponiveis)
        
        view_decision = input("Deseja ver o seu carrinho? Digite 'Sim' \n")
        if view_decision.lower() == "sim":
            carrinho.mostrar_carrinho()
            
            remove_decision = input("Deseja retirar algum item de seu carrinho? Digite 'Sim' \n")
            if remove_decision.lower() == "sim":
                carrinho.remover_produto()
                carrinho.mostrar_carrinho()
                # pessoa.pay_cart()
            #else:
               # pessoa.pay_cart()
        else: 
            print("Muito obrigado por utilizar o Python Market!")
        
    
    else:
        print("Muito obrigado por utilizar o Python Market!")