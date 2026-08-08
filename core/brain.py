from core.providers.gemini import gerar_resposta


def pensar(mensagem):
    mensagem = str(mensagem).strip()

    if not mensagem:
        return ""

    return gerar_resposta(mensagem)


if __name__ == "__main__":
    resposta = pensar("Apresente-se brevemente.")
    print(f"PETER: {resposta}")