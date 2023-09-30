from tkinter import *#import everything from tkinter module
from PIL import Image,ImageTk#importing pillow for loading image
from tkinter import ttk,filedialog,messagebox#importing ttk which has Combobox,listbox etc
import dataloader#the function that we defined
import matplotlib.pyplot as plt#matplotlib to show graphs

root=Tk()#starting a window
root.title('SKOOLBELL APP')#nameing the window
root.geometry('1500x800')#defining the size of windo
root.resizable(0,0)# removinvg the maximize minimize 
root.iconbitmap('../assets/logo/Picture11.ico')#setting up logo

fnt=('Helvatica',16)#[helvatica,16,default]
#====================================================================BACKGROUND==================================
bg=PhotoImage(file="../assets/background/bg11.png")#loading the backgroung
main_label=Label(root,image=bg)#setting up background
main_label.pack()# packing the background

bug=0 #to fix a bug that i found while using the class combobox in update
def putnames(e):  # gets data from csv and puts it on listbox which works for view and remove(used in class combobox)
    search.place(x=500,y=80)
    lb.place(x=500,y=110)
    lb.delete(0, END)# removing everything from listbox
    #view_frame.place_forget()
    data = dataloader.view_student(cls.get())# getting the students from the class
    typed=search.get()#gives what typed in search bar
    if typed=='':
        for i in data:
            lb.insert(END, str(i[0]+'.\t'+i[1]+'  '+i[2]))#inserts everyone in that class if nothing is typed
    else:
        D=[]
        for i in data:
            if typed.lower() in i[1].lower() or typed.lower() in i[2].lower():
                D.append(i[0]+'.\t'+i[1]+'  '+i[2])# finds the students with the typed letters and append them to a list
                lb.delete(0,END)# delete previous students from listbox
        for i in D:
            lb.insert(END,i)#inserting all students into listbox that user searched for
#=================================================================VIEW STUDENTS=====================================
def view_press():#when we press view button
    global bug
    bug=0
    button_view.config(bg='blue')# to change the colour of buttons
    button_rem.config(bg='#122841')#same above
    button_add.config(bg='#122841')#same above
    remove_view(),cls.place(x=500,y=30),up_frame.place_forget(),add_frame.place_forget(),remove.place_forget()#adds and removes items related to view

def detail(e):#when we select a student from listbox
    global bug
    if bug==1:
        return
    def getmark():#shows the graph when exam score is pressed
        plt.plot(['Exam1','Exam2','Exam3'],[int(data[9]),int(data[10]),int(data[11])])
        plt.ylabel('Marks')
        plt.xlabel('Exam')
        plt.show()
    student=lb.get(ANCHOR)#getting the name of the student selected in listbox
    view_frame.place(x=800,y=50)#placing the main frame to display details of student
    data=[]
    try:
        data=dataloader.view_student(cls.get(),roll=int(student[0]))#getting the student details
    except:
        pass
    titles=['Roll no:                      ','First Name:            ','Second Name:       ','gender:                  ','Subject:                 ','Father:                  ','Mother:                 ',
            'Date of Birth:        ','Fee:                      ']#these are the texts in Labels
    y_loc=155#this value is for y axis and it will change everytime inside the loop
    for i in range(9):#labeling the student names on to the main frame
        try:
            Label(view_frame,text=str(titles[i]+'     '+data[i]+'                           '),font=fnt,bg='white').place(x=0,y=y_loc)
            y_loc+=50
        except:
            pass
    Button(view_frame,text='Exam Score',font=fnt,bg='#122841',fg='white',command=getmark).place(x=0,y=600)#setting up button to display marks
    update.place(x=300,y=600)
    try:#trying to add image
        global pic1
        pic1=ImageTk.PhotoImage(Image.open(data[12]))#loading the image
        Label(view_frame,image=pic1,height=150,width=150).place(x=70,y=0)#setting the image
    except:#giving message if there is no image
        Label(view_frame,text='No Picture\nInserted',height=10,width=20,bg='white').place(x=70,y=0)

def remove_view():#when we press the remove button it removes elements of other buttons and place its neccessary items
    view_frame.place_forget()#removing main label where student details are ther
    cls.place_forget()#removing the class comobox
    lb.place_forget()#removing the listbox
    up_frame.place_forget()#removing the update frame
    search.place_forget()#removing the search button           

def Putimage():#this function opens file manager to and returns its location
    root.filename=filedialog.askopenfilename(initialdir='C:/Users',title='select image(150x150,png)',
                                             filetypes=(('png files','*.png'),('ppm files','*ppm'),('jpg','*jpg')))#this function opens file manager
    return (str(root.filename))#changing the value of eloc which is going to be added into csv

eloc='' #this empty string will take the new image loaction 
def update_click():#when we press update
    if lb.get(ANCHOR)=='':
        messagebox.showinfo("INFO",'Please select a student')
        return
    def bck():# to go back and cancel the updation process
        view_press()#undoing everything
        view_frame.place_forget()
    def putimg():#puts the image onto the button
        global epic,eloc
        eloc=Putimage()
        epic=ImageTk.PhotoImage(Image.open(str(eloc)))#opening the selected image
        imgb.config(image=epic,height=150,width=150)#and putting it into that button
    def upd():#verifies all inputted data and updates
        if fn.get()=='' or sn.get()=='' or fa.get()=='' or mo.get()=='' or dob.get()=='' or str(exm1.get())=='' or str(exm2.get())=='' or str(exm3.get())=='':
            messagebox.showinfo('INFO','Complete Data')#checks if anthing is left without inputting
            return
        if str(exm1.get()).isdigit()==False or str(exm2.get()).isdigit()==False or str(exm2.get()).isdigit()==False or int(exm1.get())>100 or int(exm2.get())>100 or int(exm3.get())>100 or int(exm1.get())<0 or int(exm2.get())<0 or int(exm3.get())<0:
            messagebox.showinfo('INFO','Invalid Mark')#checks if numbers are inseted into exam entry
            exm1.delete(0,END),exm2.delete(0,END),exm3.delete(0,END)#deletes marks if not properly given
            return
        else:
            if int(messagebox.askyesno('CONFIRM','Do You Want to Change'))>0:#if everything if correct this will be asked and if user press yes it will update data
                #updating the data using dataloader
                dataloader.edit_student(cls.get(),roll,fn.get(),sn.get(),gen.get(),sb.get(),fa.get(),mo.get(),dob.get(),fe.get(),exm1.get(),exm2.get(),exm3.get(),eloc)
                #deleting all entry
                fn.delete(0,END),sn.delete(0,END),fa.delete(0,END),mo.delete(0,END),dob.delete(0,END),exm1.delete(0,END),exm2.delete(0,END),exm3.delete(0,END)
                up_frame.place_forget(),view_frame.place_forget(),update.place_forget()
        
    roll=(lb.get(ANCHOR)[0])#getting roll number
    student=dataloader.view_student(cls.get(),int(roll))#fetching the student data
    remove_view()
    loc=student[12]#image location
    up_frame.place(x=800,y=50),view_frame.place_forget()
    txtlist=['First Name:','Second Name:','Gender','Subject:','Father:','Mother:','Date of Birth:','fee:','Exam1','Exam2:','Exam3:']
    Y=160
    for i in range(11):#putting the datas of student in update frame
        Label(up_frame,text=txtlist[i],font=fnt,bg='#122841',fg='white').place(x=0,y=Y)
        Y=Y+50
    fn=Entry(up_frame,width=20,font=fnt)#Entry boxes,comboboxes and others for updation
    fn.insert(0,student[1])#inserting the existing data for reference
    fn.place(x=150,y=160)#placing it
    sn=Entry(up_frame,width=20,font=fnt)#same as above
    sn.insert(0,student[2])#same as above
    sn.place(x=150,y=200)#same as above
    gen=ttk.Combobox(up_frame,value=gen_,font=fnt,width=19,state='readonly')
    gen.current(gen_.index(student[3]))
    gen.place(x=150,y=250)
    sb=ttk.Combobox(up_frame,value='',font=fnt,width=19,state='readonly')#creating dependent a comboobx for subjects
    if cls.get()=='XII' or cls.get()=='XI':#adds subjects if the class is XII or XI
        s_add = ['CS', 'bio-math',
                 'bio-ip', 'commerce']
        sb.config(value=s_add)#setting up values
        sb.current(s_add.index(student[4]))#setting a default value
    else:
        sb.config(value=['Hindi','Malayalam'])
    sb.place(x=150,y=300)
    fa=Entry(up_frame,width=20,font=fnt)#entry box for father
    fa.insert(0,student[5])
    fa.place(x=150,y=350)
    mo=Entry(up_frame,width=20,font=fnt)#entry box for mother
    mo.insert(0,student[6])
    mo.place(x=150,y=400)
    dob=Entry(up_frame,width=20,font=fnt)#entry box for date of birth
    dob.insert(0,student[7])
    dob.place(x=150,y=450)
    fev=['PAID','DUE']
    fe=ttk.Combobox(up_frame,value=fev,font=fnt,width=19,state='readonly')#combobox for fees
    fe.current(fev.index(student[8]))
    fe.place(x=150,y=500)
    exm1=Entry(up_frame,width=3,font=fnt)#entry box for exam marks
    exm1.insert(0,student[9])
    exm1.place(x=150,y=550)
    exm2=Entry(up_frame,width=3,font=fnt)#entry box for 2nd exam marks
    exm2.insert(0,student[10])
    exm2.place(x=150,y=600)
    exm3=Entry(up_frame,width=3,font=fnt)#entry box for third exam marks
    exm3.insert(0,student[11])
    exm3.place(x=150,y=650)
    #setting up image in the button
    imgb=Button(up_frame,command=putimg)
    imgb.place(x=0,y=0)
    global pic5,eloc#putting the images
    try:
        eloc=loc# adding the image location to eloc which is previously defined
        pic5=ImageTk.PhotoImage(Image.open(loc))#trying to open with that location
        imgb.config(image=pic5)#setting up the image
    except:
        imgb.config(height=10,width=21,text='Insert Picture',command=putimg)#if image fails to set up
    back=Button(up_frame,text='Back',font=fnt,command=bck)#button for going back
    back.place(x=50,y=700)
    change=Button(up_frame,text='Change Data',font=fnt,command=upd)#button to update data
    change.place(x=200,y=700)

view_frame=Frame(root,height=700,width=400,bg='#122841')

button_view=Button(root,text='View Student',font=fnt,bg='#122841', fg='white',command=view_press,width=20)#button for viewing students
button_view.place(x=200,y=50)
update=Button(view_frame,text='Update',font=fnt,bg='#122841',fg='white',command=update_click)#button for updating students
up_frame=Frame(root,height=850,width=500,bg='#122841')#update frame where things related to update are put
add_frame=Frame(root,height=750,width=500,bg='#122841')#add frame where things related to add are placed

#===================================================ADD STUDENT================================================
aloc='null'#this will be the default value added to image of student unless anothing is selected
def add_click():#function for add button
    button_view.config(bg='#122841')#changes the colours
    button_rem.config(bg='#122841')
    button_add.config(bg='blue')
    global bug#to fix the bug
    bug=1
    def putimg():#this function will put the image that user chooses
        global apic,aloc
        aloc=Putimage()#opens file manager and returns image location
        apic=ImageTk.PhotoImage(Image.open(str(aloc)))#opeing the picture
        insert.config(image=apic,height=150,width=150)#setting up the image
    def addstu():#function to add new student
        #checking if all are filled
        if fn.get()=='' or sn.get()=='' or fa.get()=='' or mo.get()=='' or dob.get()=='' or str(exm1.get())=='' or str(exm2.get())=='' or str(exm3.get())=='':
            messagebox.showinfo('INFO','Complete Data')
            return
        if str(exm1.get()).isdigit()==False or str(exm2.get()).isdigit()==False or str(exm2.get()).isdigit()==False or int(exm1.get())>100 or int(exm2.get())>100 or int(exm3.get())>100 or int(exm1.get())<0 or int(exm2.get())<0 or int(exm3.get())<0:
            #checks if number is entered in all
            messagebox.showinfo('INFO','Invalid Mark')
            exm1.delete(0,END),exm2.delete(0,END),exm3.delete(0,END)
            return
        else:
            if int(messagebox.askyesno('CONFIRM','Do You Want to Add'))>0:
                #this will add the student into csv
                dataloader.add_student(grd.get(),fn.get(),sn.get(),gen.get(),sb.get(),fa.get(),mo.get(),dob.get(),fe.get(),exm1.get(),exm2.get(),exm3.get(),aloc)
                fn.delete(0,END),sn.delete(0,END),fa.delete(0,END),mo.delete(0,END),dob.delete(0,END),exm1.delete(0,END),exm2.delete(0,END),exm3.delete(0,END)
                add_frame.place_forget()
    def addsubj(e):#function to change subject according to class
        if grd.get() == 'XI' or grd.get() == 'XII':#if the user selects the class XII or XI the subject will be updated
            s_add = ['CS', 'bio-math',
                 'bio-ip', 'commerce']
            sb.config(value=s_add)
            sb.current(0)
        elif grd.get() in class_[0:9]:# if user selects any class from LKG to VIII
            sb.config(value=['ALL'])
            sb.current(0)
        else:
            sb.config(value=['Hindi', 'Malayalam'])
            sb.current(0)
    remove_view()
    add_frame.place(x=600,y=20)#the skeleton in which all add widgets are placed
    insert=Button(add_frame,text='''SELECT PICTURE
size:150x150
type:png,ppm''',padx=50,pady=50,command=putimg)#button that will insert image
    insert.place(x=0,y=0)
    Label(add_frame,text='Class:',font=fnt,bg='#122841',fg='white').place(x=0,y=165)#adding labels
    Label(add_frame,text='Exam1:',font=fnt,bg='#122841',fg='white').place(x=80,y=600)
    Label(add_frame,text='Exam2:',font=fnt,bg='#122841',fg='white').place(x=230,y=600)
    Label(add_frame,text='Exam3:',font=fnt,bg='#122841',fg='white').place(x=360,y=600)
    title2=['First Name:','Second Name:','Gender:','Subject:','Father:','Mother:','Date of Birth:','fee:']
    y_val=200#this is the y axis it keeps changing in the for loop
    for i in range(8):#adding labels
        Label(add_frame,text=title2[i],font=fnt,bg='#122841',fg='white').place(x=0,y=y_val)
        y_val+=50
    grd=ttk.Combobox(add_frame,value=class_,font=fnt,width=19,state='readonly')#combobox for class
    grd.current(0)
    grd.bind('<<ComboboxSelected>>', addsubj)#this command will call addsubj when user selects an item in combobox
    grd.place(x=150,y=165)
    fn=Entry(add_frame,width=20,font=fnt)#for first name
    fn.place(x=150,y=200)
    sn=Entry(add_frame,width=20,font=fnt)#second name
    sn.place(x=150,y=250)
    gen=ttk.Combobox(add_frame,value=['Male','Female','Others'],font=fnt,width=18,state='readonly')
    gen.current(0)
    gen.place(x=150,y=300)
    sb=ttk.Combobox(add_frame,value='',font=fnt,width=19,state='readonly')#subject
    sb.place(x=150,y=350)
    fa=Entry(add_frame,width=20,font=fnt)#father
    fa.place(x=150,y=400)
    mo=Entry(add_frame,width=20,font=fnt)#mother
    mo.place(x=150,y=450)
    dob=Entry(add_frame,width=20,font=fnt)#date of birth
    dob.place(x=150,y=500)
    fe=ttk.Combobox(add_frame,value=['PAID','DUE'],font=fnt,width=19,state='readonly')#for fee
    fe.current(0)
    fe.place(x=150,y=550)
    exm1=Entry(add_frame,width=3,font=fnt)
    exm1.place(x=100,y=650)
    exm2=Entry(add_frame,width=3,font=fnt)
    exm2.place(x=250,y=650)
    exm3=Entry(add_frame,width=3,font=fnt)
    exm3.place(x=390,y=650)
    add=Button(add_frame,text='Add Student',font=fnt,command=addstu)#the button that will add students
    add.place(x=200,y=700)
    view_frame.place_forget()

button_add=Button(root,text='Add Student',font=fnt,bg='#122841', fg='white',command=add_click,width=20)#button for adding
button_add.place(x=200,y=200)

#=========================================================REMOVE STUDENT=========================================
def remove_click():#when we press the remove button(the first one)
    global bug
    bug=0
    button_view.config(bg='#122841')
    button_rem.config(bg='blue')
    button_add.config(bg='#122841')
    remove_view()
    cls.place(x=500,y=30)
    add_frame.place_forget()
    update.place_forget()
    view_frame.place_forget()
    remove.place(x=300,y=600)
    

def removing():#when we press remove to remove student
    if messagebox.askyesno('REMOVE','Are You Sure')>0:
        student=lb.get(ANCHOR)
        dataloader.remove_student(cls.get(),int(student[0]))
        remove_view()
        view_frame.place_forget()
    else:
        return

button_rem=Button(root,text='Remove Student',font=fnt,bg='#122841', fg='white',command=remove_click,width=20)#button for removing
button_rem.place(x=200,y=350)
remove=Button(view_frame,text='Remove',font=fnt,bg='#122841',fg='white',command=removing)#the remove button

#=======================================================SOME COMMON THINGS THAT WE ALWAYS USE
class_ = ['LKG','UKG','I','II','III','IV','V','VI','VII','VIII', 'IX', 'X', 'XI', 'XII']# this list is used many times
gen_=['Male','Female','Others']
cls = ttk.Combobox(root, value=class_, font=fnt, width=20,state='readonly')#the combobox used in add remove to select class #It can only be read and not edit
cls.current(0)#set default value
root.option_add('*TCombobox*Listbox.font', ('Helvatica', 15))
cls.bind('<<ComboboxSelected>>', putnames)#when user selects a class putnames functions will be called
search=Entry(root,width=20,font=fnt)#search button 
search.bind('<KeyRelease>',putnames)#Key release function will will call putnames when user types in the searcbar and updates the listbox with similar results
lb = Listbox(root, bd=3, font=fnt, width=20, height=25)#the listbox that we use to show list of students in remove and view
lb.bind('<<ListboxSelect>>',detail)#when user selects an item from listbox the <<ListboxSelect>> function will call detail function

root.mainloop()#mainloop keeps the gui running
