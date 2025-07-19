from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt

win=Tk()
win.geometry('1200x1000')
win.title('Result Calculation')

p=IntVar()
c=IntVar()
m=IntVar()
t=IntVar()
pr=DoubleVar()
name=StringVar()
g=StringVar()


def calClick():
    
    #Total Marks
    t.set(p.get() + c.get() + m.get())

    #Percentage
    pr.set((p.get() + c.get() + m.get())/3)
   
   #Grade
    if pr>=90: g='A+'

    elif pr>=80: g='A'
    elif pr>=70: g='B'
    elif pr>=60: g='C'
    elif pr>=50: g='D'
    elif pr>=40: g='E'
    
    else:
        g='FAIL'

    b1.config(state='disabled')


def plotClick():
    headers=['Name','Physics','Chemistry','Maths','Total','Percent','Grade']
    df=pd.read_csv('marksheet.csv',names=headers)
    df.plot.bar(x='Name',y=['Physics','Chemistry','Maths'],stacked=False)
    plt.show()
    b3.config(state='normal')


def saveClick():
    b2.config(state='normal')
    data="{},{},{},{},{},{},{}\n".format(name.get(),p.get(),c.get(),m.get(),t.get(),pr.get(),g.get())
    print('Data is',data)
    f=open('marksheet.csv','a')
    f.write(data)
    f.close()

    Message.showinfo('Saved','Marks Saved Successfully to File')



def clearClick():
    p.set("")
    c.set("")
    m.set("")
    t.set("")
    pr.set("")
    name.set("")
    g.set("")
    b4.config(state='normal')



dict={'background':'black','foreground':'white','font':('sans-serif',14)}
dict2={'background':'light green','foreground':'black','font':('arial',14)}
dict3={'background':'red','foreground':'dark blue','font':('arial',14)}


#NAME
l1=Label(win,text='Name',**dict)
l1.grid(row=0,column=2,pady=40)

t1=Entry(win,width=20,textvariable=name,**dict2)
t1.grid(row=0,column=4)

#SUBJECTS
l2=Label(win,text='Physics',**dict)
l2.grid(row=2,column=2,pady=10)

t2=Spinbox(win,from_=1,to=100,width=20,textvariable=p,**dict2)
t2.grid(row=2,column=4)

l3=Label(win,text='Chemistry',**dict)
l3.grid(row=4,column=2,pady=10)

t3=Spinbox(win,from_=1,to=100,width=20,textvariable=c,**dict2)
t3.grid(row=4,column=4)

l3=Label(win,text='Maths',**dict)
l3.grid(row=6,column=2,pady=30)

t3=Spinbox(win,from_=1,to=100,width=20,textvariable=m,**dict2)
t3.grid(row=6,column=4)

#CALCULATIONS
l3=Label(win,text='Total',**dict)
l3.grid(row=9,column=0)

t3=Entry(win,width=20,state='readonly',textvariable=t,**dict3)
t3.grid(row=9,column=1)

l3=Label(win,text='Percent',**dict)
l3.grid(row=9,column=3)

t3=Entry(win,width=20,state='readonly',textvariable=pr,**dict3)
t3.grid(row=9,column=4)

l3=Label(win,text='Grade',**dict)
l3.grid(row=9,column=7,pady=30)

t3=Entry(win,width=20,state='readonly',textvariable=g,**dict3)
t3.grid(row=9,column=8,pady=30)

#BUTTONS
b1=Button(win,width=20,text='Calculate',command=calClick)
b1.grid(row=11,column=2,pady=30)

b2=Button(win,width=20,text='Save',command=calClick)
b2.grid(row=11,column=6,pady=30)

b3=Button(win,width=20,text='Plot',command=clearClick)
b3.grid(row=12,column=2)

b4=Button(win,width=20,text='Clear',command=clearClick)
b4.grid(row=12,column=6)

win.mainloop()
