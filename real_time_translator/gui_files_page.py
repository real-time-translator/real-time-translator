# import os
# from input_text import input_text_file
# from input_image import imagetotext
# from input_voice import transcript_from_file
# from tkinter import *
# from tkinter.ttk import *
# from tkinter.filedialog import askopenfile, askopenfilename
# from tkinter import filedialog
# from translator import translat_str

root = Tk()
root.geometry('1050x400')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Real-Time-Translator')
# extracted_text=None
# user_input = StringVar()

# def ask_for_image():
#     global extracted_text
#     file_path = filedialog.askopenfile(   title="Choose a file",
#     filetypes=[
#                ('image files', '.png'),
#                ('image files', '.jpg'),
#                ('image files', '.jpeg'),
#            ])
#     extracted_text = imagetotext(file_path.name)
#     show_answer(extracted_text)
#
# def ask_for_text():
#     global extracted_text
#     file_path = filedialog.askopenfile(   title="Choose a file",
#     filetypes=[
#                ('text files', '.txt'),
#               ])
#     extracted_text = input_text_file(file_path.name)
#     show_answer(extracted_text)
#
# def ask_for_audio():
#     global extracted_text
#     file_path = filedialog.askopenfile(   title="Choose a file",
#     filetypes=[
#                ('audio', '.wav'),
#                ('audio', '.mp3'),
#            ])
#     extracted_text = transcript_from_file(file_path.name)
#     show_answer(extracted_text)
#
# def show_answer(extracted_text):
#     label = Label(text=extracted_text)
#     label .place(x=300,y = 160 ,height = 75,width = 450)
#     print(extracted_text)

# def ask_for_edit():
#     global extracted_text, user_input
#     box=Entry(root,textvariable=user_input)
#     box.insert(END,extracted_text)
#     box.place(x=300,y = 160 ,height = 75,width = 450)
#
#     def ask_for_submit():
#         global extracted_text, user_input
#         extracted_text=user_input.get()
#         user_input.set("")
#         print(extracted_text)
#         label  = Label( text=extracted_text)
#         label.place(x=300,y = 160 ,height = 75,width = 450)
#         submit_button.destroy()
#     submit_button=Button(root,text="Submit ",command=ask_for_submit)
#     submit_button.place(x = 800, y= 190 )

# def translate():
#     global extracted_text
#     translated_text = translat_str(extracted_text)
#     print(translated_text)
#     label_translated = Label(root,text=translated_text)
#     label_translated.place(x=300,y = 300, height = 75,width = 450)


# adharbtn = Button(root,text ='Choose a picture',command = lambda:ask_for_image())
# adharbtn.place(x=250,y = 120)
#
# dlbtn = Button(root,text ='Choose a text ',command = lambda:ask_for_text())
# dlbtn.place(x=450,y = 120)
#
# msbtn = Button(root,text ='Choose an audio',command = lambda:ask_for_audio())
# msbtn.place(x=650,y = 120)
#
# trans_btn = Button(root, text = 'Edit',command = ask_for_edit)
# trans_btn.place(x = 800, y= 190 )
#
# trans_btn = Button(root, text = 'Translate',command = translate)
# trans_btn.place(x = 450, y= 250 )


root.mainloop()