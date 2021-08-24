import tkinter as tk

root = tk.Tk()



def page1(root):
    
    page = tk.Frame(root)
    page.grid()
    # tk.Label(page, text = 'This is the main page').grid(row = 0)
    label=tk.Label(root,text="").grid(row=1,column=1)
    label1=tk.Label(root,text="").grid(row=2,column=1)
    label2=tk.Label(root,text="").grid(row=3,column=1)
    label3=tk.Label(root,text="").grid(row=4,column=1)
    tk.Button(page, text = 'Translte By Voice', command = lambda: changepage_page1(), fg="white",bg="black",font=("Arial", 15)).grid(row = 4,column=2, ipadx=20, ipady=20)
    tk.Button(page, text = 'Translate By Text', command = lambda: changepage_page2(),fg="white",bg="black",font=("Arial", 15)).grid(row = 4,column=3, ipadx=20, ipady=20)
    tk.Button(page, text = 'Translate By File', command = lambda: changepage_page3(),fg="white",bg="black",font=("Arial", 15)).grid(row = 4,column=4, ipadx=20, ipady=20)
    
def changepage_page1():
        root.withdraw()
        
        import page1
def changepage_page2():
    root.withdraw()
    
    import page2

def changepage_page3():
    root.withdraw()
    
    import page3
 


root.geometry("967x725")
root.title("Real Time Translator")
img = tk.PhotoImage(file="assets/images/dictionary2.png")
label=tk.Label(root, image=img)
label.place(x=0, y=0)
label=tk.Label(root, text="", background="white",fg="black",font=("Arial", 15)).grid(row=1, column=1, pady=50)
page1(root)
root.mainloop()