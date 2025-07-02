from pydub import AudioSegment
from pydub.effects import normalize
import whisper

#CARREGAR E LIMPAR O ÁUDIO
def limpar_audio(caminho_audio, caminho_limpo):
    audio = AudioSegment.from_file(caminho_audio, format="wav")

    # Normalização de volume (opcional mas útil)
    audio = normalize(audio)

    # Exporta o áudio limpo
    audio.export(caminho_limpo, format="wav")
    print(f"Áudio limpo salvo em: {caminho_limpo}")

#TRANSCRIÇÃO
def transcrever_audio(caminho_audio, caminho_txt):
    modelo = whisper.load_model("medium")
    resultado = modelo.transcribe(caminho_audio)

    texto = resultado["text"]
    print("Transcrição concluída!")

    # 3. SALVAR EM .TXT
    with open(caminho_txt, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)
    print(f"Transcrição salva em: {caminho_txt}")

# CAMINHOS
entrada = "audio_extraido.wav"
limpo = "audio_limpo.wav"
saida_txt = "transcricao.txt"

# EXECUÇÃO
limpar_audio(entrada, limpo)
transcrever_audio(limpo, saida_txt)
