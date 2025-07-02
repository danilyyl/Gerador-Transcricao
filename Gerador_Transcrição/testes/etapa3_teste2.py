from pydub import AudioSegment
from pydub.effects import normalize, strip_silence
import whisper

# Caminho para o áudio original
caminho_audio_original = r"C:\Users\danie\OneDrive\Desktop\Gerador\audio.wav"
caminho_audio_limpo = r"C:\Users\danie\OneDrive\Desktop\Gerador\audio_limpo.wav"

# 1. Carrega o áudio original
audio = AudioSegment.from_file(caminho_audio_original, format="wav")

# 2. Normaliza o volume
audio_normalizado = normalize(audio)

# 3. Remove silêncios (início/fim) e aumenta volume
audio_sem_silencio = strip_silence(audio_normalizado, silence_len=100, silence_thresh=-40)
audio_limpo = audio_sem_silencio + 5  # Aumenta o volume em 5 dB

# 4. Exporta o áudio limpo
audio_limpo.export(caminho_audio_limpo, format="wav")

# 5. Transcreve com Whisper
modelo = whisper.load_model("base")
resultado = modelo.transcribe(caminho_audio_limpo)

# 6. Exibe o resultado
print("Transcrição do áudio limpo:")
print(resultado["text"])
