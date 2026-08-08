from core.brain import pensar
from voice.listener import ouvir
from voice.speaker import falar


def iniciar():
    print("PETER iniciado. Pode falar...")

    mensagem = ouvir(duracao=5)

    if not mensagem:
        print("Nenhuma fala foi reconhecida.")
        return

    print("PETER está pensando...")
    resposta = pensar(mensagem)

    falar(resposta)


if __name__ == "__main__":
    iniciar()