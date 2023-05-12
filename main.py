# importando a biblioteca
import speech_recognition as sr
from audioConverter import convert_ogg_to_wav

convert_ogg_to_wav('audio/audio.ogg')
# instanciando e limitando o threshold
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

# vamos guardar nosso áudio em uma varíavel com o mesmo nome
audio = sr.AudioFile('./audio/audio.wav')

with audio as source:
    audio = recognizer.record(source)
    translate = recognizer.recognize_google(audio_data=audio, language="pt-BR")
    print(translate)
