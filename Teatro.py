import os
import pickle

pecas = {}
try:
    arq_pecas = open("pecas.dat", "rb")
    pecas = pickle.load(arq_pecas)
except:
    pecas = {
     '100' : ["Romeu e Julieta", "Drama", "2h30m", "01/07/2026"],
     '101' : ["Hamlet", "Tragédia", "3h", "05/02/2026"],
     '102' : ["O Fantasma da Ópera", "Musical", "2h45m", "10/07/2026"],
     '103' : ["O Auto da Compadecida", "Comédia", "2h15m", "20/07/2026"],
     '104' : ["As Bruxas de Salem", "Suspense", "2h", "28/07/2026"]
    }
    arq_pecas = open("pecas.dat", "wb")
    pickle.dump(pecas, arq_pecas)
    arq_pecas.close()

ingressos = {}
try:
    arq_ingressos = open("ingressos.dat", "rb")
    ingressos = pickle.load(arq_ingressos)
except:
    ingressos = {
     '200' : ["Flavius Gorgonio", "Romeu e Julieta", "01/07/2026"],
     '201' : ["João Victor", "Hamlet", "05/02/2026"],
     '202' : ["Ana Beateiz", "O Fantasma da Ópera", "10/07/2026"],
     '203' : ["Carlos Henrique", "O Auto da Compadecida", "20/07/2026"],
     '204' : ["Fernanda Costa", "As Bruxas de Salem", "28/07/2026"]
    }
    arq_ingressos = open("ingressos.dat", "wb")
    pickle.dump(ingressos, arq_ingressos)
    arq_ingressos.close()

atores = {}
try:
    arq_atores = open("atores.dat", "rb")
    atores = pickle.load(arq_atores)
except:
    atores = {
     '300' : ["Matheus Augusto", "19 anos", "Masculino", "Romeu e Julieta"],
     '301' : ["Aline Silva", "18 anos", "Feminino", "Romeu e Julieta"],
     '302' : ["Davi Lucas", "22 anos", "Masculino", "O Fantasma da Ópera"],
     '303' : ["Natalia Costa", "32 anos", "Feminino", "O Auto da Compadecida"],
     '304' : ["Lucas Mendes", "25 anos", "Masculino", "Hamlet"]
    }
    arq_atores = open("atores.dat", "wb")
    pickle.dump(atores, arq_atores)
    arq_atores.close()

resp = ""
while resp != '0':
   os.system('cls' if os.name == 'nt' else 'clear' )


   print("""


   ░█▓▓▓█▓▓▓█▓▓▓██▓▓█▓▓▓██▓▓██▓▓██▓▓██▓▓▓█▓▓██▓▓▓█▓▓▓█▓▓▓█░
   ░█░  █░ ░█   ▓░  ▓░  ▓▒  ▒▒  ▒▒  ▒█  ░▓  ░█   █░ ░█  ░█░
   ░█░  █░ ░█   ▓░  ▓░  ▓▒  ▒▒  ▒▒  ▒█  ░▓  ░█   █░ ░█  ░█░
   ░█░  █▓█▓█   ▓▓█▓█░  ▓▓██▓▒  ▒▓██▓█  ░█▓█▓█   █▓█▓█  ░█░
   ░█░ ░█░ ░█░ ░█░  ▒▒░░█▒  ▒█  █▒  ▒█░ ▒▓  ░█░ ░█░ ░█░ ░█░
   ░█░ ▒▒      █░                            ░█      ▒▒ ░█░
   ░█░ ▒▒     ░█                              █░     ▒▓ ░█░
   ░█░ ▓▒ █   ▓░       GESTÃO DE TEATRO       ░█░  █ ▒▓ ░█░
   ░█░ ▓░░█  ░█░                              ░█░  █░░█ ░█░
   ░█░ █░▒▓  ▓░      1 - Modulo Peças          ░▓  ▓▒░█ ░█░
   ░█░░▓ ▓▒ ░█       2 - Modulo Ingressos       █░ ░▓ ▓░░█░
   ░█░▓░▒▓ ░█        3 - Modulo Elenco           █░ ▓▒░█░█░
   ░█░█░█░▒█░        4 - Modulo Relatório        ░▓▒░█░█░█░
   ░█▓░▓▒█▒          5 - Modulo Informações        ▒█▒▓░▓█░
   ░█▒▒▒▒█           0 - Sair                       █▒▒▒▒█░
   ░█████▒                                          ▒█████░


   """)
   resp = input("Escolha sua opção: ")


   if resp == '1':
       resp_pecas = ""
       while resp_pecas != '0':
        os.system('cls' if os.name == 'nt' else 'clear')
 
        print("""
                     
       ╔══════════════════════════════╗
       ║                              ║
       ║         Modulo Peças         ║
       ║                              ║
       ║      1 - Cadastrar peça      ║
       ║      2 - Pesquisar peça      ║
       ║      3 - Atualizar peça      ║
       ║      4 - Deletar peça        ║
       ║      0 - Retornar            ║
       ║                              ║
       ╚══════════════════════════════╝     
                  
               """)
        resp_pecas = input("Escolha sua opção: ")
        if resp_pecas == '1':
            
            print("Bem-vindo ao módulo de cadastramento de peças!")
            print("↓ Preencha as informações abaixo ↓")
            
            nome = input("Nome da peça: ")
            genero = input("Gênero da peça: ")
            duracao = input("Duração da peça: ")
            estreia = input("Data de estreia da peça: ")
            idpeca = input("ID da peça: ")

            pecas[idpeca] = [nome, genero, duracao, estreia]
            print("\nPeça cadastrada com sucesso!")
            print("\nPeças", pecas)

            input("\nTecle <ENTER> para continuar...")
            
        elif resp_pecas == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            idpeca = input("Digite o ID da peça: ")

            if idpeca in pecas:
                print("\nNome da peça:", pecas[idpeca][0])
                print("Gênero da peça:", pecas[idpeca][1])
                print("Duração da peça:", pecas[idpeca][2])
                print("Data de estreia da peça:", pecas[idpeca][3])
            else:
                print("\nPeça não encontrada.")
            input("\nTecle <ENTER> para continuar...")    

            
        elif resp_pecas == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            idpeca = input("Digite o ID da peça: ")

            if idpeca in pecas:

                print("Informações atuais da peça:")
                print("\nNome da peça:", pecas[idpeca][0])
                print("Gênero da peça:", pecas[idpeca][1])
                print("Duração da peça:", pecas[idpeca][2])
                print("Data de estreia da peça:", pecas[idpeca][3])
                print("Digite as novas informações da peça:")
                nome = input("Nome da peça: ")
                genero = input("Gênero da peça: ")
                duracao = input("Duração da peça: ")

                pecas[idpeca] = [nome, genero, duracao, estreia]          

                print("\nA Peça", nome, "foi atualizada.")
                print("Peças", pecas)

            else:
                print("\nPeça não encontrada.")
            input("\nTecle <ENTER> para continuar...")    
            
        elif resp_pecas == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            idpeca = input("Digite o ID da peça: ")

            if idpeca in pecas:
                print("\nNome da peça:", pecas[idpeca][0])
                print("Gênero da peça:", pecas[idpeca][1])
                print("Duração da peça:", pecas[idpeca][2])
                print("Data de estreia da peça:", pecas[idpeca][3])

                confirma = input("\nTem certeza que deseja deletar essa peça? (s/n): ")
                if confirma.lower() == 's':
                    del pecas[idpeca]
                    print("\nPeça deletada com sucesso.")
                    print("Peças", pecas)
                else:
                     print("\nA peça não foi deletada.")            
            else:
                print("\nPeça não encontrada.")
                input("\nTecle <ENTER> para continuar...")
       input("\nTecle <ENTER> para continuar...")
            
        
   elif resp == '2':
       resp_ingr = ""
       while resp_ingr != '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        print("""


       ╔══════════════════════════════╗
       ║                              ║
       ║       Modulo Ingressos       ║
       ║                              ║
       ║    1 - Cadastrar ingresso    ║
       ║    2 - Consultar ingresso    ║
       ║    3 - Atualizar ingresso    ║
       ║    4 - Cancelar ingresso     ║
       ║    0 - Retornar              ║
       ║                              ║
       ╚══════════════════════════════╝     
                  
               """)
        resp_ingr = input("Escolha sua opção: ")

        if resp_ingr == '1':
            print("Bem-vindo ao módulo de cadastramento de ingressos!")
            print("↓ Preencha as informações abaixo ↓")
                
            nome_cliente = input("Nome do cliente: ")
            idingresso = input("ID do ingresso: ")
            id_peca = input("Digite o ID da peça: ")

            if id_peca in pecas:
                nome_peca = pecas[id_peca][0]
                data_peca = pecas[id_peca][3]

                print("\nNome da peça:", pecas[id_peca][0])
                print("Gênero da peça:", pecas[id_peca][1])
                print("Duração da peça:", pecas[id_peca][2])
                print("Data de estreia da peça:", data_peca)

                confirma = input("\nConfirme a compra do ingresso. (s/n): ")
                if confirma.lower() == 's':
                    ingressos[idingresso] = [nome_cliente, nome_peca, data_peca]
                    print("\nIngresso vendido com sucesso!")
                else:
                    print("\nCompra cancelada.")
            else:
                print("\nID da peça não encontrado! Tente novamente.")
                
            input("\nTecle <ENTER> para continuar...")            
            
        elif resp_ingr == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            idingresso = input("Digite o ID do ingresso: ")

            if idingresso in ingressos:
                print("\nIngresso encontrado!")
                print("\nNome do cliente:", ingressos[idnome][0])
                print("Nome da peça:", ingressos[idnome][1])
                print("Data da peça:", ingressos[idnome][2])
            else:
                print("\nIngresso não encontrado.")
            input("\nTecle <ENTER> para continuar...")
        
        elif resp_ingr == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            idnome = input("Digite o nome ou ID do ingresso: ")
            if idnome in ingressos:
                print("\nInformações atuais do ingresso:")
                print("\nNome do cliente:", ingressos[idnome][0])
                print("Nome da peça:", ingressos[idnome][1])
                print("Data da peça:", ingressos[idnome][2])
                print("\nDigite as novas informações do ingresso:")
                nome_cliente = input("Nome do cliente: ")
                idingresso = input("ID do ingresso: ")
                idnome_peca = input("Nome ou ID da peça: ")
                idnome_peca = pecas[idnome_peca][0]
                estreia = ingressos[idnome][2]
                
                if idnome_peca in pecas:
                    
                    print("\nNome da peça:", pecas[idnome_peca][0])
                    print("Gênero da peça:", pecas[idnome_peca][1])
                    print("Duração da peça:", pecas[idnome_peca][2])
                    print("Data de estreia da peça:", pecas[idnome_peca][3])
                else:
                    print("\nPeça não encontrada. O ingresso não pode ser atualizado.")
                    input("\nTecle <ENTER> para continuar...")


                confirma = input("\nConfirme a atualização do ingresso para a peça acima. (s/n): ")
                if confirma.lower() == 's':
                    ingressos[idnome] = [nome_cliente, idnome_peca, estreia]
                    print("\nIngresso atualizado com sucesso.")
                    print("Ingressos", ingressos)
                else:
                    print("\nA atualização do ingresso foi cancelada.")
            else:
                print("\nIngresso não encontrado.")
            input("\nTecle <ENTER> para continuar...")
            
        elif resp_ingr == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            idnome = input("Digite o nome ou ID do ingresso: ")
            if idnome in ingressos:
                print("\nNome do cliente:", ingressos[idnome][0])
                print("Nome da peça:", ingressos[idnome][1])
                print("Data da peça:", ingressos[idnome][2])
                
                confirma = input("\nTem certeza que deseja cancelar esse ingresso? (s/n): ")
                if confirma.lower() == 's':
                    del ingressos[idnome]
                    print("\nIngresso cancelado com sucesso.")
                    print("Ingressos", ingressos)
            else:
                print("\nIngresso não encontrado.")
            input("\nTecle <ENTER> para continuar...")
       input("\nTecle <ENTER> para continuar...")     

   elif resp == '3':
       resp_elenco = ""
       while resp_elenco != '0':
        os.system('cls' if os.name == 'nt' else 'clear')        
               
        print("""


       ╔══════════════════════════════╗
       ║                              ║
       ║         Modulo Elenco        ║
       ║                              ║
       ║   1 - Cadastrar ator/atriz   ║
       ║   2 - Pesquisar ator/atriz   ║
       ║    3 - Atualizar cadastro    ║
       ║    4 - Remover ator/atriz    ║
       ║         0 - Retornar         ║
       ║                              ║
       ╚══════════════════════════════╝     
                  
               """)
        resp_elenco = input("Escolha sua opção: ")

        if resp_elenco == '1':
            print("Bem-vindo ao módulo de cadastramento do elenco!")
            print("↓ Preencha as informações abaixo ↓")
            
            nome = input("Nome do ator/atriz: ")
            idade = input("Idade do ator/atriz: ")
            genero = input("Gênero do ator/atriz: ")
            atorpeca = input("Peça em que o ator/atriz atua: ")
            idator = input("ID do ator/atriz: ")

            atores[idator] = [nome, idade, genero, atorpeca]
            print("Atores:", atores)
            print("\nAtor/atriz cadastrado com sucesso!")
            input("\nTecle <ENTER> para continuar...")

        elif resp_elenco == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            idator = input("Digite o ID do ator/atriz: ")

            if idator in atores:
                print("\nNome do ator/atriz:", atores[idator][0])
                print("Idade do ator/atriz:", atores[idator][1])
                print("Gênero do ator/atriz:", atores[idator][2])
                print("Peça em que o ator/atriz atua:", atores[idator][3])
            else:
                print("\nAtor/atriz não encontrado.")
                        
            input("\nTecle <ENTER> para continuar...")

        elif resp_elenco == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            idator = input("Digite o ID do ator/atriz: ")
            if idator in atores:
                print("\nInformações atuais do ator/atriz:")
                print("\nNome do ator/atriz:", atores[idator][0])
                print("Idade do ator/atriz:", atores[idator][1])
                print("Gênero do ator/atriz:", atores[idator][2])
                print("Peça em que o ator/atriz atua:", atores[idator][3])
                print("\nDigite as novas informações do ator/atriz:")
                nome = input("Nome do ator/atriz: ")
                idade = input("Idade do ator/atriz: ")
                genero = input("Gênero do ator/atriz: ")
                atorpeca = input("Peça em que o ator/atriz atua: ")
                idator = input("ID do ator/atriz: ")

                atores[idator] = [nome, idade, genero, atorpeca]          

                print("\nO cadastro do ator/atriz", nome, "foi atualizado.")
                print("Atores:", atores)
            else:
                print("\nAtor/atriz não encontrado.")
            input("\nTecle <ENTER> para continuar...")
        
        elif resp_elenco == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            idator = input("Digite o ID do ator/atriz: ")
            if idator in atores:
                print("\nNome do ator/atriz:", atores[idator][0])
                print("Idade do ator/atriz:", atores[idator][1])
                print("Gênero do ator/atriz:", atores[idator][2])
                print("Peça em que o ator/atriz atua:", atores[idator][3])

                confirma = input("\nTem certeza que deseja remover esse ator/atriz? (s/n): ")
                if confirma.lower() == 's':
                    del atores[idator]
                    print("\nAtor/atriz removido com sucesso.")
                    print("Atores:", atores)
            else:
                print("\nAtor/atriz não encontrado.")
            input("\nTecle <ENTER> para continuar...")
       input("\nTecle <ENTER> para continuar...")
   elif resp == '4':
               print()
               print("""


       ╔════════════════════════════════╗
       ║                                ║
       ║        Modulo Relatório        ║
       ║                                ║
       ║     1 - Gerar relatório        ║
       ║     2 - Visualizar relatório   ║
       ║     3 - Exportar relatório     ║
       ║     4 - Deletar relatório      ║
       ║     5 - Retornar               ║
       ║                                ║
       ╚════════════════════════════════╝     
                  
               """)
               os.system('cls' if os.name == 'nt' else 'clear')
               input("Tecle <ENTER> para continuar...")
   elif resp == '5':
               print()
               print("""
       ╔════════════════════════════════════════╗
       ║                                        ║
       ║      SISTEMA DE GESTÃO  DE TEATRO      ║
       ║       Desenvolvedor: Isaac Bruno       ║
       ║                                        ║
       ╚════════════════════════════════════════╝
               """)
               os.system('cls' if os.name == 'nt' else 'clear')
               input("Tecle <ENTER> para continuar...")
   elif resp == '0':
               print()
               print("""


       ╔════════════════════════════════════════╗
       ║                                        ║
       ║           PROGRAMA ENCERRADO!          ║
       ║                Até mais                ║
       ║                                        ║
       ╚════════════════════════════════════════╝     
                  
               """)


               input("Tecle <ENTER> para continuar...")
   else:
               print()
               print("""


       ╔════════════════════════════════════════╗
       ║                                        ║
       ║            OPÇÃO INVÁLIDA!             ║
       ║   Retorne ao menu e tente novamente.   ║
       ║                                        ║
       ╚════════════════════════════════════════╝     
                  
               """)
               input("Tecle <ENTER> para continuar...")


print("Fim")

arq_pecas = open("pecas.dat", "wb")
pickle.dump(pecas, arq_pecas)
arq_pecas.close()

arq_ingressos = open("ingressos.dat", "wb")
pickle.dump(ingressos, arq_ingressos)
arq_ingressos.close()

arq_atores = open("atores.dat", "wb")
pickle.dump(atores, arq_atores)
arq_atores.close()



