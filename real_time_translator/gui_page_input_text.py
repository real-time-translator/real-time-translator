import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from googletrans import Translator 

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # The line bellow if you are using pyCharm, but you need to change the path
        # logo = tk.PhotoImage(file=r"\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\images\dictionary2.2.png")

        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)
    def show(self):
        self.lift()

class Page2(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.extracted_text=None
        self.user_input = StringVar()
        self.text_entry=Entry(self,textvariable=self.user_input)
        self.text_entry.place(x=300,y = 200 ,height = 20,width = 450)

        
        self.selected_language = tk.StringVar() 
        self.languages_menu = Combobox(self, width = 20, textvariable = self.selected_language, state='readonly',font=("Arial", 15)) 
        self.languages_menu['values'] = (
                                'Afrikaans',
                                'Albanian',
                                'Arabic',
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
                                'English',
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
                                'Haitian Creole',
                                'Hausa',
                                'Hawaiian',
                                'Hebrew',
                                'Hindi',
                                'Hmong',
                                'Hungarian',
                                'Icelandic',
                                'Igbo',
                                'Indonesian',
                                'Irish',
                                'Italian',
                                'Japanese',
                                'Javanese',
                                'Kannada',
                                'Kazakh',
                                'Khmer',
                                'Kinyarwanda',
                                'Korean',
                                'Kurdish',
                                'Kyrgyz',
                                'Lao',
                                'Latin',
                                'Latvian',
                                'Lithuanian',
                                'Luxembourgish',
                                'Macedonian',
                                'Malagasy',
                                'Malay',
                                'Malayalam',
                                'Maltese',
                                'Maori',
                                'Marathi',
                                'Mongolian',
                                'Myanmar',
                                'Nepali',
                                'Norwegian'
                                'Odia',
                                'Pashto',
                                'Persian',
                                'Polish',
                                'Portuguese',
                                'Punjabi',
                                'Romanian',
                                'Russian',
                                'Samoan',
                                'Scots Gaelic',
                                'Serbian',
                                'Sesotho',
                                'Shona',
                                'Sindhi',
                                'Sinhala',
                                'Slovak',
                                'Slovenian',
                                'Somali',
                                'Spanish',
                                'Sundanese',
                                'Swahili',
                                'Swedish',
                                'Tajik',
                                'Tamil',
                                'Tatar',
                                'Telugu',
                                'Thai',
                                'Turkish',
                                'Turkmen',
                                'Ukrainian',
                                'Urdu',
                                'Uyghur',
                                'Uzbek',
                                'Vietnamese',
                                'Welsh',
                                'Xhosa'
                                'Yiddish',
                                'Yoruba',
                                'Zulu',
                                ) 
        self.languages_menu.place(x= 405, y=150)
        self.languages_menu.current(0) 


        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate,fg="white",bg="black",font=("Arial", 15))
        self.trans_btn.place(x = 450, y= 250 )

        self.show_label = Label(self,text=self.extracted_text)
        self.label_translated = tk.Label(self)


    def translate(self):
        self.extracted_text=self.user_input.get()
        print(self.extracted_text)
        self.label_translated.destroy()
        translator = Translator()
        self.translation = translator.translate(self.extracted_text, self.selected_language.get()).text
        print(self.translation)
        self.label_translated = Label(self,text=self.translation)
        self.label_translated.place(x=50,y = 370, height = 75,width = 350)
        