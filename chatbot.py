from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import pandas as pd

arquivo_de_treinamento = 'treinamento_inicial.txt'
bot = ChatBot('roboTI', logic_adapters=['chatterbot.logic.BestMatch'])

def menu_de_erros():
    print("""Problemas comuns:
    Internet Lenta, Estou sem Internet, Computador não liga,\n
    Minha impressora não funciona, estou com problemas na impressora.
            """)

def get_lista_treinamento(caminho_arquivo):
    """Esta função define como o bot será treinado a partir de uma dada lista."""
    treinamento = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8', errors='ignore') as data:
            for item in data.readlines():
                treinamento.append(item)
    except Exception:
        pass

    return treinamento

def treina_bot(lista_treinamento):
    conversa = ListTrainer(bot)
    conversa.train(lista_treinamento)


if __name__ == "__main__":

    lista_treinamento = get_lista_treinamento(arquivo_de_treinamento)
    try:
        treina_bot(lista_treinamento)
    except Exception:
        pass
    menu_de_erros()
    print("Para começar digite 'Ola', 'Oi', ou entre com um problema mencionado acima.")
    while True:
        try:
            pergunta = input('Usuário: ')
        except Exception:
            pass
        resposta = bot.get_response(pergunta)
        if float(resposta.confidence) > 0.5:
            print('RoboTI: ', resposta)
        else:
            print('RoboTI: Hmmm lamento, mas ainda não entendi direito')
