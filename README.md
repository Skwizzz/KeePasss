# KeePasss
Simple password manager, I might add an UI later but for now its shell based. Passwords are encrypted and saved into a text file in the directory of the application.


Librairies required : Pyperclip, cryptocode and PIL.
How to download ?
Open a terminal
Type pip install pyperclip and enter
Type pip install cryptocode and enter
Type pip install PIL and enter

HOW TO USE THIS APP ?

1 - Registering a password : 
 Use  the "KeePass.py" program
 Enter a name for the account (I usually just use the site for example if I want to set a password for GitHub I will set the name as GitHub)
 Enter your password
 Press save
 Your password should be encrypted and saved in the same directory as the programs (I might in a next update change the directory to a child named passwords to be more organized)

2 - Reading a password : 
 IMPORTANT : as its still WIP there is no UI to decrypt and show a password so its in the terminal and in another program, this is going to be changed in the next updates.
 Use the "KeePassDecoder.py" program
 Enter the name of the file where your password is saved ( Second step when you register a password)
 The terminal will display your password.
2.1 NEWEST VERSION : 
 You can now use the main program to read a password, the program KeePassDecoder.py is still working but its less efficient.
 Now, simply enter the file name where your password is stored and the password will be directly copied to clipboard.
Voila !






 



 NOTE : You should change the key in both programs, the default one is KeePassKey25152021.

 If you consider using KeePass for a personal use, change this key this will be your "main password"
 I might add in the future a way to change this key directly in the UI.

 Thanks for reading, if you have any questions or suggestions please add me on discord, with the username "boulogne".
