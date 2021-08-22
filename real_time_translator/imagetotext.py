# import the following libraries
# will convert the image to text string
# import googletrans
import re
import googletrans
import pytesseract      
  
# adds image processing capabilities
from PIL import Image   

def imagetotext():
    imageFileName = input("enter the name of the image file: ")
        
    # opening an image from the source path
    img = Image.open(imageFileName)     

    # describes image format in the output
    print(img)                          
    
    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(imageFileName) 

    # write text in a text file and save it to source path   
    with open('abc.txt',mode ='w') as file:     
        
                    file.write(result)
                    print(result)

    # print(googletrans.LANGUAGES)

    # Initial
    translator = googletrans.Translator()

    # Basic Translate
    results = translator.translate(result,dest="ar")

    with open('abc.txt',mode ='w') as file:     
        
                    x=file.write(results.text)
    return results.text

if __name__ == "__main__":
    print(imagetotext())
