import wave
from pathlib import Path

import sounddevice as sd


def gravar_audio(
    caminho_audio,
    duracao=10,
    taxa_amostragem=44100,
    canais=1,
):
    caminho_audio = Path(caminho_audio)
    caminho_audio.parent.mkdir(parents=True, exist_ok=True)

    print("Gravação iniciada. Fale alguma coisa...")

    audio = sd.rec(
        int(duracao * taxa_amostragem),
        samplerate=taxa_amostragem,
        channels=canais,
        dtype="int16",
    )

    sd.wait()

    with wave.open(str(caminho_audio), "wb") as arquivo_wav:
        arquivo_wav.setnchannels(canais)
        arquivo_wav.setsampwidth(2)
        arquivo_wav.setframerate(taxa_amostragem)
        arquivo_wav.writeframes(audio.tobytes())

    print(f"Gravação concluída: {caminho_audio}")
    return caminho_audio


if __name__ == "__main__":
    arquivo_teste = Path(__file__).parent / "gravacao_teste.wav"
    gravar_audio(arquivo_teste)