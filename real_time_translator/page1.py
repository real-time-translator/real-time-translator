import tkinter as tk


# def page1(root):
#     def change_page1():
#         root.withdraw()
#         import gui
#     page = tk.Frame(root)
#     page.grid()
#     tk.Label(page, text = 'This is page 1').grid(row = 0)
#     tk.Button(page, text = 'main page', command = lambda: change_page1()).grid(row = 1,column=6)
    # tk.Button(page, text = 'To page 3', command = changepage_page3).grid(row = 1,column=7)

    

# def changepage_page3():
#     root.quit()
#     import page3
    


# root.title("Real Time Translator")
# root.geometry("400x400")
# page1(root)
# root.mainloop()
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

if __name__ == "__main__":
    root= tk.Tk()
    root.mainloop()