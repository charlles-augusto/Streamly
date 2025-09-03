# Sistema de Locadora de Filmes Online sem usar funções (def)

# Lista de filmes disponíveis inicialmente
filmes_disponiveis = [
    "Vingadores: Ultimato",
    "O Poderoso Chefão",
    "Pulp Fiction",
    "Matrix",
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Star Wars: Episódio V - O Império Contra-Ataca",
    "Interestelar",
    "Cidade de Deus",
    "Jurassic Park",
    "Titanic",
    "Invocação do Mal",
    "Como Treinar seu Dragão",
    "Godzilla",
    "F1",
    "Jurassic World"
]

# Dicionário para armazenar filmes alugados e seus prazos
filmes_alugados = {}

# Loop principal do programa
while True:
    print("\n===== STREAMLY - LOCADORA DE FILMES ONLINE =====\n")
    print("1. Listar filmes disponíveis")
    print("2. Alugar um filme")
    print("3. Devolver um filme")
    print("4. Sair do sistema")
    
    try:
        opcao = int(input("\nEscolha uma opção: "))
        
        # Opção 1: Listar filmes disponíveis
        if opcao == 1:
            print("\n===== FILMES DISPONÍVEIS =====\n")
            if not filmes_disponiveis:
                print("Não há filmes disponíveis no momento.")
            else:
                for i, filme in enumerate(filmes_disponiveis, 1):
                    print(f"{i}. {filme}")
                print()
        
        # Opção 2: Alugar um filme
        elif opcao == 2:
            if not filmes_disponiveis:
                print("\nNão há filmes disponíveis para alugar.\n")
            else:
                # Listar filmes disponíveis
                print("\n===== FILMES DISPONÍVEIS =====\n")
                for i, filme in enumerate(filmes_disponiveis, 1):
                    print(f"{i}. {filme}")
                print()
                
                try:
                    escolha = int(input("Digite o número do filme que deseja alugar (0 para cancelar): "))
                    
                    if escolha == 0:
                        print("Operação cancelada.")
                    elif 1 <= escolha <= len(filmes_disponiveis):
                        filme_escolhido = filmes_disponiveis[escolha - 1]
                        
                        try:
                            dias = int(input(f"Por quantos dias deseja alugar '{filme_escolhido}'? "))
                            
                            if dias <= 0:
                                print("Número de dias inválido. Operação cancelada.")
                            else:
                                filmes_disponiveis.remove(filme_escolhido)
                                filmes_alugados[filme_escolhido] = dias
                                
                                print(f"\nFilme '{filme_escolhido}' alugado com sucesso por {dias} dias!\n")
                        
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um número.")
                    else:
                        print("Opção inválida. Por favor, escolha um número válido.")
                
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        
        # Opção 3: Devolver um filme
        elif opcao == 3:
            if not filmes_alugados:
                print("\nVocê não tem filmes alugados para devolver.\n")
            else:
                print("\n===== FILMES ALUGADOS =====\n")
                filmes_alugados_lista = list(filmes_alugados.keys())
                
                for i, filme in enumerate(filmes_alugados_lista, 1):
                    print(f"{i}. {filme} - Alugado por {filmes_alugados[filme]} dias")
                
                try:
                    escolha = int(input("\nDigite o número do filme que deseja devolver (0 para cancelar): "))
                    
                    if escolha == 0:
                        print("Operação cancelada.")
                    elif 1 <= escolha <= len(filmes_alugados_lista):
                        filme_escolhido = filmes_alugados_lista[escolha - 1]
                        dias_alugados = filmes_alugados[filme_escolhido]
                        
                        try:
                            dias_reais = int(input(f"Por quantos dias você ficou com o filme '{filme_escolhido}'? "))
                            
                            if dias_reais < 0:
                                print("Número de dias inválido. Operação cancelada.")
                            else:
                                # Cálculo da multa (R$ 2,00 por dia de atraso)
                                if dias_reais > dias_alugados:
                                    dias_atraso = dias_reais - dias_alugados
                                    multa = dias_atraso * 2.0
                                    print(f"\nVocê devolveu o filme com {dias_atraso} dias de atraso.")
                                    print(f"Multa a pagar: R$ {multa:.2f}")
                                else:
                                    print("\nFilme devolvido dentro do prazo. Obrigado!")
                                
                                # Remover o filme dos alugados e adicionar de volta aos disponíveis
                                del filmes_alugados[filme_escolhido]
                                filmes_disponiveis.append(filme_escolhido)
                                print(f"Filme '{filme_escolhido}' devolvido com sucesso!\n")
                        
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um número.")
                    else:
                        print("Opção inválida. Por favor, escolha um número válido.")
                
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        
        # Opção 4: Sair do sistema
        elif opcao == 4:
            print("\nObrigado por usar o sistema de locadora de filmes Streamly!")
            print("Volte sempre!\n")
            break
        
        # Opção inválida
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
    
    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número.\n")