from tkinter import *
import os
import cryptocode
import pyperclip
from tkinter import filedialog
from PIL import ImageTk, Image
import time

root = Tk()
root.title('KeePass')
root.geometry('800x600')
root.configure(bg="#C6CAC3")
root.resizable(0,0)


saved = Label(root,text="SAVED",bg="red",fg="white",font=("Arial",'20'),width=50,)
copied = Label(root,text="COPIED TO CLIPBOARD",bg="green",fg="white",font=("Arial",'20'),width=50,)

# SAVING DATA TO FILES

def save_data():
    
    
    passw_info = passw.get()
    file_info = fileinfo.get()
    passwcoded = cryptocode.encrypt(passw_info,"KeePassKey25152021")
    f = open(file_info,"w")
    f.write(passwcoded)
    f.close()
    saved.pack()
    
    root.after(2000,saved.destroy)


# SEARCHING DATA TO FILES

def search_data():
    appinfo = appinformation.get()
    with open(appinfo,"r+") as f:

        passwcoded = f.read()
        
        passwdecoded = cryptocode.decrypt(passwcoded,"KeePassKey25152021")
        print(passwdecoded)
        entryPassw.delete(0,END)
        entryPassw.insert(0,passwdecoded)
        pyperclip.copy(passwdecoded)
        copied.pack()
    
        root.after(2000,copied.destroy)

# DISPLAY THE LOGO OF THE APP

frameLogo = Frame(root,width=800,height=50,bg="white").pack()
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Label(frameLogo,image=logo,bd=0,width=150).place(x=0,y=5)








appinformation = StringVar()

fileinfo = StringVar()
passw = StringVar()

   
# LEFT PART 
    
Label(root,text="Application ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="60",y="200")
Entry(root,relief=FLAT,width=30,textvariable=fileinfo,bg="white",fg="black",font=35).place(x="50",y="250")
    
  
Label(root,text="Password ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="60",y="300")
Entry(root,relief=FLAT,width=30,show="*",textvariable=passw,bg="white",fg="black",font=35).place(x="50",y="350")
    
   
save = Button(root,text="SAVE",font=("Arial",'15'),bg="#1C729B",fg="white",bd=0,width=15,command=lambda:save_data()).place(y=400,x=100)


  
# RIGHT PART


Label(root,text="Application ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="460",y="200")
Entry(root,relief=FLAT,width=30,bg="white",fg="black",font=35,textvariable=appinformation).place(x="450",y="250")  # TEXT VARIABLE TO GET ENTRIES
    
search = Button(root,text="SEARCH",font=("Arial",'15'),bg="#1C729B",fg="white",bd=0,width=15,command=search_data).place(y=400,x=500)  # NO COMMAND
Label(root,text="Your password :",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="460",y="300")
entryPassw = Entry(root,relief=FLAT,width=30,show="*",bg="white",fg="black",font=35,)
entryPassw.place(x="450",y="350") 

   






















root.mainloop()
