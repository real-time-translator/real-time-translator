import tkinter as tk



# def page3(root):
#     def change_page1():
#         root.withdraw()
#         import gui
        
    
#     page = tk.Frame(root)
#     page.grid()
#     tk.Label(page, text = 'This is page 3').grid(row = 0)
#     tk.Button(page, text = 'main page', command = lambda: change_page1()).grid(row = 1,column=6)
#     # tk.Button(page, text = 'To page 2', command = changepage_page2).grid(row = 1,column=7)


# # def changepage_page2():
# #     root.quit()
# #     import page2
  


# root.title("Real Time Translator")
# root.geometry("400x400")
# page3(root)
# root.mainloop()
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    root= tk.Tk()
    root.mainloop()