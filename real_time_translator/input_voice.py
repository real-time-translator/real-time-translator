from typing import Text
import speech_recognition as sr
import audiomath as am
import ffmpeg
import subprocess
import os
r = sr.Recognizer()


def transcript_from_file(file:str)->str:
    # convert the mp3 file to wav 
    if file.endswith('.mp3'):
      try:
        os.remove('assets/voices/file_converted.wav')
      except:
        pass
      subprocess.call(['ffmpeg', '-i', file,
                'assets/voices/file_converted.wav'])
        #save Audio  in file 
      file='assets/voices/file_converted.wav'

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
  # s.Write('assets/voices/file.wav')
  # file='assets/voices/file.wav'

  # These two lines for Yahia because he is using pyCharm
  s.Write(r'\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\voices\file.wav')
  file=r'\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\voices\file.wav'

  # Transcript form the File
  text=transcript_from_file(file)
  print(text)
  return(text)
  
if __name__ == '__main__':
  file='source/audio_files_harvard.wav'
  # print(transcript_from_file('assets/voices/How to Give Welcome Remarks.mp3'))
  print(transcript_from_record())

