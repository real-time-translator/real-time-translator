import tkinter as tk

root= tk.Tk()

def page2(root):
    def change_page1():
        root.withdraw()
        import gui
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text = 'This is page 2').grid(row = 0)
    tk.Button(page, text = 'main page', command = lambda: change_page1()).grid(row = 1,column=6)
    # tk.Button(page, text = 'To page 3', command = changepage_page3).grid(row = 1,column=7)

    

# def changepage_page3():
#     root.quit()
#     import page3
    


root.title("Real Time Translator")
root.geometry("400x400")
page2(root)
root.mainloop()