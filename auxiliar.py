from sys import exit
from perguntas import *
from placar import guarda_placar

verde_bg = "\033[1;42m"
vermelho_bg = "\033[1;41m"
inverte_bg = "\033[;7m "
reset = "\033[0m"
barra =  "\n" + inverte_bg + "# " * 36 + reset + "\n"

def iniciar_jogo(nome):
    """Inicia um novo jogo mostrando um menu de modos de jogo e ajuda."""

    print('\n\tTREINAMENTO')
    print('\tMARATONA')
    print('\tAJUDA')
    print('\tSAIR')

    modo_jogo = input('> ').lower()
    print(barra)
    modo_invalido = True

    while modo_invalido:
        if 'trein' in modo_jogo:
            modo_invalido = False
            treinamento(nome)
        elif 'mara' in modo_jogo:
            modo_invalido = False
            maratona(nome)
        elif 'ajuda' in modo_jogo:
            modo_invalido = False
            ajuda()
            iniciar_jogo(nome)
        elif 'ajuda' in modo_jogo:
            modo_invalido = False
            sair()
        else:
            print('Modo de jogo inválido. Insira novamente:')
            modo_jogo = input('> ').lower()

def sair():
    print(f'{inverte_bg}MUITO OBRIGADO POR EXPERIMENTAR O JOGO ESTADOS E CAPITAIS! ATÉ A PRÓXIMA!{reset}')
    exit()

def ajuda():
    print('TREINAMENTO: você escolhe o número de rodadas e no fim, confere se acertou as respostas e a sua pontuação.')
    print('\nMARATONA: você segue respondendo perguntas até errar. Sua pontuação será guardada no placar.')
    print(barra)

def treinamento(nome):

    print(f'Você precisa escolher o número de rodadas de treinamento:')
    numero_rodadas = int(input('> '))
    pontuacao = 0
    resultado = '\t'

    for rodada in range(numero_rodadas):
        print(f'\n{inverte_bg}# # # # # # # # # # # # # # # # # RODADA {rodada+1} # # # # # # # # # # # # # # # # #{reset}')
        if pergunta():
            pontuacao += 1
            resultado += verde_bg + f' {rodada+1} ' + reset + ' '
        else:
            resultado += vermelho_bg + f' {rodada+1} ' + reset + ' '

    print('\n' + resultado)
    print(f'\nSeu desempenho: {pontuacao}/{numero_rodadas}')

    sair()

def maratona(nome):
    print(f"A partir de agora você começa a maratona. Ela acaba quando você errar uma questão. Boa sorte, {nome}!")
    pontuacao = 0

    acertou = True
    while acertou:
        print(barra[:-1])
        if pergunta():
            pontuacao += 1
        else:
            acertou = False

    print(f"\nSua pontuação: {pontuacao}\n")

    guarda_placar(nome, pontuacao)
    sair()