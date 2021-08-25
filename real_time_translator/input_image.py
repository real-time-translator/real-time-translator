import pytesseract

# This lines for Yahia because he is using pyCharm
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# adds image processing capabilities
from PIL import Image   

def imagetotext(imageFileName):
    # opening an image from the source path
    img = Image.open(imageFileName)

    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(imageFileName)

    # write text in a text file and save it to source path
    # with open('abc.txt',mode ='w') as file:
    #     file.write(result)
    return str(result)

if __name__ == "__main__":
    imageFileName = input("enter the name of the image file: ")
    print(imagetotext(imageFileName))
