from pathlib import Path

from faster_whisper import WhisperModel


modelo = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)


def transcrever_audio(caminho_audio):
    caminho_audio = Path(caminho_audio)

    if not caminho_audio.exists():
        raise FileNotFoundError(f"Áudio não encontrado: {caminho_audio}")

    segmentos, _ = modelo.transcribe(
        str(caminho_audio),
        language="pt",
        beam_size=5,
    )

    texto = " ".join(
        segmento.text.strip()
        for segmento in segmentos
    )

    return texto.strip()


if __name__ == "__main__":
    arquivo_teste = Path(__file__).parent / "gravacao_teste.wav"

    print("Transcrevendo áudio...")
    resultado = transcrever_audio(arquivo_teste)

    print("Texto reconhecido:")
    print(resultado)