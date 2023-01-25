import tkinter as tk
from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename,os 
y=tk.Tk()

y.title("ALHAMD BOOK DEEPO")
def do():   
    n=ent1.get()
    n1=ent2.get()
    n2=ent3.get()
    n3=ent4.get()
    n4=tt.get()
    if n4==1:
        p="YES"
    if n4==0:
        p="NO"
    if n=="":
        tk.messagebox.showerror("error","please enter the book name")
    elif n1=="":
        tk.messagebox.showerror("error","please enter the book price")
    elif n2=="":
        tk.messagebox.showerror("error","please enter the purchase date") 
    elif n3=="":
        tk.messagebox.showerror("error","please enter the serial number")                  
    else:
        list1.insert(END,f"{n},{n1},{n2},{n3},{p}")
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
def delete():
    list1.delete(tk.ANCHOR)
def close():
    y.destroy()
def view():
    f=open("goodDetail.csv","r")  
    for i in f:
        list1.insert(END,i)   
def de():
    list1.delete(0,END)
def savef():
    global file
    file=asksaveasfilename(title="choce the file",filetypes=[("all files","*.*"),
    ("python files","*.py")])
    f=open(file,"w")
    for i in list1.get(0,END):
        f.write(str(i))
        f.write("\n")
    f.close()
def update():
    list1.update(ANCHOR) 
def multidel():
    new=""
    for i in reversed(list1.curselection()):
        list1.delete(i)         
def openf():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
            list1.delete(0,END)
            with open(file,"r") as f:
                for j in f:
                    list1.insert(END,j)
                f.close()
    


def help():
    a=tmsg.showinfo("help","hasnain will help you")
def rate():
    a=tmsg.askquestion("was your experience good","was you experience good")
    if a=="yes":
        tmsg.showinfo("nice","rate us on playstore")
    else:
        tmsg.showinfo("ohh no","tell us whats wrong we will fix")
def newf():
    global file
    list1.delete(1,END)
# def search():
#     n5=ent5.get()
#     y=[]
#     for i in list1.get(0,END):
#         y.append(i.split(","))
#     print(y[0])
#     for l in range(0, len(y)):
#         if n5==y[l][0]:
#             list1.insert(y[l][0])
#             break        

#labels

l=tk.Label(y,text="ALHAMD BOOK DEEPO",font="comiscansms 19 bold",bg="red",activebackground="blue",width=20,height=3,relief=SUNKEN,highlightthickness=10,highlightcolor="black",bd=4)
l.grid(pady=30,padx=10)
l1=tk.Label(y,text="Book Name",font=15)
l1.grid(row=1,column=2)
l2=tk.Label(y,text="Book Price",font=15)
l2.grid(row=2,column=2)
l3=tk.Label(y,text="purchase date",font=15)
l3.grid(row=3,column=2)
l4=tk.Label(y,text="serial number",font=15)
l4.grid(row=4,column=2)

# entries


ent1=StringVar()
e1=Entry(y,textvariable=ent1,bd=4,font="comiscansms 10 bold")
e1.grid(row=1,column=3)
ent2=StringVar()
e2=Entry(y,textvariable=ent2,bd=4,font="comiscansms 10 bold")
e2.grid(row=2,column=3)
ent3=StringVar()
e3=Entry(y,textvariable=ent3,bd=4,font="comiscansms 10 bold")
e3.grid(row=3,column=3)
ent4=StringVar()
e4=Entry(y,textvariable=ent4,bd=4,font="comiscansms 10 bold")
e4.grid(row=4,column=3)
# ent5=StringVar()
# e5=Entry(Y,textvariable=ent5,bd=4)
# e5.grid(row=6,column=1)


# lists
f=Frame(y)
scr=Scrollbar(f,orient=VERTICAL,)
scr.grid(row=0,column=2)
list1=Listbox(f,height=8,width=50,yscrollcommand=scr.set,selectmode=MULTIPLE,bg="green",fg="white",font="comiscansms 10 bold")
scr.config(command=list1.yview)
list1.grid(rowspan=1,row=0,column=3,columnspan=1,pady=20)
f.grid(row=0,column=3)
p="BOOK NAME"
j="PRICE"
l="EXPIREY DATE"
k="SERIAL NUMBER"
g=">>"
list1.insert(END,f"{g},{p},{j},{l},{k}")

#buttons


#b=tk.Button(y,text="view all",bg="red",width=10,height=2,command=view,padx=20).grid(row=2,column=0,pady=5,padx=50)
im=PhotoImage(name="m1",file="CLEAR.png")
im2=PhotoImage(name="m2",file="DELETE.png")
im3=PhotoImage(name="m3",file="DELETE ALL.png")
im4=PhotoImage(name="m4",file="EXIT1.png")
im5=PhotoImage(name="m5",file="INSERT.png")
im6=PhotoImage(name="m6",file="UPDATE.png")
b=tk.Button(y,image=im5,command=do,padx=20,width=100,height=50,bd=0).grid(row=2,column=1,padx=20)
b=tk.Button(y,image=im6,command=update,padx=20,width=100,height=50,bd=0).grid(row=3,column=0,pady=5)
b=tk.Button(y,image=im2,width=100,height=50,command=multidel,padx=20,bd=0).grid(row=3,column=1,padx=20)
b=tk.Button(y,image=im,width=100,height=50,bd=0,command=clear,padx=20).grid(row=4,column=0,pady=5,padx=20)
b=tk.Button(y,image=im4,width=100,height=50,command=close,padx=20,bd=0).grid(row=4,column=1,padx=20)
#b=tk.Button(y,text="save all",bg="red",width=10,height=2,command=save,padx=20).grid(row=5,column=0,pady=5,padx=20)
b=tk.Button(y,image=im3,width=100,height=50,command=de,padx=20,bd=0,activebackground="green").grid(row=2,column=0,padx=20)
#b=tk.Button(y,text="search",bg="red",width=10,height=2,command=search,padx=20).grid(row=6,column=0,padx=20)
tt=IntVar()
t1=IntVar
#t2=Radiobutton(y,text="special customer",variable=t1).grid(row=7,column=1,padx=20)
t=Checkbutton(text="special custmer",variable=tt,activebackground="red",anchor=S,bg="green").grid(row=5,column=3,padx=20)


#menues

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
