def input_text_manually():
    user_input = input('Type Your Text')
    return(user_input)

def input_text_file():
   
    user_input_path = input("paste your path's file")
    user_input_text = open(user_input_path , 'r') 
    return user_input_text.read()


if __name__ == '__main__':
    input_text_manually()
    print(input_text_file())

from pyautogui import typewrite

print("enter folder name: ")
typewrite("Default Value")
folder = input()
print (folder) 
 