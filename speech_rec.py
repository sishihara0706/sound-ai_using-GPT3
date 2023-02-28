import speech_recognition as sr
import sys
from input_audio import input_audio
import pyttsx3


engine = pyttsx3.init()
# engine.say("{音声読み上げライブラリ I am a student.}")
arg1 = sys.argv[1]

engine.say(f"私はあなたが言ったことをそのまま返すおうむ返し音声ボットです。recording startの文字が出たら")
engine.say(f"{arg1}秒間で適当に喋ってみてください。")
engine.runAndWait()

input_audio(int(arg1))

# input_audio_file =  f"./audio{sys.argv[1]}.wav" 
input_audio_file =  f"./output.wav" 
 
recognizer = sr.Recognizer()
 
with sr.AudioFile(input_audio_file) as source:
    audio = recognizer.record(source)
 
recognition_result = recognizer.recognize_google(audio, language='ja-JP')
print(recognition_result)

engine = pyttsx3.init()
# engine.say("{音声読み上げライブラリ I am a student.}")
engine.say(f"{recognition_result}…と言いましたね？")
engine.runAndWait()
