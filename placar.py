import auxiliar
import os


def mostra_placar(nome):
    ha_placar = True

    if os.exists("placar.txt"):
        open("placar.txt")
    else:
        ha_placar = False

    if ha_placar:
        cabecalho = "NOME" + ' ' * 16 + "PLACAR\n"
        print(cabecalho)
        with open("placar.txt") as placar:
            for linha in placar:
                nome, pontos = linha.strip().split()
                nome = nome.replace('_', ' ')
                # define a posição para o placar estar justificado à direita
                numero_rjust = len(cabecalho) - len(nome) - 1
                pontos = pontos.rjust(numero_rjust, ' ')
                print("{}{}".format(nome, pontos))
    else:
        print("Ainda não há um placar. Você deseja jogar?")
        print("\tSIM")
        print("\tNÃO")
        opcao = input('> ').lower()

        if 's' in opcao:
            auxiliar.iniciar_jogo(nome)
        else:
            print()
            auxiliar.sair()


def guarda_placar(nome, pontuacao):
    with open("placar.txt", 'a') as placar:
        nome = nome.upper().replace(' ', '_')
        placar.write("{} {}\n".format(nome, pontuacao))
