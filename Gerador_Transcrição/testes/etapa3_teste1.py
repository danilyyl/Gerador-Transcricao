import whisper

#Carrega o modelo base do whisper
modelo = whisper.load_model("base")

#Caminho para o arquivo de audio
caminho_audio = r"C:\Users\danie\OneDrive\Desktop\Gerador\audio.wav"

#Transcreve o audio
resultado = modelo.transcribe(caminho_audio)

#Imprime a transcrição
print("Transcrição do audio:")
print(resultado["text"])