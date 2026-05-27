def menu():
    
    while True: 
        print("Menu".center(60, "-"))
        opcao_str = input("""
    [ 1 ] - Adicionar Contato
    [ 2 ] - Alterar Contato
    [ 3 ] - Remover Contato
    [ 4 ] - Listar contatos
    [ 5 ] - Sair

    Escolha uma opção: """)
        
        try:
            opcao = int(opcao_str)
            
            if opcao == 5:
                return 5
            elif opcao == 1:
                return 1
            elif opcao == 2:
                return 2
            elif opcao == 3:
                return 3
            elif opcao == 4:
                return 4
            else:
                print("\nOpção Invalida! Escolha apenas uma das opçoes abaixo:")
                continue
            
        except ValueError:
            print("\nDigite apenas um valor inteiro!")
            continue
        
## Função para adicionar contato! ##

def adicionar_contato():
    print()
    
    print("Adicione um novo contato".title().center(60, "-"))
    
    print()
    
    while True:
    
        nome = input("Digite o nome do contato: ").strip()  
        
        if not nome.replace(" ", "").isalpha():
            print("\nNome invalido! Digite apenas letras!")
            continue
        break
    
    while True:
        telefone = input("Digite o numero de telefone: ").strip()
        
        if not telefone.isdigit():
            print("\nTelefone invalido! Digite apenas numero!")
            continue
        
        if len(telefone) != 11:
            print("\nQuantidaade de caracteres invalida! Digite 11 digitos!")
            continue
        break
    
    contato = {
        'nome': nome.title(),
        'telefone': telefone
    }
    
    contatos.append(contato)
    
    print("\nContato salvo com sucesso!")
    
## Função para alterar contato! ##
    
def alterar_contato():
    print()
    
    print("Editar Contato".title().center(60, "-"))
    
    print()
    
    if not contatos:
        print("\nNão há contatos cadastrados!")
        return
    
    listar_contato()
    
    print()
    
    while True:
    
        escolha = input("Digite o nome do contato para editar: ").strip()
        
        if not escolha.replace(" ", "").isalpha():
            print("\nNome invalido! Digite apenas letras!")
            continue
        break
    
    for contato in contatos:
        
        if escolha.lower() == contato['nome'].lower():
            
            while True: 
                nome = input("Digite o novo nome do contato: ").strip()  
                
                if not nome.replace(" ", "").isalpha():
                    print("\nNome invalido! Digite apenas letras!")
                    continue
                break
            
            while True:
                
                telefone = input("Digite o novo numero de telefone: ").strip()
            
                if not telefone.isdigit():
                    print("\nTelefone invalido! Digite apenas numero!")
                    continue
                
                if len(telefone) != 11:
                    print("\nQuantidaade de caracteres invalida! Digite 11 digitos!")
                    continue  
                break
            
            contato['nome'] = nome.title()
            contato['telefone'] = telefone
            
            print(f"\nO contato {escolha} foi alterado com sucesso!")
            return
    else:
        print("\nContato não encontrado!")
        
## Função para excluir contato! ##

def excluir_contato():
    print()
    
    print("Excluir Contato".title().center(60, "-"))
    
    print()
    
    if not contatos:
        print("\nNão há contatos cadastrados!")
        return
    
    listar_contato()
    
    print()
    
    while True:
        escolha = input("Digite o nome do contato que deseja excluir: ").strip()
        
        if not escolha.replace(" ", "").isalpha():
            print("\nNome invalido! Digite apenas letras!")
            continue
        break
    
    for contato in contatos:
        
        if escolha.lower() == contato['nome'].lower():
            contatos.remove(contato)
                
            print(f"\nO contato {escolha} foi excluido com sucesso")
            return
    else:
        print(f"\nO contato {escolha} não existe em sua lista de contatos!")
                
            
def listar_contato():
    print()
    
    print("Lista de Contatos".center(60, "-").title())
    
    print()
    
    if not contatos:
        print("Não há contatos cadastrados!")
        return
        
    print()
    print(f"Contatos: {len(contatos)}".rjust(60))
    print()
    
    for i, contato in enumerate(contatos):
        print(f"{contato['nome']:<45} {contato['telefone']:<11}")
    print()

    

#Variaveis e Dados Globais:

contatos = []
        
#Principal:

while True:
    
    opcao = menu()
    
    if opcao == 5:
        print("\nSaindo...")
        break
    elif opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        alterar_contato()
    elif opcao == 3:
        excluir_contato()
    elif opcao == 4:
        listar_contato()