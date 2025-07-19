#File Name - Candidates_Framework.py
#Created By - Manas Jagyasi

from tkinter import *
from tkinter import messagebox 
from tkinter.messagebox import askyesno 
import mysql.connector as my
import dbconfig 
import sys  
from sqlalchemy import create_engine,text
import pandas
mydb=None 
try:
    mydb = my.connect(**dbconfig.config) 
   
    engine = create_engine("mysql+pymysql://root:Manas2353r@localhost/quiz")   
except Exception as ex:
    messagebox.showinfo('Database Exception' , str(ex))
    sys.exit(0) 


cursor=mydb.cursor(dictionary=True)


win=Tk()
win.geometry('800x300')
win.title('Candidate Frame-By Manas')


Enrollment=IntVar()  
Name=StringVar()
Qualification=StringVar()
Mobile=IntVar()
email=StringVar()
dob=StringVar()
address=StringVar()
city=StringVar()

operation="" 
modified=False 
df=None  
index=0  
rows=0 
cols=0  

def showData(index):
    Enrollment.set(df.loc[index][0]) 
    Name.set(df.loc[index][1])
    Qualification.set(df.loc[index][2])
    Mobile.set(df.loc[index][3])
    email.set(df.loc[index][4])
    dob.set(df.loc[index][5])
    address.set(df.loc[index][6])
    city.set(df.loc[index][7])

def loadData():
    
    global df  
    sql='Select * from candidates'
   
    df=pandas.read_sql(sql, engine) 
    global index,rows, cols
    rows,cols=df.shape  
    index=rows-1 
    print('Data Frame=',df)  
    showData(index) 

loadData()  

def emptyText():
    Enrollment.set('')
    Name.set('')
    Qualification.set('')
    Mobile.set('')
    email.set('')
    dob.set('')
    address.set('')
    city.set('')
    
def setTextState(value):
    txtaddress.config(state=value) 
    txtName.config(state=value)
    txtQualification.config(state=value)
    txtMobile.config(state=value)
    txtemail.config(state=value)
    txtdob.config(state=value)
    txtcity.config(state=value)
   
def setButtonState(value):
    btnAdd.config(state=value)
    btnEdit.config(state=value)
    btnSave.config(state='normal' if value=='disabled' else 'disabled')
    btnDelete.config(state=value)
    btnFirst.config(state=value)
    btnPrevious.config(state=value)
    btnNext.config(state=value)
    btnLast.config(state=value)

def addClick():
    
    global operation 
    operation="add"  
    emptyText() 
    setTextState('normal') 
    setButtonState('disabled') 

def editClick():
    
    global operation 
    operation='edit'
    setTextState('normal') 
    setButtonState('disabled') 
    
def saveClick():

    confirmation = askyesno(title='confirmation',
                    message='Are you sure to Save it?')
    if not confirmation: 
        messagebox.showerror('Failure' , 'Record Not Saved')
        setTextState('readonly') 
        setButtonState('normal') 
        return 
    
    sql='' 
    global operation
    if operation=='add': 
        sql="insert into candidates(Name,Qualification,Mobile,email,address,dob,city) values('{}','{}','{}','{}','{}','{}','{}')".format(Name.get(),Qualification.get(),Mobile.get(),email.get(),address.get(),dob.get(),city.get())
    elif operation=='edit': 
        sql="update candidate set Enrollment='{}' , \
            Name='{}', Qualification='{}', Mobile='{}', email='{}', dob='{}', city='{}' where Enrollment='{}'".format(Enrollment.get(),Name.get(),Qualification.get(),Mobile.get(),email.get(),address.get(),dob.get(),city.get())
    print('SQL=', sql)     
    
    try:
        cursor.execute(sql)
        count=cursor.rowcount
        print('Result=', count)
        if count>0:
            mydb.commit() 
            global modified 
            modified=True
            messagebox.showinfo('Congrats', 'Record Saved')
        else:
            messagebox.showerror('Sorry', 'Failed to Saved')
    except Exception as ex:
        messagebox.showerror('Error in Save' , str(ex))
    
    setTextState('readonly') 
    setButtonState('normal')

def deleteClick():
    
    q=Enrollment.get()
    if q is None or q==0:
        messagebox.showerror('Sorry', 'No qid found')
        return 
    
    confirmation = askyesno(title='confirmation',
                    message='Are you sure to Delete it?')
    if not confirmation: 
        return
   
    sql="delete from question2 where qid='{}' ".format(q)
    print('Debugging . SQL=', sql)
    try:
        cursor.execute(sql)
        count=cursor.rowcount
        print('Result=', count)
        if count>0:
            mydb.commit()
            global modified 
            modified=True
            messagebox.showinfo('Congrats', 'Record Deleted')
        else:
            messagebox.showerror('Sorry', 'Failed to Delete')
    except Exception as ex:
        messagebox.showerror('Error in Save' , str(ex))

  
def navigationClick(value): 
   
    global modified
    if modified:   
        loadData() 
        modified=False 
        
    global index, rows
    if value=='F': index=0  
    elif value=='L': index=rows-1 
    elif value=='P':  
        if index>0:  
            index-=1   
        else:
            index=rows-1 
    elif value=='N': 
        if index<rows-1: 
            index+=1  
        else:
            index=0    
    showData(index)
    print('Value is ', value)  


Label(win, text="Enrollment:" ).grid(row=0, column=0)
txtEnrollment=Entry(win, width='20',textvariable=Enrollment, state='readonly')
txtEnrollment.grid(row=0, column=1, padx='10' ,pady='10')

btnAdd=Button(win, width='10', text='Add', command=addClick)
btnAdd.grid(row=0, column=2)

Label(win, text="Name").grid(row=1, column=0)
txtName=Entry(win,width='100', textvariable=Name, state='readonly')
txtName.grid(row=1, column=1)

btnEdit=Button(win, width='10', text='Edit', command=editClick)
btnEdit.grid(row=1, column=2)

Label(win, text="Qualification:").grid(row=2, column=0)
txtQualification=Entry(win, width='20', textvariable=Qualification, state='readonly')
txtQualification.grid(row=2, column=1)

btnSave=Button(win, width='10' ,text='Save', command=saveClick, state='disabled')
btnSave.grid(row=2, column=2)

Label(win, text="Mobile No.:").grid(row=3, column=0)
txtMobile=Entry(win, width='50', textvariable=Mobile, state='readonly')
txtMobile.grid(row=3, column=1)

btnDelete=Button(win, width='10', text='Delete', command=deleteClick)
btnDelete.grid(row=3, column=2)

Label(win, text="email:").grid(row=4, column=0)
txtemail=Entry(win, width='50', textvariable=email, state='readonly')
txtemail.grid(row=4, column=1)

Label(win, text="address:").grid(row=5, column=0)
txtaddress=Entry(win, width='50', textvariable=address, state='readonly')
txtaddress.grid(row=5, column=1)

Label(win, text="dob:").grid(row=6, column=0)
txtdob=Entry(win, width='50', textvariable=dob, state='readonly')
txtdob.grid(row=6, column=1)

Label(win, text="city:").grid(row=7, column=0)
txtcity=Entry(win, width='50', textvariable=city, state='readonly')
txtcity.grid(row=7, column=1)


btnFirst=Button(win ,text='First', width='10', command=lambda: navigationClick('F'))
btnFirst.grid(row=8 , column=0)

btnPrevious=Button(win ,text='Previous', width='10', command=lambda:navigationClick('P'))
btnPrevious.grid(row=8, column=1,sticky='E')

btnNext=Button(win ,text='Next', width='10', command=lambda:navigationClick('N'), anchor='center')
btnNext.grid(row=9 , column=0 )

btnLast=Button(win ,text='Last', width='10', command=lambda:navigationClick('L'))
btnLast.grid(row=9 , column=1, sticky='E')


win.mainloop()
