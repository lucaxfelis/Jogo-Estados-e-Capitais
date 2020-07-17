from random import *
from dicionario import *
from unicodedata import normalize, combining


def formata(item):
    """Formata item deixando todas as letras minúsculas e ignorando
    a acentuação."""

    item = item.lower()
    return ''.join(ch for ch in normalize('NFKD', item) if not combining(ch))


def pergunta():
    """Realiza pergunta e retorna True, se o palpite do usuário for
    correto, e False, caso contrário.

    Escolhe aleatóriamente um tipo de pergunta, entre as seis possíveis
    e um item do dicionário de estados e capitais e faz a pergunta ao
    usuário.

    Essa função ignora acentuação e letras maiúsculas, ou seja,
    se o palpite não possuir acentuação correta ou alguma letra
    maiúscula, será considerada correto se combinar com a resposta.
    """

    # Lê o dicionário e escolhe um item aleatoriamente
    lista = list(dicionario_estados_capitais.items())
    estado, (capital, sigla) = choice(lista)

    # Dicionário com os seis tipos de perguntas possíveis,
    # os complementos das mensagens, e as respostas certas.
    perguntas = {
        1: ("Qual estado brasileiro possui a sigla {}?", sigla, estado),
        2: ("Qual estado brasileiro possui a capital {}?", capital, estado),
        3: ("Qual a capital do estado brasileiro {}?", estado, capital),
        4: ("Qual a capital do estado brasileiro de sigla {}?",
            sigla, capital),
        5: ("Qual a sigla do estado brasileiro {}?", estado, sigla),
        6: ("Qual a sigla do estado brasileiro cujo a capital é {}?",
            capital, sigla)
    }

    # Escolhe aleatóriamente um tipo de pergunta
    tipo = randint(1, 6)

    # extrai a mensagem, o complemento e a resposta
    (pergunta, complemento, resposta) = perguntas[tipo]

    # imprime a pergunta, recebe o palpite e retorna True
    # se o palpite está correto, e False, caso contrário
    print(pergunta.format(complemento))
    palpite = formata(input('> '))
    return palpite == formata(resposta)
