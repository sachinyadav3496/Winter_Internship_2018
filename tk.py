import tkinter as tk


root = tk.Tk()
root.title('my application')
root.wm_maxsize(500,500)
root.wm_minsize(500,500)

c = 3
label = []
def hello():
    global c
    label.append(tk.Label(f,text='Hello world'))
    label[-1].grid(row=c,column=0,columnspan=6)
    c = c+1

def hi():
    name = e.get()
    print(name)

f = tk.Frame(root)

e = tk.Entry(f,)
e.grid(row=2,column=0,columnspan=5)
b2 = tk.Button(f,text='show value',command=hi)
b2.grid(row=2,column=6)
l = tk.Label(f,text='hello world to graphical interface')
b = tk.Button(f,text='ClickMe!',command=hello)

b1 = tk.Button(f,text='Exit',command=root.destroy)
b1.grid(row=0,column=10)

l.grid(row=0,column=0,columnspan=6)
b.grid(row=0,column=6)

f.pack()

root.mainloop()
