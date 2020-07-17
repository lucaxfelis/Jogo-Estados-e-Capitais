import os


def ordena_placar():
    """Cria um dicionário a partir do arquivo 'placar.txt' para
    selecionar apenas as maiores pontuações de cada jogador.

    Retorna uma lista orordenada com os nomes dos jogadores e os seus
    respectivos placares mais altos.
    """

    # Dicionário que armazenará jogadores e pontuações
    dicionario = dict()

    # Abre arquivo 'placar.txt'
    with open('placar.txt', 'r') as placar:
        # Lê as linhas do arquivo
        for linha in placar:
            jogador, pontos = linha.strip().split()
            pontos = int(pontos)
            jogador = jogador.replace('_', ' ')

            if jogador not in dicionario:  # Jogador ausente
                dicionario[jogador] = pontos
            else:  # Jogador presente
                # Testa se a nova ponuação é menor que a atual
                if dicionario[jogador] < pontos:
                    dicionario[jogador] = pontos

    # Cria uma lista com os elementos do dicionário
    lista = [(j, p) for j, p in dicionario.items()]
    # Ordena a lista de acordo com a pontuação
    lista_ordenada = sorted(lista, key=lambda item: item[1], reverse=True)

    return lista_ordenada


def mostra_placar(nome):
    """Mostra os placares salvos no arquivo placar.txt de maneira
    formatada. Função chamada por 'main.py'.

    O placar será mostrado quando o arquivo placar.txt já existir,
    o que significa que alguém já jogou e já registrou uma pontuação.
    Nesse caso, a função retorna False.
    
    Se o arquivo não existir, o usuário será perguntado se deseja
    iniciar uma partida. Se sim, retorna True. Caso contrário, retorna
    False.
    """

    # Variável de controle
    ha_placar = os.path.exists("placar.txt")

    # Controle para 'main.py'
    iniciar_novo_jogo = False

    if ha_placar:  # Quando há placar
        # Adiciona um cabeçalho para melhor visualização
        cabecalho = "NOME" + (' ' * 16) + "PLACAR\n"
        print(cabecalho)

        # Abre o arquivo e imprime o conteúdo linha por linha
        placar = ordena_placar()
        for linha in placar:
            jogador, pontos = linha

            # Define a posição para o placar estar justificado à direita
            numero_rjust = len(cabecalho) - len(jogador) - 1
            pontos = str(pontos).rjust(numero_rjust, ' ')
            print("{}{}".format(jogador, pontos))

        # Não iniciará um novo jogo em 'main.py'
        return iniciar_novo_jogo

    else:  # Quando não há placar
        print("Ainda não há um placar. Você deseja jogar?")
        print("\tSIM")
        print("\tNÃO")
        opcao = input('> ').lower()

        if 's' in opcao:
            # Iniciará um novo jogo em 'main.py'
            iniciar_novo_jogo = True
        return iniciar_novo_jogo


def guarda_placar(nome, pontuacao):
    """Função chamada quando o usuário encerra uma partida no modo
    maratona.

    Recebe o nome e a pontuação do usuário e guarda os dados em um
    arquivo chamado 'placar.txt'.
    """

    # Abre o arquivo e escreve nome e pontuação
    with open("placar.txt", 'a') as placar:
        nome = nome.upper().replace(' ', '_')
        placar.write("{} {}\n".format(nome, pontuacao))
