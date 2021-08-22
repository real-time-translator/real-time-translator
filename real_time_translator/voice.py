import speech_recognition as sr
from translate import Translator
import audiomath as am
r = sr.Recognizer()


def translate_from_file(file:str,to_lang="en")->str:
    # select the language you want to translate to 
    translator= Translator(to_lang=to_lang)
    with sr.AudioFile(file) as source:
      # listen for the data (load audio to memory)
      audio_data = r.record(source)
      # recognize (convert from speech to text)
      text = r.recognize_google(audio_data)
      # translation = translator.translate("hallo meine Freunde")
      print(text)



def translate_from_record(to_lang="en"):
  print("start talking ")
  s = am.Record() 

if __name__ == '__main__':
  file='source/audio_files_harvard.wav'
  # translate_from_file(file,'ar')
  translate_from_record()