from tkinter import *
import os
import cryptocode
import pyperclip
from tkinter import filedialog
from PIL import ImageTk, Image
import time
import webbrowser





root = Tk()
root.title('KeePass')
root.geometry('900x700')
root.configure(bg="#C6CAC3")
root.resizable(0,0)


saved = Label(root,text="SAVED",bg="red",fg="white",font=("Arial",'20'),width=50,)
copied = Label(root,text="COPIED TO CLIPBOARD",bg="green",fg="white",font=("Arial",'20'),width=50,)

# CONTACT 
def callback(url):
   webbrowser.open_new_tab(url)
link = Label(root,text="NEED HELP ?",font=("Arial",'15'),bg="#1C729B",fg="white",bd=0,width=15)
link.place(x=700,y=100)
link.bind("<Button-1>", lambda e:
callback("https://discord.gg/GbV9EguW"))








# SAVING DATA TO FILES

def save_data():
    
    
    passw_info = passw.get()
    file_info = fileinfo.get()
    savingKey = savekey.get()
    passwcoded = cryptocode.encrypt(passw_info,savingKey)
    f = open(file_info,"w")
    f.write(passwcoded)
    f.close()
    saved.pack()
    
    root.after(2000,saved.destroy)


# SEARCHING DATA TO FILES

def search_data():
    appinfo = appinformation.get()
    searchingKey = searchkey.get()
    with open(appinfo,"r+") as f:

        passwcoded = f.read()
        
        passwdecoded = cryptocode.decrypt(passwcoded,searchingKey)
        print(passwdecoded)
        
        pyperclip.copy(passwdecoded)
        copied.pack()
    
        root.after(2000,copied.destroy)
# PRESSING THE SEE BUTTON (LEFT)
def seepass():
    password = passw.get()
    leftEntryPass.configure(show=password)
    
def hidepass():
    
    leftEntryPass.configure(show="*")    
    
# DISPLAY THE LOGO OF THE APP

frameLogo = Frame(root,width=900,height=50,bg="white").pack()
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Label(frameLogo,image=logo,bd=0,width=150).place(x=0,y=5)


# SEE ICON
see = PhotoImage(file="see.png")
hide = PhotoImage(file="hide.png")


passwGiven = StringVar()
searchkey = StringVar()
appinformation = StringVar()
savekey = StringVar()
fileinfo = StringVar()
passw = StringVar()

   
# LEFT PART 
    
Label(root,text="Application ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="60",y="200")
Entry(root,relief=FLAT,width=30,textvariable=fileinfo,bg="white",fg="black",font=35).place(x="50",y="250")
    
  
Label(root,text="Password ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="60",y="300")
leftEntryPass = Entry(root,relief=FLAT,width=30,show="*",textvariable=passw,bg="white",fg="black",font=35)
leftEntryPass.place(x="50",y="350")
    
seeleft = Button(root,image=see,bg="#C6CAC3",bd=0,highlightcolor="#C6CAC3",command=seepass).place(x=40,y=100)
hideleft = Button(root,image=hide,bg="#C6CAC3",bd=0,highlightcolor="#C6CAC3",command=hidepass).place(x=80,y=100)

Label(root,text="Key ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="60",y="400")
Entry(root,relief=FLAT,width=30,textvariable=savekey,bg="white",fg="black",font=35).place(x="50",y="450")


   
save = Button(root,text="SAVE",font=("Arial",'15'),bg="#1C729B",fg="white",bd=0,width=15,command=lambda:save_data()).place(y=500,x=100)


  
# RIGHT PART


Label(root,text="Application ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="460",y="200")
Entry(root,relief=FLAT,width=30,bg="white",fg="black",font=35,textvariable=appinformation).place(x="450",y="250")  # TEXT VARIABLE TO GET ENTRIES
    
search = Button(root,text="SEARCH",font=("Arial",'15'),bg="#1C729B",fg="white",bd=0,width=15,command=search_data).place(y=500,x=500)  # NO COMMAND


Label(root,text="Key ? ",bg="#C6CAC3",fg="#0F4159",font=("Arial",'25')).place(x="460",y="300")
Entry(root,relief=FLAT,width=30,textvariable=searchkey,bg="white",fg="black",font=35).place(x="450",y="350")

   






















root.mainloop()
