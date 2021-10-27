# Minor-1
A web application which can secure files using cryptography. It can encrypt the content inside of a .txt file by converting the content into some cypher text using AES 128-bit algorithm. Frontend was developed using HTML & CSS while backend was built using Flask framework, where cryptography algorithm is implemented using cryptography.fernet module.

To run the web app, run Main.py and then go to the localhost (127.0.0.1:5500)

Note:- Before running the webapp 'allow access for less secure apps' in senders email account and also code has to be edited in main.py from line 10 for
  1) Senders email id & password
  2) Folder location to store encrypted & decrypted data data
