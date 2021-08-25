import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from translator import translat_str
from translate import Translator
from input_voice import transcript_from_record

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # logo = tk.PhotoImage(file=r"\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\images\dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

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
        self.lan1menu["menu"].config(fg="white",bg="black",font=("Arial", 15))
        self.lan1menu.pack()
        self.label_lan1= tk.Label(self,text="Select a language",fg="white",bg="black",font=("Arial", 15)).place(x= 300, y=110)
        self.lan1menu.place(x= 330, y=150)
        self.lan2menu = OptionMenu( self, self.lan2, *self.choices)
        self.lan2menu["menu"].config(fg="white",bg="black",font=("Arial", 15))
        self.lan2menu.pack()
        self.label_lan2= tk.Label(self,text="Select a language",fg="white",bg="black",font=("Arial", 15)).place(x= 600, y=110)
        self.lan2menu.place(x= 630, y=150)

        self.submit_btn = Button(self,text="Submit ",command=self.ask_for_submit)
        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit , fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate , fg="white",bg="black",font=("Arial", 15),width=15,height=1)

        self.show_label = Label(self,text=self.extracted_text)
        self.label_translated = tk.Label(self)

        self.record_btn=tk.Button(self,text="Start Recording",command=self.ask_for_record,fg="white",bg="black",font=("Arial", 15))
        self.record_btn.place(x=430,y =20)

    def ask_for_record(self):
        self.extracted_text=transcript_from_record()
        self.show_answer()

    def show_answer(self):
        self.edit_btn.destroy()
        self.show_label.destroy()
        self.edit_box.destroy()
        self.submit_btn.destroy()
        self.trans_btn.destroy()

        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit, fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.edit_btn.place(x = 800, y= 190 )
        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate, fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.trans_btn.place(x = 450, y= 250 )

        self.show_label = Label(self,text=self.extracted_text)
        self.show_label.place(x=300,y = 200 ,height = 20,width = 450)
        print(self.extracted_text)

    def ask_for_edit(self):
        self.record_btn.destroy()
        self.edit_btn.destroy()
        self.show_label.destroy()
        self.edit_box.destroy()
        self.submit_btn.destroy()
        self.trans_btn.destroy()
        self.label_translated.destroy()

        self.submit_btn=Button(self,text="Submit ",command=self.ask_for_submit)
        self.submit_btn.place(x = 800, y= 200 )

        self.edit_box=Entry(self,textvariable=self.user_input)
        self.edit_box.insert(END,self.extracted_text)
        self.edit_box.place(x=300,y = 200 ,height = 20,width = 450)

    def ask_for_submit(self):
        self.edit_box.destroy()
        self.submit_btn.destroy()

        self.record_btn=tk.Button(self,text="Start Recording",command=self.ask_for_record,fg="white",bg="black",font=("Arial", 15))
        self.record_btn.place(x=430,y =20)

        self.extracted_text=self.user_input.get()
        self.user_input.set("")
        print(self.extracted_text)

        self.edit_btn = tk.Button(self, text = 'Edit',command = self.ask_for_edit, fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.edit_btn.place(x = 800, y= 190 )
        self.trans_btn = tk.Button(self, text = 'Translate',command = self.translate,fg="white",bg="black",font=("Arial", 15),width=15,height=1)
        self.trans_btn.place(x = 450, y= 250 )

        self.show_label = Label(self, text=self.extracted_text)
        self.show_label.place(x=300,y = 200 ,height = 20,width = 450)
        self.label_translated = Label(self,text=self.translation)
        self.label_translated.place(x=50,y = 370, height = 75,width = 350)


    def translate(self):
        self.label_translated.destroy()
        translator = Translator( from_lang=self.lan1.get(),to_lang=self.lan2.get())
        self.translation = translator.translate(self.extracted_text)
        print(self.translation)
        self.label_translated = Label(self,text=self.translation)
        self.label_translated.place(x=50,y = 370, height = 75,width = 350)


# if __name__ == "__main__":
#     root= tk.Tk()
    # root.mainloop()