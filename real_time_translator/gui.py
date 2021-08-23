from input_text import input_text_manually, input_text_file
from input_image import imagetotext
from input_voice import transcript_from_file, transcript_from_record
from edit_text import edit_text
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import tkinter.filedialog as filedialog
import time



root = Tk()
root.geometry('1050x400')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Real-Time-Translator')

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        pass

def uploadFiles():
    pb1 = Progressbar(
        root, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(root, text='File Uploaded Successfully!', foreground='green').place(x=250,y = 120)
        
    
    
adharbtn = Button(
    root, 
    text ='Choose a picture', 
    command = lambda:open_file()
    ) 
adharbtn.place(x=250,y = 120)



dlbtn = Button(
    root, 
    text ='Choose a text ', 
    command = lambda:open_file()
    ) 
dlbtn.place(x=450,y = 120)



msbtn = Button(
    root, 
    text ='Choose an audio', 
    command = lambda:open_file()
    ) 
msbtn.place(x=650,y = 120)

upld = Button(
    root, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.place(x=800,y = 120)

trans_btn = Button(root, text = 'Edit',command = Translate )
trans_btn.place(x = 800, y= 190 )
Input_text = Text(root, height = 5, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=300,y = 160)
trans_btn = Button(root, text = 'Translate',command = Translate )
trans_btn.place(x = 450, y= 250 )
Input_text = Text(root, height = 5, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=300,y = 300)
root.mainloop()

root.mainloop()




# def input():
#     input_path = tk.filedialog.askopenfilename()
#     input_entry.delete(1, tk.END)  # Remove current text in entry
#     input_entry.insert(0, input_path)  # Insert the 'path'

# def output():
#     path = tk.filedialog.askdirectory()
#     output_entry.delete(1, tk.END)  # Remove current text in entry
#     output_entry.insert(0, path)  # Insert the 'path'


# def begin():
#     my_excel_file = input_entry.get()
#     output_directory = output_entry.get()
#     data_automation(my_excel_file, output_directory)

# trans_btn = tk.Button( text = 'Edit Text',font = 'arial 12 bold',pady = 5,command = input , bg = 'blue', activebackground = 'sky blue')
# trans_btn.place(x = 800, y= 190 )
# Input_text = Text(font = 'arial 10', height = 5, wrap = WORD, padx=5, pady=5, width = 60)
# Input_text.place(x=300,y = 160)


# # #Import the image using PhotoImage function
# # click_btn= imagetotext(file='clickme.png')

# # #Let us create a label for tk.button event
# # img_label= Label(image=click_btn)

# # #Let us create a dummy button and pass the image
# # button= Button(win, image=click_btn,command= my_command,
# # borderwidth=0)
# # button.pack(pady=30)




