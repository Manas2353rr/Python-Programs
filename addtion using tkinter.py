#File name- addtion using tkinter.py
#By- Manas Jagyasi



from tkinter import *
win=Tk()
win.title('Addition Example')

a=DoubleVar()
b=DoubleVar()
c=DoubleVar()

def addClick():
    c.set(a.get()+b.get())

def clearClick():
    a.set("")
    b.set("")
    c.set("")

dict={'background':'black','foreground':'white','font':('sans-serif',14)}
dict2={'background':'light grey','foreground':'black','font':('arial',14)}

l1=Label(win,text='enter number 1',**dict)
l1.grid(row=0,column=0)

t1=Entry(win,width=20,textvariable=a,**dict2)
t1.grid(row=0,column=1)

l2=Label(win,text='enter number 2',**dict)
l2.grid(row=1,column=0)

t2=Entry(win,width=20,textvariable=b,**dict2)
t2.grid(row=1,column=1)

l3=Label(win,text='Result is',**dict)
l3.grid(row=2,column=0)

t3=Entry(win,width=20,textvariable=c,**dict2)
t3.grid(row=2,column=1)

b1=Button(win,text='Addition',command=addClick)
b1.grid(row=3,column=0)

b2=Button(win,text='Clear',command=clearClick)
b2.grid(row=3,column=1)

win.mainloop()
