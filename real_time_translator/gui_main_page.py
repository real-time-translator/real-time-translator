
import tkinter as tk

root = tk.Tk()
#background
#define img
# class Canvas:
#     def __init__(self):
        
#         img = tk.PhotoImage(file="assets/images/dictionary2.2.png")
#         #create canvas
#         my_canvas = tk.Canvas(root, width=1000, height=714)
#         my_canvas.pack(fill="both", expand=True)
#         #set img in canvas
#         my_canvas.create_image(0,0, image=img, anchor="nw")



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

    def show(self):
        self.lift()

class MainPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

class Navigator(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        logo = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0,y=0,width=1000,height=714)

        pm = MainPage(self)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        # container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        # container.pack(side="top", fill="both", expand=True)

        pm.place(in_=BGlabel, x=0, y=30, relwidth=1, relheight=1)
        p1.place(in_=BGlabel, x=0, y=30, relwidth=1, relheight=1)
        p2.place(in_=BGlabel, x=0, y=30, relwidth=1, relheight=1)
        p3.place(in_=BGlabel, x=0, y=30, relwidth=1, relheight=1)

        bm = tk.Button(BGlabel, text="Main Page", command=pm.show)
        b1 = tk.Button(BGlabel, text="Page 1", command=p1.show)
        b2 = tk.Button(BGlabel, text="Page 2", command=p2.show)
        b3 = tk.Button(BGlabel, text="Page 3", command=p3.show)

       

        bm.grid(row=2, column=1)
        b1.grid(row=2, column=2)
        b2.grid(row=2, column=3)
        b3.grid(row=2, column=4)
        # pm.show()




if __name__ == "__main__":
    from page1 import Page1
    from page2 import Page2
    from page3 import Page3
    root.title("Real Time Translator")
   
    main = Navigator(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x714")

    root.mainloop()


        # img = tk.PhotoImage(file="assets/images/dictionary2.2.png")
        # label=tk.Label(root, image=img)
        # label.place(x=0, y=0)
           # bg_image = tk.PhotoImage(file ="assets/images/dictionary2.2.png")
        # x = tk.Label (image = bg_image)
        # x.grid(row = 0, column = 0)
        # label = tk.Label(self, text="This is main page")
        # label.pack(side="top", fill="both", expand=True)
