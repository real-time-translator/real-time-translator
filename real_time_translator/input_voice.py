from typing import Text
import speech_recognition as sr
import audiomath as am
import ffmpeg
import subprocess
import os
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
  # Transcript form the File
  text=transcript_from_file(file)
  return(text)


# def converter(src):
#   if src.endswith('.mp3'):
#     try:
#       dst= 'assets/voices/file_converted.wav'
#       sound = AudioSegment.from_mp3(src)
#       sound.export(dst, format="wav")
#       return dst
#     except:
#       print('Has Not converted ')

#   if src.endswith('.oga'):
#     try:
#       print('ok')
#       dst= 'assets/voices/file_converted.wav'
#       sound = AudioSegment.from_ogg(src)
#       sound.export(dst, format="wav")
#       return dst
#     except:
#       print('Has Not converted ')


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






