from tkinter.constants import END, S
from typing import Text
from input_text import input_text_manually, input_text_file
from input_image import imagetotext
from input_voice import transcript_from_file, transcript_from_record
# from edit_text import edit_text
import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
      
       self.extracted_text=None
       self.edit_text=None

       label = tk.Label(self, text="This is page 1")
       label.grid(row=12,column=12)

       self.button_record=tk.Button(self,text="Start Recording",command=self.handle_record)
       self.button_record.place(x=130,y=30)

    def handle_record(self):
        try:
            self.box.destroy()
        except:
            if not self.extracted_text: 
                self.extracted_text=transcript_from_record()
                self.label = tk.Label(self, text=self.extracted_text)
                self.label .place(x=130,y=120)
            else :
                self.label .destroy()
                self.extracted_text=transcript_from_record()
                self.label  = tk.Label(self, text=self.extracted_text)
                self.label .place(x=130,y=120)
                
            edit_button=tk.Button(self,text="Edit Text",command=self.handle_editing)
            edit_button.place(x=20,y=120)
            translate_button=tk.Button(self,text="Translate",command=self.handle_translation)
            translate_button.place(x=20,y=170)


    def handle_editing(self):
            self.user_input = tk.StringVar(self)
            self.box=tk.Entry(self,textvariable=self.user_input)

            self.box.insert(END,self.extracted_text)
            self.box.place(x=130,y=150)

            self.submit_button=tk.Button(self,text=" Submit ",command=self.handle_submiting)
            self.submit_button.place(x=20,y=150)

            self.button_record=tk.Button(self,text="Start Recording",command=self.handle_record)
            self.button_record.place(x=130,y=30)


    def handle_submiting(self):
        self.extracted_text=self.user_input.get()
        print(self.extracted_text)
        self.user_input.set("")
        self.label .destroy()
        self.label  = tk.Label(self, text=self.extracted_text)
        self.label .place(x=130,y=120)
        self.submit_button.destroy()
        self.box.destroy()


    def handle_translation(self):
        try:
            self.label_translation.destroy()
            self.label_translation  = tk.Label(self, text=self.extracted_text)
            self.label_translation .place(x=130,y=200)
           
        except:
            self.label_translation  = tk.Label(self, text=self.extracted_text)
            self.label_translation .place(x=130,y=200)
            print('b')

  

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)
       

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Real Time Translator")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()