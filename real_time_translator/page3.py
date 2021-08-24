import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile, askopenfilename
from tkinter import filedialog
import os
from translator import translat_str

from input_text import input_text_file
from input_image import imagetotext
from input_voice import transcript_from_file

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.extracted_text=None
        self.user_input = StringVar()
        self.edit_box=Entry(self,textvariable=self.user_input)
        self.submit_button=Button(self,text="Submit ",command=self.ask_for_submit)
        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit)
        self.show_label = Label(text=self.extracted_text)

        self.image_btn = tk.Button(self,text ='Choose a picture',command = lambda:self.ask_for_image()) 
        self.image_btn.place(x=250,y = 120)

        self.text_btn = tk.Button(self,text ='Choose a text ',command = lambda:self.ask_for_text()) 
        self.text_btn.place(x=450,y = 120)

        self.audio_btn = tk.Button(self,text ='Choose an audio',command = lambda:self.ask_for_audio()) 
        self.audio_btn.place(x=650,y = 120)


    def ask_for_image(self):
        file_path = filedialog.askopenfile(   title="Choose a file",
        filetypes=[('image files', '.png'),('image files', '.jpg'),('image files', '.jpeg')])
        self.extracted_text =''
        self.extracted_text = imagetotext(file_path.name)
        self.show_answer()

    def ask_for_text(self):
        file_path = filedialog.askopenfile(   title="Choose a file",
        filetypes=[('text files', '.txt')])
        self.extracted_text =''
        self.extracted_text = input_text_file(file_path.name)
        self.show_answer()

    def ask_for_audio(self):
        file_path = filedialog.askopenfile(title="Choose a file",
        filetypes=[('audio', '.wav'),('audio', '.mp3')])
        self.extracted_text =''
        self.extracted_text = transcript_from_file(file_path.name)
        self.show_answer()

    def show_answer(self):
        self.edit_btn.destroy()
        self.show_label.destroy()
        self.edit_box.destroy()
        self.submit_button.destroy()
        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit)
        self.edit_btn.place(x = 800, y= 190 )
        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate)
        self.trans_btn.place(x = 450, y= 250 )

        self.show_label = Label(text=self.extracted_text)
        self.show_label.place(x=300,y = 200 ,height = 20,width = 450)
        print(self.extracted_text)

    def ask_for_edit(self):
        self.image_btn.destroy()
        self.text_btn.destroy()
        self.audio_btn.destroy()
        self.edit_btn.destroy()
        self.show_label.destroy()
        self.edit_box.destroy()
        self.submit_button.destroy()

        self.submit_button=Button(self,text="Submit ",command=self.ask_for_submit)
        self.submit_button.place(x = 800, y= 190 )
        self.edit_box=Entry(self,textvariable=self.user_input)
        self.edit_box.insert(END,self.extracted_text)
        self.edit_box.place(x=300,y = 200 ,height = 20,width = 450)

    def ask_for_submit(self):
        self.edit_box.destroy()
        self.submit_button.destroy()

        self.extracted_text=self.user_input.get()
        self.user_input.set("")
        print(self.extracted_text)

        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit)
        self.edit_btn.place(x = 800, y= 190 )
        self.show_label = Label( text=self.extracted_text)
        self.show_label.place(x=300,y = 200 ,height = 20,width = 450)
        self.image_btn = tk.Button(self,text ='Choose a picture',command = lambda:self.ask_for_image()) 
        self.image_btn.place(x=250,y = 120)
        self.text_btn = tk.Button(self,text ='Choose a text ',command = lambda:self.ask_for_text()) 
        self.text_btn.place(x=450,y = 120)
        self.audio_btn = tk.Button(self,text ='Choose an audio',command = lambda:self.ask_for_audio()) 
        self.audio_btn.place(x=650,y = 120)

    def translate(self):
        translated_text = translat_str(self.extracted_text)
        print(translated_text)
        label_translated = Label(self,text=translated_text)
        label_translated.place(x=300,y = 300, height = 75,width = 450)



# if __name__ == "__main__":
#     root= tk.Tk()
#     root.mainloop()