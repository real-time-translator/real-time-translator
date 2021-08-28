def input_text_manually():
    user_input = input('Type Your Text')

    return(user_input)

def input_text_file(path):
    print(path)
    user_input_text = open(path , 'r')
    return str(user_input_text.read())

# if __name__ == '__main__':
#     # input_text_manually()
#     # print(input_text_file())
#     print(input_text_file('assets/input_text/input.txt'))
