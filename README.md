# 🎧 Gerador de Transcrição de Vídeos com Python e Whisper

Este projeto permite **extrair áudio de vídeos locais ou do YouTube**, limpar esse áudio, e **gerar automaticamente uma transcrição em texto** utilizando o modelo de inteligência artificial Whisper da OpenAI.

Desenvolvido com foco em praticar:
- Manipulação de áudio e vídeo
- Uso de bibliotecas modernas de Python
- Aplicação de IA (Whisper)
- Automatização de tarefas via terminal

---

## 🚀 Funcionalidades

✅ Transcrição de vídeos locais (`.mp4`, `.avi`, etc.)  
✅ Transcrição de vídeos do YouTube  
✅ Extração e limpeza de áudio com `ffmpeg` e `pydub`  
✅ Geração de arquivo `.txt` com o conteúdo transcrito  
✅ Interface simples via terminal

---

## 🛠️ Tecnologias e bibliotecas utilizadas

- Python 3.13 (global, instalado no sistema)
- [FFmpeg](https://ffmpeg.org/)
- [`pydub`](https://github.com/jiaaro/pydub)
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- [`whisper`](https://github.com/openai/whisper)
- [`ffmpeg-python`](https://github.com/kkroening/ffmpeg-python)

---

## ⚙️ Como usar

### 1. Instale o FFmpeg no seu sistema

- [Download do FFmpeg](https://ffmpeg.org/download.html)
- Após instalar, adicione `ffmpeg` ao **Path** do Windows.

### 2. Instale as dependências Python

Abra o terminal e execute:

pip install moviepy pydub yt-dlp ffmpeg-python
pip install git+https://github.com/openai/whisper.git

### 3. Executar o projeto

Navegue até a pasta onde está o codigoPTBR.py e execute:

python codigoPTBR.py
