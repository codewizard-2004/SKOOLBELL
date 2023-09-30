import csv
import os

#Roll-First-Second-Subject-F-M-DOB-Fee-T1-T2-Int-Img

def count(clas):
    '''Gives the number of students in a class'''
    path ='../assets/data/student/'+clas+'.csv'
    file = open(path)
    data = csv.reader(file)
    count = 0
    for i in data:
        count = count+1
    return count

def view_student(Class,roll='all'):
    '''Returns a list of students of a class
     or a single student if roll no is given'''
    path= '../assets/data/student/'+Class+'.csv'
    if roll=='all':
        data=[]
        with open(path) as file:
            r=csv.reader(file)
            for i in r:
                data.append(i)
        return data
    else:
        data=[]
        with open(path) as file:
            r=csv.reader(file)
            for i in r:
                if int(i[0])==roll:
                    return i

def add_student(Class,first,second,gender,subject,father,mother,dob,fee,e1,e2,e3,img):
    '''adds student to csv'''
    path='../assets/data/student/'+Class+'.csv'
    file=open(path,'r+',newline='')
    w = csv.writer(file)
    l = count(Class)
    file.read()
    w.writerow([str(l+1),first,second,gender,subject,father,mother,dob,fee,e1,e2,e3,img])
    file.close()

def edit_student(Class,roll,first,second,gender,subject,father,mother,dob,fee,e1,e2,e3,img):
    '''edit the data given in csv of a student and replace
      them with new values'''
    path='../assets/data/student/'+Class+'.csv'
    path1 = '../assets/data/student/'+Class+'1.csv'
    s = open(path, 'r')
    t = open(path1, 'w', newline='')
    w = csv.writer(t)
    r = csv.reader(s)
    data = []
    for i in r:
        if i[0]==roll:
            i[1]=first
            i[2]=second
            i[3]=gender
            i[4]=subject
            i[5]=father
            i[6]=mother
            i[7]=dob
            i[8]=fee
            i[9]=e1
            i[10]=e2
            i[11]=e3
            i[12]=img
            data.append(i)
        else:
            data.append(i)
    for i in data:
        w.writerow(i)
    s.close()
    t.close()
    os.remove(path)
    os.rename(path1, path)

def remove_student(Class,roll):
    '''remove the student with given roll number
      in the given class'''
    path = '../assets/data/student/'+Class+'.csv'
    path1 = '../assets/data/student/'+Class+'1.csv'
    s = open(path, 'r')
    t = open(path1, 'w', newline='')
    w = csv.writer(t)
    r = csv.reader(s)
    data = []
    for i in r:
        data.append(i)
    for i in data:
        if int(i[0]) == roll:
            data.remove(i)
    for i in range(len(data)):
        data[i][0] = i+1
    for i in data:
        w.writerow(i)
    s.close()
    t.close()
    os.remove(path)
    os.rename(path1, path)
