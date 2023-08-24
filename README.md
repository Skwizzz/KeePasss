# KeePasss
Simple password manager, I might add an UI later but for now its shell based. Passwords are encrypted and saved into a text file in the directory of the application.


You need to install the libraries Pyperclip and Cryptocode in order to use the app


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
 The terminal will display your password. Voilà !


 NOTE : You should change the key in both programs, the default one is KeePassKey25152021.
 You can change it in line 9 of the decoder and same line in the encoder.
 If you consider using KeePass for a personal use, change this key this will be your "main password"

 Thanks for reading, if you have any questions or suggestions please add me on discord, with the username "boulogne".
