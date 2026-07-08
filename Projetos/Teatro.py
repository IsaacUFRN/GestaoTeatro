import os

from validacao import (validar_cpf, validar_cpf2, validar_data, validar_preco)

from persistencia import (recupera_pecas, recupera_ingressos, 
                          recupera_atores, grava_pecas, grava_ingressos, grava_atores)

from relatorios import (lista_pecas, lista_ingressos, lista_atores, 
                        ingressos_por_peca, elenco_por_peca)


def soft_delete(dicionario, chave):
    if chave in dicionario:
        dicionario[chave][-1] = False
        return True
    return False


    ### PROGRAMA PRINCIPAL ###


pecas = recupera_pecas()
ingressos = recupera_ingressos()
atores = recupera_atores()


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

            estreia = input("Data de estreia da peça (dd/mm/aaaa): ")
            while not validar_data(estreia):
                print("\nData inválida.")
                estreia = input("Data de estreia da peça (dd/mm/aaaa): ")
            idpeca = input("ID da peça: ")
            while idpeca in pecas:
                print("\nEsse ID já está cadastrado.")
                idpeca = input("Digite outro ID da peça: ")

            preco = input("Preço da peça: ")
            while validar_preco(preco) == None:
                print("\nPreço inválido.")
                preco = input("Preço da peça: ")
            preco = validar_preco(preco)


            pecas[idpeca] = [nome, genero, duracao, estreia, preco, True]

            print("\nPeça cadastrada com sucesso!")
            input("\nTecle <ENTER> para continuar...")
            
        elif resp_pecas == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            idpeca = input("Digite o ID da peça: ")

            if idpeca in pecas:
                print("\nNome da peça:", pecas[idpeca][0])
                print("Gênero da peça:", pecas[idpeca][1])
                print("Duração da peça:", pecas[idpeca][2])
                print("Data de estreia da peça:", pecas[idpeca][3])
                print("Preço da peça:", pecas[idpeca][4])
            else:
                print("\nPeça não encontrada.")
            input("\nTecle <ENTER> para continuar...")    
            
        elif resp_pecas == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            idpeca = input("Digite o ID da peça que deseja alterar: ")

            if idpeca in pecas:

                print("Informações atuais da peça:")
                print("\nNome da peça:", pecas[idpeca][0])
                print("Gênero da peça:", pecas[idpeca][1])
                print("Duração da peça:", pecas[idpeca][2])
                print("Data de estreia da peça:", pecas[idpeca][3])
                print("Preço da peça:", pecas[idpeca][4])

                print("\nDigite as novas informações da peça:")
                nome = input("Nome da peça: ")
                genero = input("Gênero da peça: ")
                duracao = input("Duração da peça: ")

                estreia = input("Data de estreia da peça (dd/mm/aaaa): ")
                while not validar_data(estreia):
                   print("\nData inválida.")
                   estreia = input("Data de estreia da peça (dd/mm/aaaa): ")

                preco = input("Preço da peça: ")
                while validar_preco(preco) == None:
                    print("\nPreço inválido.")
                    preco = input("Preço da peça: ")
                preco = validar_preco(preco)

                pecas[idpeca] = [nome, genero, duracao, estreia, preco, True]          

                print("\nA Peça", nome, "foi atualizada com sucesso.")

            else:
                print("\nPeça não encontrada.")
            input("\nTecle <ENTER> para continuar...")    
            
        elif resp_pecas == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            idpeca = input("Digite o ID da peça que deseja deletar: ")

            if idpeca in pecas:
                print("Informações atuais da peça:")
                print("\nNome da peça:", pecas[idpeca][0])
                print("Gênero da peça:", pecas[idpeca][1])
                print("Duração da peça:", pecas[idpeca][2])
                print("Data de estreia da peça:", pecas[idpeca][3])
                
                confirma = input("\nTem certeza que deseja deletar essa peça? (s/n): ")
                
                if confirma.lower() == 's':
        
                    pecas[idpeca][-1] = False
                    
                    print("\nA Peça", pecas[idpeca][0], "foi deletada com sucesso.")
                else:
                    print("\nAção cancelada. A peça não foi deletada.")

            else:
                print("\nPeça não encontrada.")
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
            nome_cliente = input("Nome do cliente: ")
            
            cpf_cliente = input("Digite o CPF do cliente: ")
            while not validar_cpf(cpf_cliente):
                print("\nCPF inválido.")
                cpf_cliente = input("Digite o CPF do cliente: ")
                
            idingresso = input("ID do ingresso: ")
            while idingresso in ingressos:
                print("\nEsse ID de ingresso já está cadastrado.")
                idingresso = input("Digite outro ID do ingresso: ")

            id_peca = input("Digite o ID da peça: ")     
            if id_peca in pecas and pecas[id_peca][-1] == True:
                preco_peca = pecas[id_peca][4] 
                print("\nPreço do ingresso:", preco_peca)
                confirma = input("Confirme a venda (s/n): ")
                
                if confirma.lower() == 's':
                    ingressos[idingresso] = [nome_cliente, cpf_cliente, id_peca, True]
                    print("\nVenda realizada com sucesso!")
                else:
                    print("\nVenda cancelada.")
            else:
                print("\nPeça não encontrada ou encontra-se indisponível.")
            input("\nTecle <ENTER> para continuar...")            
            
        elif resp_ingr == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            idingresso = input("Digite o ID do ingresso: ")
            
            if idingresso in ingressos:
                
                id_peca = ingressos[idingresso][2]
                nome_peca = pecas[id_peca][0]
                data_peca = pecas[id_peca][3]
                preco_peca = pecas[id_peca][4] 
                
                if ingressos[idingresso][-1] == True:
                    status = "Ativo"
                else:
                    status = "Cancelado"
                
                print("\nIngresso encontrado!")
                print("Nome do cliente:", ingressos[idingresso][0])
                print("CPF do cliente:", ingressos[idingresso][1])
                print("Nome da peça:", nome_peca) 
                print("Data da peça:", data_peca)
                print("Preço do ingresso:", preco_peca)
                print("Status do ingresso:", status)
            else:
                print("\nIngresso não encontrado.")
            input("\nTecle <ENTER> para continuar...")
        
        elif resp_ingr == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            idingresso = input("Digite o ID do ingresso que deseja atualizar: ")

            if idingresso in ingressos:
                
                idpeca_atual = ingressos[idingresso][2]
                nome_peca = pecas[idpeca_atual][0] 
                if idpeca_atual in pecas:
                   nome_peca = pecas[idpeca_atual][0]
                else:
                   nome_peca = "Não encontrada"

                print("Informações atuais do ingresso:")
                print("\nNome do cliente:", ingressos[idingresso][0])
                print("CPF do cliente:", ingressos[idingresso][1])
                print("Peça atual:", nome_peca)

                print("\nDigite as novas informações do ingresso:")
                nome = input("Nome do cliente: ")
                
                cpf_cliente = input("Digite o CPF do cliente: ")
                while not validar_cpf(cpf_cliente):
                    print("\nCPF inválido.")
                    cpf_cliente = input("Digite o CPF do cliente: ")

                idpeca = input("Digite o ID da nova peça: ")
                while idpeca not in pecas or pecas[idpeca][-1] == False:
                    print("\nPeça não encontrada ou indisponível.")
                    idpeca = input("Digite o ID da nova peça: ")

                ingressos[idingresso] = [nome, cpf_cliente, idpeca, True]          

                print("\nO Ingresso foi atualizado com sucesso.")

            else:
                print("\nIngresso não encontrado.")
            input("\nTecle <ENTER> para continuar...")
            
        elif resp_ingr == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            idingresso = input("Digite o ID do ingresso que deseja cancelar: ")

            if idingresso in ingressos:
                id_peca = ingressos[idingresso][2]
                nome_peca = pecas[id_peca][0] 
                if id_peca in pecas:
                   nome_peca = pecas[id_peca][0]
                else:
                   nome_peca = "Não encontrada"

                print("Informações do ingresso:")
                print("\nCliente:", ingressos[idingresso][0])
                print("Peça:", nome_peca)
                
                confirma = input("\nTem certeza que deseja cancelar esse ingresso? (s/n): ")            
                if confirma.lower() == 's':
                    ingressos[idingresso][3] = False
                    print("\nIngresso cancelado com sucesso.")
                else:
                    print("\nAção cancelada. O ingresso continua ativo.")

            else:
                print("\nIngresso não encontrado.")
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
            print("Bem-vindo ao módulo de cadastramento de atores")
            cpfvalido = False
            cpfator = ""

            while not cpfvalido:
                cpf_input = input("Digite o CPF/ID do ator/atriz: ")
                
                if validar_cpf(cpf_input) or validar_cpf2(cpf_input):
                    cpf_limpo = cpf_input.replace(".", "").replace("-", "").strip()
                    
                    if cpf_limpo in atores:
                        print("\nEsse CPF/ID já está cadastrado.")
                    else:
                        cpfator = cpf_limpo
                        cpfvalido = True
                else:
                    print("\nCPF/ID inválido. Digite novamente.")

            nome = input("Nome do ator/atriz: ")
            idade = input("Idade do ator/atriz: ")
            genero = input("Gênero do ator/atriz: ")
            
            atorpeca = input("Peça em que o ator/atriz atua (ID da peça): ")  
            while atorpeca not in pecas or pecas[atorpeca][-1] == False:
                print("\nPeça não encontrada ou indisponível.")
                atorpeca = input("Peça em que o ator/atriz atua (ID da peça): ")

            atores[cpfator] = [nome, idade, genero, atorpeca, True]
            
            grava_atores(atores)
            
            print("\nAtor/atriz cadastrado com sucesso!")
            input("\nTecle <ENTER> para continuar...")

        elif resp_elenco == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            cpfator = input("Digite o CPF/ID do ator/atriz que deseja consultar: ")
            
            if cpfator in atores:
                idpeca = atores[cpfator][3]
                
                nome_peca = pecas[idpeca][0] if idpeca in pecas else "Não encontrada"
                
                if atores[cpfator][4] == True:
                    status = "Ativo"
                else:
                    status = "Inativo"
                
                print("\nInformações do Ator/Atriz:")
                print("Nome:", atores[cpfator][0])
                print("Idade:", atores[cpfator][1])
                print("Gênero:", atores[cpfator][2])
                print("Peça em que atua:", nome_peca)
                print("Status do ator:", status)
            else:
                print("\nAtor/atriz não encontrado.")
            input("\nTecle <ENTER> para continuar...")

        elif resp_elenco == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            cpfvalido = False
            cpfator = ""

            while not cpfvalido:
                cpf_input = input("Digite o CPF/ID do ator/atriz que deseja alterar: ")
                
                if validar_cpf(cpf_input) or validar_cpf2(cpf_input):
                    cpf_limpo = cpf_input.replace(".", "").replace("-", "").strip()
                    
                    if cpf_limpo in atores:
                        cpfator = cpf_limpo
                        cpfvalido = True
                    else:
                        print("\nAtor/atriz não encontrado no sistema.")
                        cpfvalido = True
                else:
                    print("\nCPF/ID inválido. Digite novamente.")

            if cpfator != "":
                idpeca_atual = atores[cpfator][3]
                
                if idpeca_atual in pecas:
                    nome_peca = pecas[idpeca_atual][0]
                else:
                    nome_peca = "Não encontrada"

                print("Informações atuais do ator/atriz:")
                print("\nNome:", atores[cpfator][0])
                print("Idade:", atores[cpfator][1])
                print("Gênero:", atores[cpfator][2])
                print("Peça em que atua:", nome_peca)

                print("\nDigite as novas informações:")
                nome = input("Nome do ator/atriz: ")
                idade = input("Idade do ator/atriz: ")
                genero = input("Gênero do ator/atriz: ")
                
                atorpeca = input("Peça em que o ator/atriz atua (ID da peça): ")  
                while atorpeca not in pecas or pecas[atorpeca][-1] == False:
                    print("\nPeça não encontrada ou indisponível.")
                    atorpeca = input("Peça em que o ator/atriz atua (ID da peça): ")

                atores[cpfator] = [nome, idade, genero, atorpeca, True]
                
                grava_atores(atores)
                
                print("\nCadastro do ator/atriz atualizado com sucesso!")
                
            input("\nTecle <ENTER> para continuar...")
        elif resp_elenco == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            cpfator = input("Digite o CPF/ID do ator/atriz que deseja remover/inativar: ")

            if cpfator in atores:
                idpeca = atores[cpfator][3]
                nome_peca = pecas[idpeca][0] 
                if idpeca in pecas:
                   nome_peca = pecas[idpeca][0]
                else:
                   nome_peca = "Não encontrada"

                print("Informações do ator/atriz que será inativado:")
                print("\nNome:", atores[cpfator][0])
                print("Peça em que atuava:", nome_peca)
                
                confirma = input("\nTem certeza que deseja inativar este ator/atriz? (s/n): ")
                
                if confirma.lower() == 's':
                    atores[cpfator][-1] = False
                    print("\nAtor/atriz inativado com sucesso.")
                else:
                    print("\nAção cancelada. O cadastro continua ativo.")

            else:
                print("\nAtor/atriz não encontrado.")
            input("\nTecle <ENTER> para continuar...")
       
   elif resp == '4':
            resp_rel = ""
            while resp_rel != '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
        ╔════════════════════════════════╗
        ║                                ║
        ║        Modulo Relatório        ║
        ║                                ║
        ║    1 - Lista de peças          ║
        ║    2 - Lista de ingressos      ║
        ║    3 - Lista de atores         ║
        ║    4 - Ingressos por peça      ║
        ║    5 - Elenco por peça         ║
        ║    0 - Retornar                ║
        ║                                ║
        ╚════════════════════════════════╝     
                """)
                resp_rel = input("Escolha sua opção: ")

                if resp_rel == '1':
                    lista_pecas(pecas)

                elif resp_rel == '2':
                    lista_ingressos(ingressos, pecas)

                elif resp_rel == '3':
                    lista_atores(atores, pecas)

                elif resp_rel == '4':
                    ingressos_por_peca(ingressos, pecas)

                elif resp_rel == '5':
                    elenco_por_peca(atores, pecas)

   elif resp == '5':
               print(os.system('cls' if os.name == 'nt' else 'clear'))
               print("""
       ╔════════════════════════════════════════╗
       ║                                        ║
       ║      SISTEMA DE GESTÃO  DE TEATRO      ║
       ║       Desenvolvedor: Isaac Bruno       ║
       ║        Licenca Publica Geral GNU       ║
       ║       www.gnu.org/licenses/gpl.html    ║                                        ║
       ║                                        ║
       ╚════════════════════════════════════════╝
               """)

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

grava_pecas(pecas)
grava_ingressos(ingressos)
grava_atores(atores)



