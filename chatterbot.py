#Step I:
from tkinter import *
from chatterbot import ChatBot  #Pascal Case - Class Name
from chatterbot.trainers import ListTrainer
import time
import pyttsx3	#For text to speech 

time.clock=time.time #Reason: Now time.clock is NOT available
#Step II: Create Instance/Object of Tk class
win=Tk()
win.title('TecDev Bot')
win.geometry('400x500')

#Step III: Create instance of ChatBot class
#support math and time logics
bot=ChatBot("TecBot",
logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
            )
#text to speech engine - load it into memory
engine = pyttsx3.init()  #Step II: initiale TTS 
#Step IV: Provide some domain-specific (like Java, Python, GK) training to the 

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

#Step V: Associate ListTrainer object with our bot

trainer = ListTrainer(bot)
#Step VI: Now train the bot with list of conversations
trainer.train(conversation)
#Step VII: Create a Bind Variable to link with Entry Widget
query=StringVar()

#Step IX: Space for Event Handler Code
def showResult():
    q=query.get() #Get text data from Entry UI
    #Get response from the bot for given value q
    response = bot.get_response(q)
    lstMsg.insert(END, "User:" + q)
    lstMsg.insert(END, "TecBot: " + str(response))
    lstMsg.yview(END) #Move cursor to end of List
    engine.say(str(response)) #Step III Speak text
    engine.runAndWait() #Step IV: asking engine to keep waiting
    query.set("") #make query empty

def enterPressed(event):
    btnResponse.invoke() #Means programmatically click button
#Step VIII: Design UI
img=PhotoImage(file="bot2.png")  #Should be in the same folder as the program
lblImage=Label(win, image=img ) #hungarian notation
lblImage.pack(pady=10)  #prefix lbl means label then purpose
#Step X: We're creating a Frame (Child Window) to create
#group of UI widgets: Listbox, Scrollbar
fra=Frame(win)
#creating a scrollbar inside the frame
vscroll=Scrollbar(fra)
vscroll.pack(side=RIGHT, fill=Y) #right hand side
#Linking Scrollbar with Listbox using yscrollcommand
lstMsg=Listbox(fra, width=50, height=10,yscrollcommand=vscroll.set)
lstMsg.pack(side=LEFT, fill=BOTH, pady=15)
fra.pack() #now frame is added to tkinter window
#below components are outside frame (part of main window)
lblQuery=Label(win,text="Write Query Here" , font=("courier" , 18))
lblQuery.pack()
txtQuery=Entry(win, width=30, font=("courier" , 18), textvariable=query)
txtQuery.pack()
btnResponse=Button(win, text="Get Response" , font=("courier" , 18), command=showResult)
btnResponse.pack()
#When Enter (Return Key) is pressed call enterPressed fn
win.bind("<Return>" , enterPressed)
win.mainloop()
