"""Funções auxiliares e estruturas de formatação utilizadas pelo arquivo
main.py"""

from sys import exit
from perguntas import *
from placar import guarda_placar

verde_bg = "\033[1;42m"
vermelho_bg = "\033[1;41m"
inverte_bg = "\033[;7m "
reset = "\033[0m"
barra = "\n" + inverte_bg + "# " * 36 + reset + "\n"


def iniciar_jogo(nome):
    """Inicia um novo jogo mostrando um menu de modos de jogo e ajuda."""

    # Mostra menu
    print("\n\tTREINAMENTO")
    print("\tMARATONA")
    print("\tAJUDA")
    print("\tSAIR")

    # Recebe o modo de jogo
    modo_jogo = input('> ').lower()
    print(barra)

    # Variável de controle para assegurar um modo de jogo válido
    modo_invalido = True

    # Loop que mantém usuário no menu até que um modo válido seja escolhido
    while modo_invalido:

        if "trein" in modo_jogo:  # Modo Treinamento
            modo_invalido = False  # Sai do loop de controle
            treinamento(nome)  # Entra no modo Treinamento

        elif "mara" in modo_jogo:  # Modo Maratona
            modo_invalido = False  # Sai do loop de controle
            maratona(nome)  # Entra no modo Maratona

        elif "ajuda" in modo_jogo:  # Ajuda
            modo_invalido = False  # Sai do loop de controle
            ajuda()  # Chama função que mostra menu de Ajuda
            iniciar_jogo(nome)  # Volta para função 'iniciar_jogo()'

        elif "sair" in modo_jogo:  # Sair
            sair()  # Chama função que sai do programa

        else:  # Usuário digitou um modo inválido
            print("Modo de jogo inválido. Insira novamente:")
            modo_jogo = input('> ').lower()  # Recebe uma nova entrada


def sair():
    """Mostra mensagem de despedida e sai do programa."""

    msg_despedida = "{}MUITO OBRIGADO POR EXPERIMENTAR O JOGO"
    + "ESTADOS E CAPITAIS! ATÉ A PRÓXIMA!{}"
    print(msg_despedida.format(inverte_bg, reset))
    exit(0)


def ajuda():
    """Mostra menu de ajuda."""

    msg_treinamento = "TREINAMENTO: você escolhe o número de rodadas e no fim,"
    + " confere se acertou as respostas e a sua pontuação."

    msg_maratona = "MARATONA: você segue respondendo perguntas até errar."
    + " Sua pontuação será guardada no placar."

    print(msg_treinamento)
    print()
    print(msg_maratona)
    print(barra)


def treinamento(nome):
    """Modo Treinamento: o usuário escolhe o número de rodadas e em seguida
    reponde ao respectivo número de perguntas. No final, são mostrados os
    erros e acertos, assim como o desempenho do usuário.
    """

    # A escolha do número de rodadas
    print("Você precisa escolher o número de rodadas de treinamento:")
    numero_rodadas = int(input('> '))
    pontuacao = 0
    resultado = '\t'

    # Loop que dura o número de rodadas
    for rodada in range(numero_rodadas):

        # Imprime o número da rodada
        msg_rodada = "\n{}# # # # # # # # # # # # # # # # # RODADA {}"
        + " # # # # # # # # # # # # # # # # #{}"
        print(msg_rodada.format(inverte_bg, rodada + 1, reset))

        if pergunta():  # Quando o jogador respondeu corretamente
            pontuacao += 1  # Um ponto é adicionado
            # O número da questão é destacado em verde
            resultado += verde_bg + " {} ".format(rodada + 1) + reset + ' '

        else:  # Quando o jogador erra a resposta
            # O número da questão é destacado em vermelho
            resultado += vermelho_bg + " {} ".format(rodada + 1) + reset + ' '

    print('\n' + resultado)
    print("\nSeu desempenho: {}/{}".format(pontuacao, numero_rodadas))

    sair()  # Sai do programa


def maratona(nome):
    """Modo Maratona: o usuário irá respondendo as perguntas até que erre
    alguma. Quando o erro acontece, a pontuação é mostrada na tela e é
    armazenada no arquivo 'placar.txt' pela função 'guarda_placar()'
    """

    # Mostra a mensagem do modo Maratona
    msg_maratona = "A partir de agora você começa a maratona."
    + " Ela acaba quando você errar uma questão. Boa sorte, {}!"
    print(msg_maratona.format(nome))

    # Inicializa a pontuação em zero
    pontuacao = 0

    acertou = True
    while acertou:  # Enquanto o usuário segue acertando
        # Imprime uma barra de '# ' para melhorar visualização
        print(barra[:-1])

        if pergunta():  # Quando o usuário acerta a pergunta
            pontuacao += 1  # Um ponto é adicionado
        else:  # Quando o usuário erra a pergunta
            acertou = False  # Variável de controle recebe False e sai do loop

    print()
    print("Sua pontuação: {}".format(pontuacao))
    print()

    # Chama a função que guarda a pontuação
    guarda_placar(nome, pontuacao)
    # Chama a função que sai de 'main.py'
    sair()
