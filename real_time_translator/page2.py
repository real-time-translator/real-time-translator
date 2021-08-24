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
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

        label = tk.Label(BGlabel, text="This is page 2")
        label.place(x=20, y=20)
        

# if __name__ == "__main__":
#     root= tk.Tk()
#     root.mainloop()