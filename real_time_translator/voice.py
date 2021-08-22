from typing import Text
import speech_recognition as sr
import audiomath as am
import ffmpeg
r = sr.Recognizer()


def transcript_from_file(file:str)->str:
    
    with sr.AudioFile(file) as source:
      # listen for the data (load audio to memory)
      audio_data = r.record(source)
      # recognize (convert from speech to text)
      text = r.recognize_google(audio_data)
      
    return(text)



def transcript_from_record():
  print("start talking ")
  # listen for the mice 
  s = am.Record(10) 
  # load audio to file
  s.Write('source/file.wav')
  file='source/file.wav'
  # Transcript form the File
  text=transcript_from_file(file)

  return(text)
  




  


if __name__ == '__main__':
  file='source/audio_files_harvard.wav'
  transcript_from_record()






