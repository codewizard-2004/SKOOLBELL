from tkinter import *#imports everything from tkinter
from tkinter import messagebox#imports messagebox
import dataloader#imports our module

#====================================================DEFINING WINDOW===============================================
root = Tk()
root.geometry('1500x800')
root.title('SKOOLBELL Log IN')
root.resizable(0, 0)
root.iconbitmap('../assets/logo/Picture11.ico')
#====================================================BACKGROUND===================================================
main_bg=PhotoImage(file='../assets/background/test.png')
main_label=Label(root,image=main_bg)
main_label.pack()
fnt=("Helvatica",26)
#====================================================SETTING-UP ENTRY BOX FOR USERNAME AND PASSOWRD==============
username = Entry(root, width=20, border=0,fg='#122841',font=('Helvatica',19))
username.place(x=575, y=345)
password = Entry(root, width=20, border=0, show='*', fg='#122841',font=('Helvatica',19))
password.place(x=575, y=445)
#===================================================LOGIN BUTTON AND ITS FUNCTIONS=================================
def log_complete():#if login is successful this window will be destroyed and display window will be imported
    root.destroy()
    import display

def log():#this function will be called when user presses login and checks the items entered in entry boxs
    u=username.get()
    p=password.get()
    if u=='SCHOOLADMIN123' and p=='123gvs':
        messagebox.showinfo("LOGIN",'Login Successful')
        log_complete()
        return
    else:
        if u=='' or p=='':
            messagebox.showwarning('LOGIN','All fields must be filled')
        else:
            messagebox.showwarning("LOGIN","Incorrect Username or Password")


ntpic=PhotoImage(file='../assets/button/login.png')#loads the image for login button
login = Button(root, bd=0, command=log,image=ntpic)#the login button
login.place(x=600, y=600)#placing the login button

root.mainloop()
