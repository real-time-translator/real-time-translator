import tkinter as tk

root = tk.Tk()

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

class MainPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # The line bellow if you are using pyCharm, but you need to change the path
        # logo = tk.PhotoImage(file=r"\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\images\dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)
       
        tk.Button(BGlabel,text='Real Time Translator',fg = 'white',bg = 'black',bd =  0, highlightcolor="black",highlightbackground="black",borderwidth=0, font=("Helvetica", 30)).place(x=515,y=280)
        
class Navigator(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # The line bellow if you are using pyCharm, but you need to change the path
        # logo = tk.PhotoImage(file=r"\\wsl$\Ubuntu\home\yahiaqous\asac\401\mid-project\real-time-translator\assets\images\dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

        pm = MainPage(self)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)

        pm.place(in_=BGlabel, x=10, y=80, relwidth=1, relheight=1)
        p1.place(in_=BGlabel, x=10, y=80, relwidth=1, relheight=1)
        p2.place(in_=BGlabel, x=10, y=80, relwidth=1, relheight=1)
        p3.place(in_=BGlabel, x=10, y=80, relwidth=1, relheight=1)

        tk.Button(BGlabel, text="Main Page", command=pm.show,fg="white",bg="black",font=("Arial", 15),width=15,height=1).grid(row = 0, column = 2, padx = 30, pady = 8)
        tk.Button(BGlabel, text="Translate a Voice", command=p1.show,fg="white",bg="black",font=("Arial", 15)).grid(row = 0, column = 3, padx = 25)
        tk.Button(BGlabel, text="Translate a Text", command=p2.show,fg="white",bg="black",font=("Arial", 15)).grid(row = 0, column = 4, padx = 25)
        tk.Button(BGlabel, text="Translate a File", command=p3.show,fg="white",bg="black",font=("Arial", 15)).grid(row = 0, column = 5, padx = 25)

        pm.show()


if __name__ == "__main__":
    from gui_page1 import Page1
    from gui_page2 import Page2
    from gui_page3 import Page3
    root.title("Real Time Translator")
    
    main = Navigator(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x714")
    root.mainloop()
