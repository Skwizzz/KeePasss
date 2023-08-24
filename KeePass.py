import os
import cryptocode
import pyperclip
verif = "no"
mode = input(" Would you like to read or write a file ? (r/w)" )
if mode == "w":
    name = input("Name of the file ? (Usually the name of the app)" ) 
    while verif=="no":
        passw = input("What is your password ? : ")
        print(" Please verify that your password is",passw,"(yes/no)" )
        verif = input()
    passwencoded = cryptocode.encrypt(passw,"Key") # This is the Key used to encrypt and decrypt, if you are using this application for a personal use you should change this. This is your "main password".
    file = open(name,"w")
    file.write(passwencoded)
    file.close()
    print("Done, press ENTER to exit")
    input()
if mode == "r":
    name = input("Name of the file ? (Usually the name the app)")
    with open(name,"r+")as f:
        print("Your password is")
        passw = f.read()
        passwdecoded = cryptocode.decrypt(passw,"Key")
        
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
