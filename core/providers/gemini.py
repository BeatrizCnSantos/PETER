import os

from dotenv import load_dotenv
from google import genai
from datetime import datetime


load_dotenv()

chave_api = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not chave_api:
    raise RuntimeError("Chave do Gemini não encontrada no arquivo .env")

cliente = genai.Client(api_key=chave_api)

MODELO = "gemini-3.6-flash"


def gerar_resposta(mensagem):
    mensagem = str(mensagem).strip()

    agora = datetime.now().astimezone()

    dias_semana = [
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo",
    ]

    meses = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]

    data_hora_atual = (
        f"{dias_semana[agora.weekday()]}, "
        f"{agora.day} de {meses[agora.month - 1]} de {agora.year}, "
        f"às {agora:%H:%M}"
    )

    if not mensagem:
        return ""

    interacao = cliente.interactions.create(
        model=MODELO,
        input=mensagem,
        system_instruction=(
            "Você é PETER, um assistente pessoal inteligente. "
            "Responda sempre em português brasileiro, de maneira natural, "
            "clara, útil e objetiva. "
            f"A data e hora local atual do computador é {data_hora_atual}. "
            "Use essa informação quando perguntarem sobre data, dia ou horário. "
            "Como suas respostas serão faladas, responda perguntas simples "
            "em uma ou duas frases e evite despedidas ou ofertas genéricas de ajuda."
            "Use a busca somente quando precisar de informações atuais."
        ),
        #tools=[{"type": "google_search"}], so funciona com a cota do Gemini paga. que no momento não tenho. mas o Gemini free funciona bem sem a busca.
        store=False,
    )

    return interacao.output_text.strip()


if __name__ == "__main__":
    resposta = gerar_resposta("Olá, quem é você?")
    print(f"PETER: {resposta}")