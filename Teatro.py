import os


resp = ""
while resp != '0':
   os.system('cls')


   print("""


   ░█▓▓▓█▓▓▓█▓▓▓██▓▓█▓▓▓██▓▓██▓▓██▓▓██▓▓▓█▓▓██▓▓▓█▓▓▓█▓▓▓█░
   ░█░  █░ ░█   ▓░  ▓░  ▓▒  ▒▒  ▒▒  ▒█  ░▓  ░█   █░ ░█  ░█░
   ░█░  █░ ░█   ▓░  ▓░  ▓▒  ▒▒  ▒▒  ▒█  ░▓  ░█   █░ ░█  ░█░
   ░█░  █▓█▓█   ▓▓█▓█░  ▓▓██▓▒  ▒▓██▓█  ░█▓█▓█   █▓█▓█  ░█░
   ░█░ ░█░ ░█░ ░█░  ▒▒░░█▒  ▒█  █▒  ▒█░ ▒▓  ░█░ ░█░ ░█░ ░█░
   ░█░ ▒▒      █░                            ░█      ▒▒ ░█░
   ░█░ ▒▒     ░█                              █░     ▒▓ ░█░
   ░█░ ▓▒ █   ▓░                              ░█░  █ ▒▓ ░█░
   ░█░ ▓░░█  ░█░       GESTÃO DE TEATRO       ░█░  █░░█ ░█░
   ░█░ █░▒▓  ▓░                                ░▓  ▓▒░█ ░█░
   ░█░░▓ ▓▒ ░█       1 - Modulo Peças           █░ ░▓ ▓░░█░
   ░█░▓░▒▓ ░█        2 - Modulo Ingressos        █░ ▓▒░█░█░
   ░█░█░█░▒█░        3 - Modulo Atores           ░▓▒░█░█░█░
   ░█▓░▓▒█▒          4 - Modulo Relatório          ▒█▒▓░▓█░
   ░█▒▒▒▒█           5 - Sair                       █▒▒▒▒█░
   ░█████▒                                          ▒█████░


   """)
   resp = input("Escolha sua opção: ")


   if resp == '1':  
        print("""
                     
       ╔══════════════════════════════╗
       ║                              ║
       ║         Modulo Peças         ║
       ║                              ║
       ║      1 - Cadastrar peça      ║
       ║      2 - Pesquisar peça      ║
       ║      3 - Atualizar peça      ║
       ║      4 - Deletar peça        ║
       ║      5 - Retornar            ║
       ║                              ║
       ╚══════════════════════════════╝     
                  
               """)
        resp2 = input("Escolha sua opção: ")
        if resp2 == '1':
            os.system('cls')
            nome = input("Nome da peça: ")
            genero = input("Gênero da peça: ")
            duracao = input("Duração da peça: ")
            estreia = input("Data de estreia da peça: ")
            print("\nPeça cadastrada com sucesso!")
            print("# ESSA É APENAS UMA SIMULAÇÃO, OS DADOS NÃO SERÃO SALVOS #")
            
        elif resp2 == '2':
            os.system('cls')
            nome = input("Digite o nome da peça: ")
            print("\nPeça encontrada:", nome)
            print("# ESSA É APENAS UMA SIMULAÇÃO, A FUNÇÃO NÃO ESTÁ IMPLEMENTADA #")
            
        elif resp2 == '3':
            os.system('cls')
            nome = input("Digite o nome da peça: ")

            print("\nA Peça", nome, "foi atualizada.")
            print("# ESSA É APENAS UMA SIMULAÇÃO, A FUNÇÃO NÃO ESTÁ IMPLEMENTADA #")
            
        elif resp2 == '4':
            os.system('cls')
            nome = input("Digite o nome da peça: ")
            print("A Peça", nome, "foi deletada.")
            print("# ESSA É APENAS UMA SIMULAÇÃO, A FUNÇÃO NÃO ESTÁ IMPLEMENTADA #")
            

        input("\nTecle <ENTER> para continuar...")

        
   elif resp == '2':
               print()
               print("""


       ╔══════════════════════════════╗
       ║                              ║
       ║       Modulo Ingressos       ║
       ║                              ║
       ║    1 - Cadastrar ingresso    ║
       ║    2 - Pesquisar ingresso    ║
       ║    3 - Atualizar ingresso    ║
       ║    4 - Deletar ingresso      ║
       ║    5 - Retornar              ║
       ║                              ║
       ╚══════════════════════════════╝     
                  
               """)
               input("Tecle <ENTER> para continuar...")
   elif resp == '3':
               print()
               print("""


       ╔══════════════════════════════╗
       ║                              ║
       ║         Modulo Atores        ║
       ║                              ║
       ║      1 - Cadastrar ator      ║
       ║      2 - Pesquisar ator      ║
       ║      3 - Atualizar ator      ║
       ║      4 - Deletar ator        ║
       ║      5 - Retornar            ║
       ║                              ║
       ╚══════════════════════════════╝     
                  
               """)
               input("Tecle <ENTER> para continuar...")
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
       ║     5 - Retornar              ║
       ║                                ║
       ╚════════════════════════════════╝     
                  
               """)
               input("Tecle <ENTER> para continuar...")
   elif resp == '5':
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



