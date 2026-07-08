import os

def lista_pecas(pecas):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- LISTA DE PEÇAS ---\n")
    if pecas:
        for idpeca, dados in pecas.items():
            status = "Ativa" if dados[-1] == True else "Inativa"
            print(f"ID: {idpeca} | Nome: {dados[0]} | Gênero: {dados[1]} | Preço: R$ {dados[4]} | Status: {status}")
            print("-" * 100)
        
    else:
        print("Nenhuma peça cadastrada.")
    input("\nTecle <ENTER> para continuar...")

def lista_ingressos(ingressos, pecas):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- LISTA DE INGRESSOS VENDIDOS ---\n")
    if ingressos:
        faturamento = 0.0
        for idingresso, dados in ingressos.items():
            idpeca = dados[2]
            nome_peca = pecas[idpeca][0] if idpeca in pecas else "Não encontrada"
            preco_bruto = pecas[idpeca][4] if idpeca in pecas else "0.0"
            
            if dados[-1] == True:
                status = "Ativo"
                try:
                    preco_limpo = str(preco_bruto).replace("R$", "").replace(",", ".").strip()
                    faturamento += float(preco_limpo)
                except:
    
                    pass
            else:
                status = "Cancelado"
             
            print(f"ID: {idingresso} | Cliente: {dados[0]} | Peça: {nome_peca} | Valor: {preco_bruto} | Status: {status}")
            print("-" * 50)
        print(f"\nFATURAMENTO TOTAL ATUAL: R$ {faturamento:.2f}")
        
    else:
        print("Nenhum ingresso vendido.")
        
    input("\nTecle <ENTER> para continuar...")

def lista_atores(atores, pecas):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- LISTA DE ATORES/ATRIZES ---\n")
    if atores:
        for cpfator, dados in atores.items():
            idpeca = dados[3]
            nome_peca = pecas[idpeca][0] if idpeca in pecas else "Não encontrada"
            status = "Ativo" if dados[-1] == True else "Inativo"
            print(f"CPF/ID: {cpfator} | Nome: {dados[0]} | Idade: {dados[1]} | Peça: {nome_peca} | Status: {status}")
            print("-" * 50)
    else:
        print("Nenhum actor/atriz cadastrado.")
        
    input("\nTecle <ENTER> para continuar...")

def ingressos_por_peca(ingressos, pecas):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- INGRESSOS POR PEÇA ---\n")
    idpeca_busca = input("Digite o ID da peça para filtrar: ")
    
    if idpeca_busca in pecas:
        print(f"\nIngressos para a peça: {pecas[idpeca_busca][0]}\n")
        encontrou = False
        for idingresso, dados in ingressos.items():
            if dados[2] == idpeca_busca:
                status = "Ativo" if dados[-1] == True else "Cancelado"
                print(f"ID Ingresso: {idingresso} | Cliente: {dados[0]} | Status: {status}")
                encontrou = True
        if not encontrou:
            print("Nenhum ingresso vendido para esta peça.")
    else:
        print("Peça não encontrada.")
    input("\nTecle <ENTER> para continuar...")

def elenco_por_peca(atores, pecas):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- ELENCO POR PEÇA ---\n")
    idpeca_busca = input("Digite o ID da peça para ver o elenco: ")
    
    if idpeca_busca in pecas:
        print(f"\nAtores/Atrizes na peça: {pecas[idpeca_busca][0]}\n")
        encontrou = False
        for cpfator, dados in atores.items():
            if dados[3] == idpeca_busca:
                status = "Ativo" if dados[-1] == True else "Inativo"
                print(f"Nome: {dados[0]} | Gênero: {dados[2]} | Status: {status}")
                encontrou = True
        if not encontrou:
            print("Nenhum ator vinculado a esta peça ainda.")
    else:
        print("Peça não encontrada.")
    input("\nTecle <ENTER> para continuar...") 