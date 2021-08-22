def input_text_manually():
    user_input = input('Type Your Text') #Change input to GUI
    return(user_input)

def input_text_file(path):
    user_input_text = open(path , 'r')
    return user_input_text.read()

if __name__ == '__main__':
    input_text_manually()
    print(input_text_file())
