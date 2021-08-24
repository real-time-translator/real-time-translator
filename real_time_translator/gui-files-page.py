import os
from input_text import input_text_file
from input_image import imagetotext
from input_voice import transcript_from_file
# from edit_text import edit_text
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile ,askopenfilename
from tkinter import filedialog
from translator import *
from googletrans import Translator

root = Tk()
root.geometry('1050x400')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Real-Time-Translator')

extracted_text=None
edit_text=None

# def translate():
#     # Initial
#     translator = googletrans.Translator()
#     # Basic Translate
#     translation = translator.translate("sara", dest="ar")
#     translated = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
#     print(translated)
#
#     # with open('abc.txt',mode ='w') as file:
#     #         file.write(translated)
#
#     return translated


def ask_for_image():
    file_path = filedialog.askopenfile(   title="Choose a file",
    filetypes=[
               ('image files', '.png'),
               ('image files', '.jpg'),
               ('image files', '.jpeg'),
           ])
    extracted_text = imagetotext(file_path.name)
    show_answer(extracted_text)

def ask_for_text():
    global extracted_text
    file_path = filedialog.askopenfile(   title="Choose a file",
    filetypes=[
               ('text files', '.txt'),
              ])
    extracted_text = input_text_file(file_path.name)
    # print (extracted_text)
    show_answer(extracted_text)

def ask_for_audio():
    file_path = filedialog.askopenfile(   title="Choose a file",
    filetypes=[
               ('audio', '.wav'),
               ('audio', '.mp3'),
           ])
    extracted_text = transcript_from_file(file_path.name)
    show_answer(extracted_text)


def show_answer(extracted_text):
    # Input_text = Entry(root)
    # text=Entry(root,  text = "%s" %(Input_text) )
    # text  = Label(root, text=extracted_text)
    label = Label(text=extracted_text)
    label .place(x=300,y = 160 ,height = 75,width = 450)

    # text.place(x=300,y = 160 ,height = 75,width = 450)
    # text.insert(END,extracted_text)
    print(extracted_text)

def ask_for_edit():
    # extracted= Entry(root)
    # box=Entry(root,text=extracted_text)
    # box.insert(END,str(extracted_text))
    # box.place(x=300,y = 160 ,height = 75,width = 450)
    # user_input = StringVar()
    global extracted_text
    box=Entry(textvariable=extracted_text)
    box.insert(END,extracted_text)
    box.place(x=300,y = 160 ,height = 75,width = 450)
    submit_button=Button(root,text="Submit ",command=ask_for_submit)
    submit_button.place(x = 800, y= 190 )
    # submit_button=Button(text=" Submit ",command=handle_submiting)
    # submit_button.place(x=20,y=150)

def ask_for_submit():
    # pass
    global extracted_text
    
    print(extracted_text)
    
    label  = Label( text=extracted_text)
    label.place(x=300,y = 160 ,height = 75,width = 450)
    label .destroy()
    submit_button.destroy()
    box.destroy()


#         Input_text = Entry(root)
#
#         text=Entry(root,  text = "%s" %(Input_text) )
#
#         text.insert(END,extracted_text)
#         text.place(x=130,y=150)
#
#         submit_button=root.Button(text=" Submit ",command=handle_submiting)
#         submit_button.place(x=20,y=150)
#
#         button_record=root.Button(text="Start Recording",command=handle_record)
#         button_record.place(x=130,y=30)

    
            

adharbtn = Button(root,text ='Choose a picture',command = lambda:ask_for_image()) 
adharbtn.place(x=250,y = 120)

dlbtn = Button(root,text ='Choose a text ',command = lambda:ask_for_text()) 
dlbtn.place(x=450,y = 120)

msbtn = Button(root,text ='Choose an audio',command = lambda:ask_for_audio()) 
msbtn.place(x=650,y = 120)


trans_btn = Button(root, text = 'Edit',command = ask_for_edit)
trans_btn.place(x = 800, y= 190 )

# Input_text = Entry(root)
# Input_text = Text(root, height = 5, wrap = WORD, padx=5, pady=5, width = 60)
# Input_text.place(x=300,y = 160)


# trans_btn = Button(root, text = 'Translate',command = translate())
# trans_btn.place(x = 450, y= 250 )

Input_text2 = Text(root, height = 5, wrap = WORD, padx=5, pady=5, width = 60)
Input_text2.place(x=300,y = 300)


root.mainloop()


# trans_btn = tk.Button( text = 'Edit Text',font = 'arial 12 bold',pady = 5,command = input , bg = 'blue', activebackground = 'sky blue')
# trans_btn.place(x = 800, y= 190 )
# Input_text = Text(font = 'arial 10', height = 5, wrap = WORD, padx=5, pady=5, width = 60)
# Input_text.place(x=300,y = 160)
# # #Import the image using PhotoImage function
# # click_btn= imagetotext(file='clickme.png')
# # #Let us create a label for tk.button event
# # img_label= Label(image=click_btn)
# # #Let us create a dummy button and pass the image
# # button= Button(win, image=click_btn,command= my_command,
# # borderwidth=0)
# # button.pack(pady=30)

