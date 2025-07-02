import subprocess
from pydub import AudioSegment, effects
from datetime import datetime
import whisper
import os
import yt_dlp

#Função que extrai áudio de vídeo local usando FFmpeg
def extrair_audio_local(caminho_video, nome_audio_saida="audio_local.wav"):
    print("Extraindo áudio do vídeo local com ffmpeg...")
    try:
        subprocess.run([
            "ffmpeg",
            "-i", caminho_video,
            "-vn",  # sem vídeo
            "-acodec", "pcm_s16le",  # formato WAV
            "-ar", "44100",  # taxa de amostragem
            "-ac", "2",  # estéreo
            nome_audio_saida
        ], check=True)
    except subprocess.CalledProcessError:
        print("Erro ao extrair áudio com ffmpeg.")
    return nome_audio_saida

#Função que baixa áudio de vídeo do YouTube
def baixar_audio_youtube(link_youtube, nome_audio_saida="audio_youtube.wav"):
    print("⬇ Baixando áudio do YouTube...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link_youtube])

    #Renomeia o arquivo baixado
    for arquivo in os.listdir():
        if arquivo.startswith("temp_audio") and arquivo.endswith(".wav"):
            os.rename(arquivo, nome_audio_saida)
            break

    return nome_audio_saida

#Função para limpar e normalizar o áudio
def limpar_audio(caminho_audio, nome_limpo_saida="audio_limpo.wav"):
    print("Limpando áudio...")
    audio = AudioSegment.from_file(caminho_audio)
    audio = effects.normalize(audio)
    audio.export(nome_limpo_saida, format="wav")
    return nome_limpo_saida

#Função para transcrever o áudio com Whisper
def transcrever_audio(caminho_audio):
    print("Transcrevendo com Whisper...")
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(caminho_audio)
    return resultado["text"]

#Função para salvar a transcrição como .txt
def salvar_transcricao(texto, origem="local"):
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"transcricao_{origem}_{agora}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
    print(f"Transcrição salva com sucesso: {nome_arquivo}")

#Função principal do sistema
def gerar_transcricao():
    print("\nGERADOR DE TRANSCRIÇÃO DE VÍDEOS")
    print("1. Transcrever vídeo local")
    print("2. Transcrever vídeo do YouTube")
    escolha = input("Escolha uma opção (1 ou 2): ")

    if escolha == "1":
        caminho_video = input("Digite o caminho do vídeo local (ex: C:/meu_video.mp4): ").strip('" ')
        audio_extraido = extrair_audio_local(caminho_video)
        audio_limpo = limpar_audio(audio_extraido)
        texto = transcrever_audio(audio_limpo)
        salvar_transcricao(texto, origem="local")

    elif escolha == "2":
        link = input("Cole o link do vídeo do YouTube: ").strip()
        audio_baixado = baixar_audio_youtube(link)
        audio_limpo = limpar_audio(audio_baixado)
        texto = transcrever_audio(audio_limpo)
        salvar_transcricao(texto, origem="youtube")

    else:
        print("Opção inválida. Tente novamente.")

#Executar se for o programa principal
if __name__ == "__main__":
    gerar_transcricao()