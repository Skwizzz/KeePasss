from tkinter import *
import os
import cryptocode
import pyperclip
from tkinter import filedialog
def save_data():
    passw_info = passw.get()
    file_info = fileinfo.get()
    passwcoded = cryptocode.encrypt(passw_info,"KeePassKey25152021")
    f = open(file_info,"w")
    f.write(passwcoded)
    f.close()




root = Tk()
root.title('KeePass')
root.geometry('600x400')
root.configure(bg="black")
root.resizable(0,0)





fileinfo = StringVar()
passw = StringVar()

   
    
    
Label(root,text="Application ? ",bg="black",fg="white",font=29).pack()
Entry(root,relief=FLAT,width=50,textvariable=fileinfo).pack()
    
  
Label(root,text="Password ? ",bg="black",fg="white",font=29).pack()
Entry(root,relief=FLAT,width=50,show="*",textvariable=passw).pack()
    
   
save = Button(root,text="SAVE",bg="white",bd=0,width=15,command=lambda:save_data()).place(y=100,x=248)
  

























root.mainloop()
