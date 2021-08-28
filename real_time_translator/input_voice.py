import speech_recognition as sr
import audiomath as am
from pydub import AudioSegment

r = sr.Recognizer()


def transcript_from_file(file:str)->str:
   
    # convert the mp3 file to wav 
    if not file.endswith('.wav'):
      file=converterII(file)

    with sr.AudioFile(file) as source:
      # listen for the data (load audio to memory)
      audio_data = r.record(source)
      # recognize (convert from speech to text)
      text = r.recognize_google(audio_data)
   
    return(text)


def transcript_from_record():
  
  print("start talking ")
  # listen for the mice 
  s = am.Record(3)

  # load audio to file
  s.Write('assets/voices/file.wav')
  file='assets/voices/file.wav'

  # The two lines bellow if you are using pyCharm, but you need to change the path
  # s.Write(r'\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\voices\file.wav')
  # file=r'\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\voices\file.wav'


  # Transcript form the File
  text=transcript_from_file(file)
  return(text)


def converterII(src):
  sound = AudioSegment.from_file(src)
  sound.export("assets/voices/file.wav", format="wav", bitrate="128k")
  return "assets/voices/file.wav"

if __name__ == '__main__':
  # file='source/audio_files_harvard.wav'
  # print(transcript_from_file('file_5.oga'))
  converterII("file_12.opus")
  pass
  # print(transcript_from_record())






