import tkinter
from tkinter import messagebox
import time
from tkinter import Tk,Label,Button
import webbrowser
import random
from tkinter import *
def mesgbox():
    parent = tkinter.Tk()
    parent.overrideredirect(1)
    parent.withdraw()
    warn = messagebox.showwarning('Warning Title', 'You Seem Drowzy!! Take a Mao', parent=parent)
    parent.after(3000,lambda:parent.destroy())


def actmind():
   
   root=Tk()
   root.geometry("300x300")
#    def skip():
#       return 

   l=[["Mindful Breathing","https://www.youtube.com/watch?v=dthmKu_llPY"],["Color Breathing","https://www.youtube.com/watch?v=BPKTBFHp-74"],["The Five Sense","https://www.youtube.com/watch?v=7o-oqjiLAOs"]]
   n=random.randint(0,2)

   def call1():
      webbrowser.open_new_tab(l[n][1])
      root.destroy()
   title_label = Label(root,text="MINDFUL ACTIVITIES",font=("Helvetica",14))
   title_label.grid(row=0,column=0,columnspan=2,pady="20")
   title_label = Label(root,text=l[n][0],font=("Helvetica",14))
   title_label.grid(row=1,column=0,columnspan=2,padx="50",pady="20")
   # strings=l[n][1]
   add_button = Button(root,text="Click Here",bg="cyan",font=("Helvetica",10),command=call1)
   add_button.grid(row=2,column=0,padx=5,pady=10)
#    add_button = Button(root,text="Skip",bg="cyan",font=("Helvetica",10),command=skip)
#   add_button.grid(row=2,column=1,padx=5,pady=10)
   root.after(3000,lambda:root.destroy())
   root.mainloop()

