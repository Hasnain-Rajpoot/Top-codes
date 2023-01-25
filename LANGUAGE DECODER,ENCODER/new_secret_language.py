import tkinter as tk
from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename,os
import random
y=tk.Tk()
y.title("secret language")
#y.geometry("800x600")
def openf():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
            t1.delete(1.0,tk.END)
            with open(file,"r") as f:
                for j in f:
                    t1.insert(END,j)
                f.close()
def savef():
    global file
    file=asksaveasfilename(title="choce the file",defaultextension=".txt",filetypes=[("all files","*.*"),
    ("python files","*.py")])
    f=open(file,"w")
    for i in t2.get(1.0,tk.END):
        f.write(str(i))
        #f.write("\n")

    f.close()
def newf():
    global file
    t1.delete(1.0,tk.END)
def help():
    a=tmsg.showinfo("help","hasnain will help you")
def rate():
    a=tmsg.askquestion("was your experience good","was you experience good")
    if a=="yes":
        tmsg.showinfo("nice","rate us on playstore")
    else:
        tmsg.showinfo("ohh no","tell us whats wrong we will fix")
def encode():
    y=[]
    o=[]
    n=t1.get(1.0,tk.END)
    spl=n.split("\n")
    for i in range(0,len(spl)):
        y.append(spl[i].split(" "))
    y.pop()
    print(y)

    for k in range(0,len(y)): 
        for t in y[k]:       
            for k in range(len(t)-1,-1,-1):
                
                fk=t[k]
                if fk.upper() == "a".upper():
                    fk=">"    
                if fk.upper()=="m".upper():
                    fk="<"
                if fk.upper()=="f".upper():
                    fk=":" 
                if fk.upper()=="t".upper():
                    fk="="
                # if fk.upper()=="z".upper():
                #     fk="¬"
                if fk.upper()=="h".upper():
                    fk="`"
                if fk.upper()=="l".upper():
                    fk="/"
                if fk.upper()=="v".upper():
                    fk="("
                if fk.upper()=="o".upper():
                    fk=")"
                if fk.upper()=="d".upper():
                    fk="["
                if fk.upper()=="t".upper():
                    fk="]"
                if fk.upper()=="s".upper():
                    fk="-"
                if fk=="1":
                    fk="_"
                if fk=="7":
                    fk="+"                    
                if fk=="4":
                    fk="'"
                if fk=="9":
                    fk="|"
                if fk=="6":
                    fk="{"
                if fk=="@":
                    fk="}"
                if fk=="0":
                    fk="$"
                if fk==" ":
                    fk="*"       
                t2.insert(END,fk)                                           
            t2.insert(END," ")
        t2.insert(END,"\n")
def decode():
    y=[]
    o=[]
    n=t2.get(1.0,tk.END)
    spl=n.split("\n")
    for i in range(0,len(spl)):
        y.append(spl[i].split(" "))
    y.pop()
    for k in range(0,len(y)):
        for t in y[k]:
            for k in range(len(t)-1,-1,-1):
                fk=t[k]
                if fk == ">":
                    fk="a"    
                if fk=="<":
                    fk="m"
                if fk==":":
                    fk="f" 
                if fk=="=":
                    fk="t"
                #if fk=="¬":
                    #fk=="pk"
                if fk=="/":
                    fk="l"
                if fk=="(":
                    fk="v"
                if fk==")":
                    fk="o"
                if fk=="[":
                    fk="d"
                if fk=="]":
                    fk="t"
                if fk=="-":
                    fk="s"    
                if fk=="`":
                    fk="h"
                if fk=="'":
                    fk="4"
                if fk=="|":
                    fk="9"
                if fk=="{":
                    fk="6"
                if fk=="}":
                    fk="@"
                if fk=="$":
                    fk="0"
                if fk=="_":
                    fk="3"
                if fk=="+":
                    fk="7"
                if fk=="*":
                    fk=""        
                print(fk)    
                t1.insert(END,fk)                                           
            t1.insert(END," ")
        t1.insert(END,"\n")
def dis():
    y.destroy()                    
f1=tk.Frame(y)
l=tk.Label(f1,text="TEXT ENCODER",font="comiscansms 19 bold",bg="green",fg="white",width=24,pady=4)
l.grid(row=0,column=0,pady=4)
scr=tk.Scrollbar(f1,orient="vertical")
t1=tk.Text(f1,height=20,width=50,highlightthickness=5,highlightcolor="red",highlightbackground="red",font="comiscansms 10 bold")
t1.grid(row=1,column=0,padx=20)
scr.grid(row=1,column=1)
scr.config(command=t1.yview)
t1.config(yscrollcommand=scr.set)
img=PhotoImage(name="image1",file="DENCODE.png")
im=PhotoImage(name="image3",file="ENCODE.png")
b1=tk.Button(f1,image=im,text="ENCODE YOUR TEXT",command=encode,fg="white",font="comiscansms 10 bold",borderwidth=0).grid(row=2,column=0,pady=20)
f1.grid(row=0,column=0)
f2=tk.Frame(y)
l2=tk.Label(f2,text="TEXT DECODER",font="comiscansms 19 bold",bg="green",fg="white",width=24,pady=4)
l2.grid(row=0,column=0,pady=4)
scr2=tk.Scrollbar(f2,orient="vertical",bg="red",highlightbackground="red",activebackground="red")
t2=tk.Text(f2,height=20,width=50,yscrollcommand=scr2.set,highlightthickness=5,highlightcolor="red",highlightbackground="red",font="comiscansms 10 bold")
scr2.config(command=t2.yview)
t2.grid(row=1,column=0)
scr2.grid(row=1,column=1)
b2=tk.Button(f2,image=img,command=decode,bd=0,relief=SUNKEN,).grid(row=2,column=0,pady=20)
f2.grid(row=0,column=1)
imm=PhotoImage(name="image9",file="EXIT1.png")
b3=tk.Button(y,image=imm,command=dis,font="comiscansms 10 bold",borderwidth=0).grid(row=4,column=1,sticky="ne",pady=20)

menu2=Menu(y)
m1=Menu(menu2,tearoff=0)
m1.add_command(label="new file",command=newf)
m1.add_command(label="open",command=openf)
m1.add_command(label="save as",command=savef)
menu2.add_cascade(label="File",menu=m1)
menu2.add_command(label="help",command=help)
menu2.add_command(label="Rate us",command=rate)
y.config(menu=menu2)
y.mainloop() 