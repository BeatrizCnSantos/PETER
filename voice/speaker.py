import base64
import os
import wave
import winsound
from pathlib import Path

from dotenv import load_dotenv
from google import genai


load_dotenv()

chave_api = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not chave_api:
    raise RuntimeError("Chave do Gemini não encontrada no arquivo .env")

cliente = genai.Client(api_key=chave_api)

MODELO = "gemini-3.1-flash-tts-preview"
VOZ = "Iapetus"
ARQUIVO_VOZ = Path(__file__).parent / "fala_peter.wav"


def salvar_wav(caminho, audio_pcm):
    with wave.open(str(caminho), "wb") as arquivo:
        arquivo.setnchannels(1)
        arquivo.setsampwidth(2)
        arquivo.setframerate(24000)
        arquivo.writeframes(audio_pcm)


def falar(texto):
    texto = str(texto).strip()

    if not texto:
        return

    print(f"PETER: {texto}")

    prompt = f"""
    Fale em português brasileiro com uma voz masculina adulta, humana,
    natural e calorosa. Use ritmo moderado e tom de conversa.
    Não use tom de locutor e não pareça um robô.

    Pronuncie somente o texto abaixo, sem acrescentar informações:

    {texto}
    """

    resposta = cliente.interactions.create(
        model=MODELO,
        input=prompt,
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"voice": VOZ}
            ]
        },
    )

    audio_pcm = base64.b64decode(resposta.output_audio.data)
    salvar_wav(ARQUIVO_VOZ, audio_pcm)

    winsound.PlaySound(
        str(ARQUIVO_VOZ),
        winsound.SND_FILENAME,
    )


if __name__ == "__main__":
    falar(
        "Olá, Beatriz. A voz Iapetus foi escolhida como minha voz oficial."
    )