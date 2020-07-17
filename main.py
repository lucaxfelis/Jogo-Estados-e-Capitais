from dicionario import *
from auxiliar import *
from placar import mostra_placar

print(f'{inverte_bg}# # # # # # # # # # SEJA BEM VINDO(A) A ESTADOS E CAPITAIS! # # # # # # # # # #{reset}')
print('\tUm jogo sobre os estados brasileiros, suas siglas e suas capitais.\n')

nome = (input('Primeiramente, digite o seu nome: '))
print(barra)

print(f'Olá, {nome}! Você deseja iniciar o jogo ou ver os placares antigos?')

print('\n\tINICIAR JOGO')
print('\tPLACARES')
print('\tSAIR')

opcao = input('> ').lower()
print(barra)

if 'iniciar' in opcao:
    print(f'Estamos quase lá, {nome}! Agora escolha seu modo de jogo (treinamento ou maratona):')
    iniciar_jogo(nome)
elif 'placar' in opcao:
    mostra_placar(nome)
    print()
    sair()
elif 'sair' in opcao:
    sair()