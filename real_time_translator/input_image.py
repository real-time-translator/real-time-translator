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

    return result

if __name__ == "__main__":
    imageFileName = input("enter the name of the image file: ")
    print(imagetotext(imageFileName))
