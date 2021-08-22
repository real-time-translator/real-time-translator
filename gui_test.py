# import tkinter as Tk
from tkinter import *


root = Tk()
root.title('Translate')
root.geometry("967x725")

 # "350x150" == window size (350 pixels wide and 150 pixels high)
 # "+220+80" == window position (220 pixels from the left screen margin and
 # 				80 pixels from the top screen margin

# root.iconbitmap('images/images_icon.png')

####background image

img = PhotoImage(file="images/dictionary3.png")
label=Label(root, image=img)
label.place(x=0, y=0)
###input field
entry = Entry(root, width=50, borderwidth=5)
entry.insert(0,"Enter your name:")


#####
def myClick():
    outPut = "Hello " + entry.get()
    myLabel1 = Label(root, text= outPut)
    myLabel1.grid()

my_label = Label(root, text="Helloooo this is NURA Testing ")
myButton = Button(root, text="click me!" ,command=myClick , fg="blue" , bg="black")
button_quit = Button(root, text="quit" , command= root.quit)

#put it on the screen
my_label.grid(row=4 , column= 2)
entry.grid(row=3 , column= 2)
myButton.grid(row=5 , column= 2)
button_quit.grid(row=6 , column= 2)

#mainloop
root.mainloop()