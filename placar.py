import auxiliar

def mostra_placar(nome):
    ha_placar = True

    try:
        open("placar.txt")
    except:
        ha_placar = False

    if ha_placar:
        print(f"NOME{' '*16}PLACAR\n")
        with open("placar.txt") as placar:
            for linha in placar:
                nome, pontos = linha[:-1].split()
                espaco = 20 - len(nome)
                print(f"{nome.replace('_', ' ')}{' ' * espaco}{pontos}")
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
        placar.write(f"{nome.upper().replace(' ', '_')} {pontuacao}\n")
