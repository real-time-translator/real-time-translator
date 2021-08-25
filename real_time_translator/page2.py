import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from translator import translat_str
from translate import Translator

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page2(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.extracted_text=None
        self.user_input = StringVar()
        self.text_entry=Entry(self,textvariable=self.user_input)
        self.text_entry.place(x=300,y = 200 ,height = 20,width = 450)

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
        self.label_lan1= tk.Label(self,text="Select a language").grid(row = 0, column = 1)
        self.lan1menu.grid(row = 1, column =1)
        self.lan2menu = OptionMenu( self, self.lan2, *self.choices)
        self.label_lan2= tk.Label(self,text="Select a language").grid(row = 0, column = 2)
        self.lan2menu.grid(row = 1, column =2)

        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate)
        self.trans_btn.place(x = 450, y= 250 )

        self.show_label = Label(self,text=self.extracted_text)
        self.label_translated = tk.Label(self)


    def translate(self):
        self.extracted_text=self.user_input.get()
        print(self.extracted_text)

        self.label_translated.destroy()
        translator = Translator( from_lang=self.lan1.get(),to_lang=self.lan2.get())
        self.translation = translator.translate(self.extracted_text)
        print(self.translation)
        self.label_translated = Label(self,text=self.translation)
        self.label_translated.place(x=300,y = 300, height = 75,width = 450)
        