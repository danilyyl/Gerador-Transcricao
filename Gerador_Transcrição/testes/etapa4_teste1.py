import yt_dlp

def baixar_audio(link_youtube):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio_extraido.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Baixando áudio de: {link_youtube}")
        ydl.download([link_youtube])
        print("Download concluído!")

# Link de teste (você pode trocar por qualquer um depois)
link = "https://youtu.be/GEaxKNRtUG4?si=BQ5N5yVNzTw1byxE"
baixar_audio(link)


