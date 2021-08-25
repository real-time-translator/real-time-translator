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
from translate import Translator


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # logo = tk.PhotoImage(file=r"\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\images\dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)
    def show(self):
        self.lift()

class Page3(Page):


    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.extracted_text=None
        self.user_input = StringVar()
        self.edit_box=Entry(self,textvariable=self.user_input)

        self.choices = {  'Afrikaans',
                        'Albanian',
                        'Arabic',
                        'English',
                        'Armenian',
                       ' Azerbaijani',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                       ' Catalan',
                        'Cebuano',
                        'Chichewa',
                        'Chinese',
                        'Corsican',
                        'Croatian',
                       ' Czech',
                        'Danish',
                        'Dutch', 
                        'Esperanto',
                        'Estonian',
                        'Filipino',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        # 'Haitian Creole',
                        # 'Hausa',
                        # 'Hawaiian',
                        # 'Hebrew',
                        # 'Hindi',
                        # 'Hmong',
                        # 'Hungarian',
                        # 'Icelandic',
                        # 'Igbo',
                        # 'Indonesian',
                        # 'Irish',
                        # 'Italian',
                        # 'Japanese',
                        # 'Javanese',
                        # 'Kannada',
                        # 'Kazakh',
                        # 'Khmer',
                        # 'Kinyarwanda',
                        # 'Korean',
                        # 'Kurdish',
                        # 'Kyrgyz',
                        # 'Lao',
                        # 'Latin',
                        # 'Latvian',
                        # 'Lithuanian',
                        # 'Luxembourgish',
                        # 'Macedonian',
                        # 'Malagasy',
                        # 'Malay',
                        # 'Malayalam',
                        # 'Maltese',
                        # 'Maori',
                        # 'Marathi',
                        # 'Mongolian',
                        # 'Myanmar',
                        # 'Nepali',
                        # 'Norwegian'
                        # 'Odia',
                        # 'Pashto',
                        # 'Persian',
                        # 'Polish',
                        # 'Portuguese',
                        # 'Punjabi',
                        # 'Romanian',
                        # 'Russian',
                        # 'Samoan',
                        # 'Scots Gaelic',
                        # 'Serbian',
                        # 'Sesotho',
                        # 'Shona',
                        # 'Sindhi',
                        # 'Sinhala',
                        # 'Slovak',
                        # 'Slovenian',
                        # 'Somali',
                        # 'Spanish',
                        # 'Sundanese',
                        # 'Swahili',
                        # 'Swedish',
                        # 'Tajik',
                        # 'Tamil',
                        # 'Tatar',
                        # 'Telugu',
                        # 'Thai',
                        # 'Turkish',
                        # 'Turkmen',
                        # 'Ukrainian',
                        # 'Urdu',
                        # 'Uyghur',
                        # 'Uzbek',
                        # 'Vietnamese',
                        # 'Welsh',
                        # 'Xhosa'
                        # 'Yiddish',
                        # 'Yoruba',
                        'Zulu',}

        self.lan1 = StringVar()
        self.lan2 = StringVar()
        self.lan1.set('English')
        self.lan2.set('Arabic')
        self.lan1menu = OptionMenu(self, self.lan1, *self.choices)
        self.label_lan1= tk.Label(self,text="Select a languages",fg="white",bg="black",font=("Arial", 15)).place(x= 300, y=70)
        self.lan1menu.place(x= 330, y=100)
        self.lan2menu = OptionMenu( self, self.lan2, *self.choices)
        self.label_lan2= tk.Label(self,text="Select a language",fg="white",bg="black",font=("Arial", 15)).place(x= 600, y=70)
        self.lan2menu.place(x= 630, y=100)

        self.submit_button = Button(self,text="Submit ",command=self.ask_for_submit)
        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit)
        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate , fg="white",bg="black",font=("Arial", 15),width=15,height=1)

        self.show_label = Label(self,text=self.extracted_text)
        self.label_translated = tk.Label(self)

        self.image_btn = tk.Button(self,text ='Choose a picture',command = lambda:self.ask_for_image(), fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.image_btn.place(x=200,y =20)
        self.text_btn = tk.Button(self,text ='Choose a text ',command = lambda:self.ask_for_text(), fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.text_btn.place(x=430,y =20)
        self.audio_btn = tk.Button(self,text ='Choose an audio',command = lambda:self.ask_for_audio(),fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.audio_btn.place(x=650,y =20)


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
        self.trans_btn.destroy()


        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit,fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.edit_btn.place(x = 800, y= 190 )
        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate,fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.trans_btn.place(x = 450, y= 250 )

        self.show_label = Label(self,text=self.extracted_text)
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
        self.trans_btn.destroy()
        self.label_translated.destroy()

        self.submit_button=Button(self,text="Submit ",command=self.ask_for_submit)
        self.submit_button.place(x = 800, y= 190 )

        self.edit_box=Entry(self,textvariable=self.user_input,font=("Arial", 15))
        self.edit_box.insert(END,self.extracted_text)
        self.edit_box.place(x=300,y = 200 ,height = 20,width = 450)

    def ask_for_submit(self):
        self.edit_box.destroy()
        self.submit_button.destroy()

        self.extracted_text=self.user_input.get()
        self.user_input.set("")
        print(self.extracted_text)

        self.image_btn = tk.Button(self,text ='Choose a picture',command = lambda:self.ask_for_image(),fg="white",bg="black",font=("Arial", 15),width=15,height=1) 
        self.image_btn.place(x=250,y = 20)
        self.text_btn = tk.Button(self,text ='Choose a text ',command = lambda:self.ask_for_text(), fg="white",bg="black",font=("Arial", 15),width=15,height=1) 
        self.text_btn.place(x=450,y = 20)
        self.audio_btn = tk.Button(self,text ='Choose an audio',command = lambda:self.ask_for_audio(),fg="white",bg="black",font=("Arial", 15),width=15,height=1) 
        self.audio_btn.place(x=650,y = 20)

        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit,fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.edit_btn.place(x = 800, y= 190 )
        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate,fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.trans_btn.place(x = 450, y= 250 )
        
        self.show_label = Label(self, text=self.extracted_text)
        self.show_label.place(x=300,y = 200 ,height = 20,width = 450)
        self.label_translated = Label(self,text=self.translation)
        self.label_translated.place(x=300,y = 300, height = 75,width = 450)

    def translate(self):
        self.label_translated.destroy()
        translator = Translator( from_lang=self.lan1.get(),to_lang=self.lan2.get())
        self.translation = translator.translate(self.extracted_text)
        print(self.translation)
        self.label_translated = Label(self,text=self.translation)
        self.label_translated.place(x=50,y = 370, height = 75,width = 350)


# if __name__ == "__main__":
#     root= tk.Tk()
#     root.mainloop()