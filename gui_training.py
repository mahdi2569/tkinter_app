from tkinter import *
from tkinter import messagebox
w = Tk()
w.title("balance")
w.configure(background =  "darkblue")
w.geometry("%dx%d+%d+%d" % (550,400,530,250))

def sub():
    name = e1.get()
    lastname = e2.get()
    age = e3.get()
    if not name or not lastname or not age:
        messagebox.showerror("error","please doldormakh kon field lari")
    else:
        messagebox.showinfo("details","details sabt shodand")

def ex():
    ans = messagebox.askyesno("exit","are you sure to exit ?")
    if ans:
        w.destroy()

l1 = Label(w, text = "name", bg = "red",fg = "snow", width = 10)
l1.place(x = 10, y = 10)

l2 = Label(w, text = "last name", bg = "red",fg = "snow", width = 10)
l2.place(x = 10, y = 40)

l3 = Label(w, text = "age", bg = "red",fg = "snow", width = 10)
l3.place(x = 10, y = 70)

x1 = StringVar()
e1 = Entry(w, textvariable = x1, bg = "grey56", fg = "black", width = 18)
e1.place(x = 90, y = 11)

x2 = StringVar()
e2 = Entry(w, textvariable = x2, bg = "grey56", fg = "black", width = 18)
e2.place(x = 90, y = 41)

x3 = IntVar()
e3 = Entry(w, textvariable = x3, bg = "grey56", fg = "black", width = 18)
e3.place(x = 90, y = 71)

b1 = Button(w, text = "submit", bg = "green", fg = "black", width = 10, command = sub)
b1.place(x = 15, y = 100)

b2 = Button(w, text = "exit", bg = "green", fg = "black", width = 10, command = ex)
b2.place(x = 105, y = 100)

lb1 = LabelFrame(w, text = "", height = 120, width = 340, bg = "light blue")
lb1.place(x =205 ,y = 10)
Checkbutton(lb1, text="Option A").place(x=10, y=10)
Checkbutton(lb1, text="Option B").place(x=10, y=40)

lb2 = LabelFrame(w, text = "procces", height = 170, width = 250, bg = "light blue")
lb2.place(x =10 ,y = 135)
Radiobutton(lb2, text="Choice 1", value=1).place(x=10, y=10)
Radiobutton(lb2, text="Choice 2", value=2).place(x=10, y=40)

lb3 = LabelFrame(w, text = "procces", height = 170, width = 280, bg = "light blue")
lb3.place(x =265 ,y = 135)
Label(lb3, text="Extra Info:", bg="lightblue").place(x=10, y=10)
Entry(lb3, width=20).place(x=100, y=10)


w.mainloop()