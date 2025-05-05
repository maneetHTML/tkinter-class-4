from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
def open_file():
    filepath=askopenfilename(filetypes=[
        ('Text File',"*.txt"),
        ("Python Files","*.py"),
        ("HTML Files",'*.html'),
        ("all File",'*.')
    ])
    if not filepath:
        return
    with open(filepath,'r') as file:
        text_editor.delete('1.0',END)
        text_editor.insert(END ,file.read())
    window.title(f'Text Editor-{filepath}')

def save_file():
    filepath=asksaveasfilename(defaultextension='.txt',filetypes=[
        ('Text File',"*.txt"),
        ("all File",'*.')  
    ])
    if not filepath:
        return
    with open(filepath,"w") as file:
        file.write(text_editor.get('1.0',END))
    window.title(f'Text Editor - {filepath}')
window=Tk()
window.title("text Editor")
window.geometry("600x500")
window.rowconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

text_editor=Text(window)
button_frame=Frame(window,relief=RAISED,bd=2)
open_button=Button(button_frame,text="Open",command=open_file)
save_button=Button(button_frame,text="Save As...",command=save_file)
open_button.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
save_button.grid(row=1,column=0,padx=5,sticky='ew')
button_frame.grid(row=0,column=0,sticky='ns')
text_editor.grid(row=0,column=1,sticky="nsew")
window.mainloop()