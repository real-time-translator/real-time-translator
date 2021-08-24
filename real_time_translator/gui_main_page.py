import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is main page")
       label.pack(side="top", fill="both", expand=True)

class Navigator(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        pm = MainPage(self)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        pm.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        bm = tk.Button(buttonframe, text="Main Page", command=pm.show)
        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        bm.pack(side="left")
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        # pm.show()


if __name__ == "__main__":
    from page1 import Page1
    from page2 import Page2
    from page3 import Page3
    root = tk.Tk()
    root.title("Real Time Translator")
    main = Navigator(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
