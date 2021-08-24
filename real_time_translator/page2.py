import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page2(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # logo = tk.PhotoImage(file=r"\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\images\dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

        label = tk.Label(BGlabel, text="This is page 2")
        label.place(x=20, y=20)
        

#     #Translator function 
#     def translate(self):
     
#         self.translator= tk.Translator(self,from_lang=self.lan1.get(),to_lang=self.lan2.get())
#         self.translation = self.translator.translate(self.var.get())
#         self.var1.set(self.translation)


#         #variables for dropdown list
#         self.lan1 = tk.StringVar(self,root)
#         self.lan2 = tk.StringVar(self,root)

#             #choices to show in dropdown menu
#         self.choices = { 'English','Hindi','Arabic','Spanish','German'}
#         #default selection for dropdownlists
#         self.lan1.set('English')
#         self.lan2.set('Arabic')

#         #creating dropdown and arranging in the grid
#         self.lan1menu = tk.OptionMenu(self,self.mainframe, self.lan1, *self.choices)
#         tk.Label(self,self.mainframe,text="Select a language").grid(row = 0, column = 1)
#         self.lan1menu.grid(row = 1, column =1)

#         self.lan2menu = tk.OptionMenu( self,self.mainframe, self.lan2, *self.choices)
#         tk.Label(self,self.mainframe,text="Select a language").grid(row = 0, column = 2)
#         self.lan2menu.grid(row = 1, column =2)

#         #Text Box to take user input
#         tk.Label(self,self.mainframe, text = "Enter text").grid(row=2,column=0)
#         self.var = tk.StringVar(self)
#         self.textbox = tk.Entry(self,self.mainframe, textvariable=self.var).grid(row=2,column=1)

#         #textbox to show output
#         #label can also be used
#         tk.Label(self,self.mainframe, text = "Output").grid(row=2,column=2)
#         self.var1 = tk.StringVar(self)
#         self.textbox =tk.Entry(self,self.mainframe, textvariable=self.var1).grid(row=2,column=3)

#         #creating a button to call Translator function
#         self.b=tk.Button(self,self.mainframe,text='Translate',command=self.translate).grid(row=3,column=1,columnspan=3)


# if __name__ == "__main__":
#     root= tk.Tk()
#     root.title("Translator")
#     #Creating a Frame and Grid to hold the Content
#     mainframe = tk.Frame(root)
#     mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
#     mainframe.columnconfigure(0, weight = 1)
#     mainframe.rowconfigure(0, weight = 1)
#     mainframe.pack(pady = 100, padx = 100)
#     root.mainloop()

# from tkinter import *
# from translate import Translator
#
# #Translator function
# def translate():
#     translator= Translator(from_lang=lan1.get(),to_lang=lan2.get())
#     translation = translator.translate(var.get())
#     var1.set(translation)
#
# #Tkinter root Window with title
# root = Tk()
# root.title("Translator")
#
# #Creating a Frame and Grid to hold the Content
# mainframe = Frame(root)
# mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
# mainframe.columnconfigure(0, weight = 1)
# mainframe.rowconfigure(0, weight = 1)
# mainframe.pack(pady = 100, padx = 100)
#
# #variables for dropdown list
# lan1 = StringVar(root)
# lan2 = StringVar(root)
#
# #choices to show in dropdown menu
# choices = {  'Afrikaans',
#                         'Albanian',
#                         'Arabic',
#                         'Armenian',
#                        ' Azerbaijani',
#                         'Basque',
#                         'Belarusian',
#                         'Bengali',
#                         'Bosnian',
#                         'Bulgarian',
#                        ' Catalan',
#                         'Cebuano',
#                         'Chichewa',
#                         'Chinese',
#                         'Corsican',
#                         'Croatian',
#                        ' Czech',
#                         'Danish',
#                         'Dutch',
#                         'English',
#                         'Esperanto',
#                         'Estonian',
#                         'Filipino',
#                         'Finnish',
#                         'French',
#                         'Frisian',
#                         'Galician',
#                         'Georgian',
#                         'German',
#                         'Greek',
#                         'Gujarati',
#                         'Haitian Creole',
#                         'Hausa',
#                         'Hawaiian',
#                         'Hebrew',
#                         'Hindi',
#                         'Hmong',
#                         'Hungarian',
#                         'Icelandic',
#                         'Igbo',
#                         'Indonesian',
#                         'Irish',
#                         'Italian',
#                         'Japanese',
#                         'Javanese',
#                         'Kannada',
#                         'Kazakh',
#                         'Khmer',
#                         'Kinyarwanda',
#                         'Korean',
#                         'Kurdish',
#                         'Kyrgyz',
#                         'Lao',
#                         'Latin',
#                         'Latvian',
#                         'Lithuanian',
#                         'Luxembourgish',
#                         'Macedonian',
#                         'Malagasy',
#                         'Malay',
#                         'Malayalam',
#                         'Maltese',
#                         'Maori',
#                         'Marathi',
#                         'Mongolian',
#                         'Myanmar',
#                         'Nepali',
#                         'Norwegian'
#                         'Odia',
#                         'Pashto',
#                         'Persian',
#                         'Polish',
#                         'Portuguese',
#                         'Punjabi',
#                         'Romanian',
#                         'Russian',
#                         'Samoan',
#                         'Scots Gaelic',
#                         'Serbian',
#                         'Sesotho',
#                         'Shona',
#                         'Sindhi',
#                         'Sinhala',
#                         'Slovak',
#                         'Slovenian',
#                         'Somali',
#                         'Spanish',
#                         'Sundanese',
#                         'Swahili',
#                         'Swedish',
#                         'Tajik',
#                         'Tamil',
#                         'Tatar',
#                         'Telugu',
#                         'Thai',
#                         'Turkish',
#                         'Turkmen',
#                         'Ukrainian',
#                         'Urdu',
#                         'Uyghur',
#                         'Uzbek',
#                         'Vietnamese',
#                         'Welsh',
#                         'Xhosa'
#                         'Yiddish',
#                         'Yoruba',
#                         'Zulu',}
# #default selection for dropdownlists
# lan1.set('English')
# lan2.set('Arabic')
#
# #creating dropdown and arranging in the grid
# lan1menu = OptionMenu( mainframe, lan1, *choices)
# Label(mainframe,text="Select a language").grid(row = 0, column = 1)
# lan1menu.grid(row = 1, column =1)
#
# lan2menu = OptionMenu( mainframe, lan2, *choices)
# Label(mainframe,text="Select a language").grid(row = 0, column = 2)
# lan2menu.grid(row = 1, column =2)
#
# #Text Box to take user input
# Label(mainframe, text = "Enter text").grid(row=2,column=0)
# var = StringVar()
# textbox = Entry(mainframe, textvariable=var).grid(row=2,column=1)
#
# #textbox to show output
# #label can also be used
# Label(mainframe, text = "Output").grid(row=2,column=2)
# var1 = StringVar()
# textbox = Entry(mainframe, textvariable=var1).grid(row=2,column=3)
#
# #creating a button to call Translator function
# b=Button(mainframe,text='Translate',command=translate).grid(row=3,column=1,columnspan=3)
#
# root.mainloop()