import os
import cryptocode
import pyperclip

name = input("Name of the file ? (Usually the name the app)")
with open(name,"r+")as f:
    print("Your password is")
    passw = f.read()
    passwdecoded = cryptocode.decrypt(passw,"KeePassKey25152021")
        
    print(passwdecoded)


    copy = input(" Would you like to copy the password to clipboard ? (y/n) ")
    if copy =="y":
        pyperclip.copy(passwdecoded)
        print("Copied to clipboard")
    else:
        input("Done.")
    f.close()
print("Please press ENTER to exit")    
input()