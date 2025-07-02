from gtts import gTTS
from pydub import AudioSegment

#texto que vai transformar em audio

texto = "Olá, isso é um teste"

#Cria o arquivo mp3 usando o gtts
tts = gTTS(texto, lang='pt')
tts.save("audio.mp3") #Salva o audio em MP3

#Converte o mp3 para o wav com o pydub
audio = AudioSegment.from_mp3("audio.mp3")
audio.export("audio.wav", format="wav") #Salva como wav

print("Audio wav gerado com sucesso!")