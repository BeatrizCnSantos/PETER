from pathlib import Path

from voice.recorder import gravar_audio
from voice.transcriber import transcrever_audio


def ouvir(duracao=10):
    arquivo_audio = Path(__file__).parent / "entrada.wav"

    gravar_audio(arquivo_audio, duracao=duracao)

    print("Transcrevendo áudio...")
    texto = transcrever_audio(arquivo_audio)

    print("Texto reconhecido:")
    print(texto)

    return texto


if __name__ == "__main__":
    ouvir()