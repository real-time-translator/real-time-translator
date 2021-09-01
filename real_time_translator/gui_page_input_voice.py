import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from input_voice import transcript_from_record
from googletrans import Translator 

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # The line bellow if you are using pyCharm, but you need to change the path
        # logo = tk.PhotoImage(file=r"\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\images\dictionary2.2.png")

        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

        self.extracted_text=None
        self.user_input = StringVar()
        self.edit_box=Entry(self,textvariable=self.user_input)

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
        translator = Translator()
        self.translation = translator.translate(self.extracted_text, self.selected_language.get()).text
        print(self.translation)
        self.label_translated = Label(self,text=self.translation)
        self.label_translated.place(x=50,y = 370, height = 75,width = 350)


# if __name__ == "__main__":
#     root= tk.Tk()
    # root.mainloop()