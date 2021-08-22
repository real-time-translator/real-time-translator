from typing import Text
import speech_recognition as sr
import audiomath as am
import ffmpeg
r = sr.Recognizer()


def transcript_from_file(file:str)->str:
    # select the language you want to translate to 
    with sr.AudioFile(file) as source:
      # listen for the data (load audio to memory)
      audio_data = r.record(source)
      # recognize (convert from speech to text)
      text = r.recognize_google(audio_data)
      
    return(text)



def transcript_from_record():
  print("start talking ")

  s = am.Record(10) 
  s.Write('source/file.wav')
  file='source/file.wav'
  text=transcript_from_file(file)
  print(text)
  
  # translate_from_file(file,'ar')



  


if __name__ == '__main__':
  file='source/audio_files_harvard.wav'
  transcript_from_record()






