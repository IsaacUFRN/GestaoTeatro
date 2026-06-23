import os

pecas = {}
try:
    arq_pecas = open("pecas.csv", "rt", encoding="utf-8")
    for linha in arq_pecas:
        linha = linha.strip()
        if linha:
            campos = linha.split(",")
            idpeca = campos[0]
            nome = campos[1]
            genero = campos[2]
            duracao = campos[3]
            estreia = campos[4]
            pecas[idpeca] = [nome, genero, duracao, estreia]
    arq_pecas.close()
except:
    pecas = {
     '100' : ["Romeu e Julieta", "Drama", "2h30m", "01/07/2026"],
     '101' : ["Hamlet", "Tragédia", "3h", "05/02/2026"],
     '102' : ["O Fantasma da Ópera", "Musical", "2h45m", "10/07/2026"],
     '103' : ["O Auto da Compadecida", "Comédia", "2h15m", "20/07/2026"],
     '104' : ["As Bruxas de Salem", "Suspense", "2h", "28/07/2026"]
    }
    arq_pecas = open("pecas.csv", "wt", encoding="utf-8")
    for idpeca, dados in pecas.items():
        arq_pecas.write(f"{idpeca},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")   
    arq_pecas.close()

ingressos = {}
try:
    arq_ingressos = open("ingressos.csv", "rt", encoding="utf-8")
    for linha in arq_ingressos:
        linha = linha.strip()
        if linha:
            campos = linha.split(",")
            idingresso = campos[0]
            nome = campos[1]
            cpf = campos[2]
            peca = campos[3]
            data = campos[4]
            ingressos[idingresso] = [nome, cpf, peca, data]
    arq_ingressos.close()
except:
    ingressos = {
     'ING01' : ["Flavius Gorgonio", "12222222222", "Romeu e Julieta", "01/07/2026"],
     'ING02' : ["João Victor", "13333333333", "Hamlet", "05/02/2026"],
     'ING03' : ["Ana Beateiz", "14444444444", "O Fantasma da Ópera", "10/07/2026"],
     'ING04' : ["Carlos Henrique", "15555555555", "O Auto da Compadecida", "20/07/2026"],
     'ING05' : ["Fernanda Costa", "16666666666", "As Bruxas de Salem", "28/07/2026"]
    }
    arq_ingressos = open("ingressos.csv", "wt", encoding="utf-8")
    for idingresso, dados in ingressos.items():
        arq_ingressos.write(f"{idingresso},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
    arq_ingressos.close()

atores = {}
try:
    arq_atores = open("atores.csv", "rt", encoding="utf-8")
    for linha in arq_atores:
        linha = linha.strip()
        if linha:
            campos = linha.split(",")
            cpf = campos[0]
            nome = campos[1]
            idade = campos[2]
            sexo = campos[3]
            peca = campos[4]
            atores[cpf] = [nome, idade, sexo, peca]
    arq_atores.close()
except:
    atores = {
     '11111111111' : ["Matheus Augusto", "19 anos", "Masculino", "Romeu e Julieta"],
     '22222222222' : ["Aline Silva", "18 anos", "Feminino", "Romeu e Julieta"],
     '33333333333' : ["Davi Lucas", "22 anos", "Masculino", "O Fantasma da Ópera"],
     '44444444444' : ["Natalia Costa", "32 anos", "Feminino", "O Auto da Compadecida"],
     '55555555555' : ["Lucas Mendes", "25 anos", "Masculino", "Hamlet"]
    }
    arq_atores = open("atores.csv", "wt", encoding="utf-8")
    for cpf, dados in atores.items():
        arq_atores.write(f"{cpf},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
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
                estreia = input("Data de estreia da peça: ")

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
            cpf_cliente = input("CPF do cliente: ")
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
                    ingressos[idingresso] = [nome_cliente, cpf_cliente, nome_peca, data_peca]
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
                print("\nNome do cliente:", ingressos[idingresso][0])
                print("CPF do cliente:", ingressos[idingresso][1])
                print("Nome da peça:", ingressos[idingresso][2])
                print("Data da peça:", ingressos[idingresso][3])
            else:
                print("\nIngresso não encontrado.")
            input("\nTecle <ENTER> para continuar...")
        
        elif resp_ingr == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            idingresso = input("Digite o ID do ingresso: ")
            if idingresso in ingressos:
                print("\nInformações atuais do ingresso:")
                print("\nNome do cliente:", ingressos[idingresso][0])
                print("CPF do cliente:", ingressos[idingresso][1])
                print("Nome da peça:", ingressos[idingresso][2])
                print("Data da peça:", ingressos[idingresso][3])

                print("\nDigite as novas informações do ingresso:")
                nome_cliente = input("Nome do cliente: ")
                cpf_cliente = input("CPF do cliente: ")
                idingresso = input("ID do ingresso: ")
                idpeca = input("ID da peça: ")
                idpeca = pecas[idpeca][0]
                estreia = ingressos[idingresso][3]

                if idpeca in pecas:
                    
                    print("\nNome da peça:", pecas[idpeca][0])
                    print("Gênero da peça:", pecas[idpeca][1])
                    print("Duração da peça:", pecas[idpeca][2])
                    print("Data de estreia da peça:", pecas[idpeca][3])
                else:
                    print("\nPeça não encontrada. O ingresso não pode ser atualizado.")
                    input("\nTecle <ENTER> para continuar...")


                confirma = input("\nConfirme a atualização do ingresso para a peça acima. (s/n): ")
                if confirma.lower() == 's':
                    ingressos[idingresso] = [nome_cliente, cpf_cliente, idpeca, estreia]
                    print("\nIngresso atualizado com sucesso.")
                    print("Ingressos", ingressos)
                else:
                    print("\nA atualização do ingresso foi cancelada.")
            else:
                print("\nIngresso não encontrado.")
            input("\nTecle <ENTER> para continuar...")
            
        elif resp_ingr == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            idingresso = input("Digite o ID do ingresso: ")
            if idingresso in ingressos:
                print("\nNome do cliente:", ingressos[idingresso][0])
                print("Nome da peça:", ingressos[idingresso][1])
                print("Data da peça:", ingressos[idingresso][2])

                confirma = input("\nTem certeza que deseja cancelar esse ingresso? (s/n): ")
                if confirma.lower() == 's':
                    del ingressos[idingresso]
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
            cpfator = input("CPF do ator/atriz: ")

            atores[cpfator] = [nome, idade, genero, atorpeca]
            print("Atores:", atores)
            print("\nAtor/atriz cadastrado com sucesso!")
            input("\nTecle <ENTER> para continuar...")

        elif resp_elenco == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            cpfator = input("Digite o CPF do ator/atriz: ")

            if cpfator in atores:
                print("\nNome do ator/atriz:", atores[cpfator][0])
                print("Idade do ator/atriz:", atores[cpfator][1])
                print("Gênero do ator/atriz:", atores[cpfator][2])
                print("Peça em que o ator/atriz atua:", atores[cpfator][3])
            else:
                print("\nAtor/atriz não encontrado.")
                        
            input("\nTecle <ENTER> para continuar...")

        elif resp_elenco == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            cpfator = input("Digite o CPF do ator/atriz: ")
            if cpfator in atores:
                print("\nInformações atuais do ator/atriz:")
                print("\nNome do ator/atriz:", atores[cpfator][0])
                print("Idade do ator/atriz:", atores[cpfator][1])
                print("Gênero do ator/atriz:", atores[cpfator][2])
                print("Peça em que o ator/atriz atua:", atores[cpfator][3])
                print("\nDigite as novas informações do ator/atriz:")
                nome = input("Nome do ator/atriz: ")
                idade = input("Idade do ator/atriz: ")
                genero = input("Gênero do ator/atriz: ")
                atorpeca = input("Peça em que o ator/atriz atua: ")
                cpfator = input("CPF do ator/atriz: ")

                atores[cpfator] = [nome, idade, genero, atorpeca]          

                print("\nO cadastro do ator/atriz", nome, "foi atualizado.")
                print("Atores:", atores)
            else:
                print("\nAtor/atriz não encontrado.")
            input("\nTecle <ENTER> para continuar...")
        
        elif resp_elenco == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            cpfator = input("Digite o CPF do ator/atriz: ")
            if cpfator in atores:
                print("\nNome do ator/atriz:", atores[cpfator][0])
                print("Idade do ator/atriz:", atores[cpfator][1])
                print("Gênero do ator/atriz:", atores[cpfator][2])
                print("Peça em que o ator/atriz atua:", atores[cpfator][3])

                confirma = input("\nTem certeza que deseja remover esse ator/atriz? (s/n): ")
                if confirma.lower() == 's':
                    del atores[cpfator ]
                    print("\nAtor/atriz removido com sucesso.")
                    print("Atores:", atores)
            else:
                print("\nAtor/atriz não encontrado.")
            input("\nTecle <ENTER> para continuar...")
       input("\nTecle <ENTER> para continuar...")
   elif resp == '4':
               print(os.system('cls' if os.name == 'nt' else 'clear'))
               print("""

       ╔════════════════════════════════╗
       ║                                ║
       ║        Modulo Relatório        ║
       ║                                ║
       ║     1 - Lista de peças         ║
       ║     2 - Lista de ingressos     ║
       ║     3 - Lista de atores        ║
       ║     4 - Ingressos por peça     ║
       ║     5 - Elenco por peça        ║
       ║     0 - Retornar               ║
       ║                                ║
       ╚════════════════════════════════╝     
                  
               """)
               os.system('cls' if os.name == 'nt' else 'clear')
               input("Tecle <ENTER> para continuar...")
   elif resp == '5':
               print(os.system('cls' if os.name == 'nt' else 'clear'))
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
               print(os.system('cls' if os.name == 'nt' else 'clear'))
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

arq_pecas = open("pecas.csv", "wt", encoding="utf-8")
for idpeca, dados in pecas.items():
    arq_pecas.write(f"{idpeca},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
arq_pecas.close()

arq_ingressos = open("ingressos.csv", "wt", encoding="utf-8")
for idingresso, dados in ingressos.items():
    arq_ingressos.write(f"{idingresso},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
arq_ingressos.close()

arq_atores = open("atores.csv", "wt", encoding="utf-8")
for cpf, dados in atores.items():
    arq_atores.write(f"{cpf},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
arq_atores.close()



