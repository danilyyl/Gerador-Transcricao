from moviepy import VideoFileClip
from pydub import AudioSegment, effects
import whisper
from datetime import datetime
import os

# Caminho do vídeo local
caminho_video = "meu_video.mp4"
arquivo_audio_extraido = "audio_local.wav"
arquivo_audio_limpo = "audio_local_limpo.wav"


# Etapa 1: Extrair áudio do vídeo local
print("Extraindo áudio do vídeo local...")
video = VideoFileClip(caminho_video)
video.audio.write_audiofile(arquivo_audio_extraido)


# Etapa 2: Limpar o áudio
print("Limpando o áudio extraído...")
audio = AudioSegment.from_file(arquivo_audio_extraido)
audio = effects.normalize(audio)
audio.export(arquivo_audio_limpo, format="wav")


# Etapa 3: Transcrever com Whisper
print("Transcrevendo com Whisper...")
modelo = whisper.load_model("base")
resultado = modelo.transcribe(arquivo_audio_limpo)


# Etapa 4: Salvar transcrição num .txt
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
arquivo_saida = f"transcricao_local_{agora}.txt"


with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write(resultado["text"])

print(f"Transcrição salva com sucesso: {arquivo_saida}")
