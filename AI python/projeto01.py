from gtts import gTTS

texto = "Workshop de Inteligência Artificial"
lingua = "pt"

tts = gTTS(texto, lang=lingua)
tts.save("audio.mp3")

import os
os.system('ffplay -autoexit -nodisp audio.mp3')