# Sistema de Locadora de Filmes Online

def listar_filmes(filmes_disponiveis):
    """
    Lista todos os filmes disponíveis de forma numerada
    """
    print("\n===== FILMES DISPONÍVEIS =====\n")
    if not filmes_disponiveis:
        print("Não há filmes disponíveis no momento.")
        return
    
    for i, filme in enumerate(filmes_disponiveis, 1):
        print(f"{i}. {filme}")
    print()

def alugar_filme(filmes_disponiveis, filmes_alugados):
    """
    Permite ao usuário alugar um filme disponível
    """
    if not filmes_disponiveis:
        print("\nNão há filmes disponíveis para alugar.\n")
        return
    
    listar_filmes(filmes_disponiveis)
    
    try:
        escolha = int(input("Digite o número do filme que deseja alugar (0 para cancelar): "))
        
        if escolha == 0:
            print("Operação cancelada.")
            return
        
        if 1 <= escolha <= len(filmes_disponiveis):
            filme_escolhido = filmes_disponiveis[escolha - 1]
            
            try:
                dias = int(input(f"Por quantos dias deseja alugar '{filme_escolhido}'? "))
                
                if dias <= 0:
                    print("Número de dias inválido. Operação cancelada.")
                    return
                
                filmes_disponiveis.remove(filme_escolhido)
                filmes_alugados[filme_escolhido] = dias
                
                print(f"\nFilme '{filme_escolhido}' alugado com sucesso por {dias} dias!\n")
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        else:
            print("Opção inválida. Por favor, escolha um número válido.")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def devolver_filme(filmes_disponiveis, filmes_alugados):
    """
    Permite ao usuário devolver um filme alugado e calcula multa se houver atraso
    """
    if not filmes_alugados:
        print("\nVocê não tem filmes alugados para devolver.\n")
        return
    
    print("\n===== FILMES ALUGADOS =====\n")
    filmes_alugados_lista = list(filmes_alugados.keys())
    
    for i, filme in enumerate(filmes_alugados_lista, 1):
        print(f"{i}. {filme} - Alugado por {filmes_alugados[filme]} dias")
    
    try:
        escolha = int(input("\nDigite o número do filme que deseja devolver (0 para cancelar): "))
        
        if escolha == 0:
            print("Operação cancelada.")
            return
        
        if 1 <= escolha <= len(filmes_alugados_lista):
            filme_escolhido = filmes_alugados_lista[escolha - 1]
            dias_alugados = filmes_alugados[filme_escolhido]
            
            try:
                dias_reais = int(input(f"Por quantos dias você ficou com o filme '{filme_escolhido}'? "))
                
                if dias_reais < 0:
                    print("Número de dias inválido. Operação cancelada.")
                    return
                
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

def main():
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
            
            if opcao == 1:
                listar_filmes(filmes_disponiveis)
            elif opcao == 2:
                alugar_filme(filmes_disponiveis, filmes_alugados)
            elif opcao == 3:
                devolver_filme(filmes_disponiveis, filmes_alugados)
            elif opcao == 4:
                print("\nObrigado por usar o sistema de locadora de filmes Streamly!")
                print("Volte sempre!\n")
                break
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
        
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.\n")

if __name__ == "__main__":
    main()