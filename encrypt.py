import pyAesCrypt
import os
from tkinter import *

root = Tk()

root.iconbitmap('logo.ico')

def encryption(file, password, buffer_size):

    pyAesCrypt.encryptFile(str(file), str(file) + ".aes", password, buffer_size)

    os.remove(file)

def decryption(file, password, buffer_size):

    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)

    os.remove(file)

def walking_by_dirs(buffer_size, is_encrypt):

    dir = path_input.get()
    password = password_input.get()

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                if is_encrypt == False:
                    decryption(path, password, buffer_size)
                elif is_encrypt == True:
                    encryption(path, password, buffer_size)
            except Exception as ex:
                print(ex)

        else:
            walking_by_dirs(path, password)

buffer_size = 512 * 1024

root['bg'] = '#C0C0C0'
root.title('Bonch encrypter')
root.geometry('500x350')
root.resizable(width=False, height=False)

password_label = Label(root, text='password', bg='#ffb700', font=40)
password_label.place(x=100, y=30)

password_input = Entry(root, bg='white', show='*')
password_input.place(relx=.2, rely=.2, height=30, width=300)

path_label = Label(root, text='path to directory', bg='#ffb700', font=40)
path_label.place(x=100, y=120)

path_input = Entry(root, bg='white')
path_input.place(relx=.2, rely=.45,height=30, width=300)

btn_encrypt = Button(root, text='encrypt', command=lambda: walking_by_dirs(buffer_size, True))
btn_encrypt.place(relx=.2, rely=.65, height=30, width=130)

btn_decrypt = Button(root, text='decrypt', command=lambda: walking_by_dirs(buffer_size, False))
btn_decrypt.place(relx=.533, rely=.65, height=30, width=130)

root.mainloop()
