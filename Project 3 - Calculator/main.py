from tkinter import *

root = Tk(screenName="My example window")
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

operation = lambda b: 0
def add(a):
    return lambda b: a + b
def sub(a):
    return lambda b: a - b
def mul(a):
    return lambda b: a * b
def div(a):
    return lambda b: int(a / b)
def powOp(a):
    return lambda b: a ** b

entry.insert(0, "0")

def num(inputNum):
    def outputFnc():
        temp = entry.get()
        temp += str(inputNum)
        temp = str(int(temp))
        entry.delete(0, END)
        entry.insert(0, temp)
        return
    return outputFnc

buttons: list = []

for i in range(10):
    buttons.append(Button(root, text=str(i), padx=40, pady=20, command=num(i)))

def addCmd():
    global operation
    operation = add(int(entry.get()))
    entry.delete(0, END)
    return
def subCmd():
    global operation
    operation = sub(int(entry.get()))
    entry.delete(0, END)
    return
def mulCmd():
    global operation
    operation = mul(int(entry.get()))
    entry.delete(0, END)
    return
def divCmd():
    global operation
    operation = div(int(entry.get()))
    entry.delete(0, END)
    return
def powCmd():
    global operation
    operation = powOp(int(entry.get()))
    entry.delete(0, END)
    return
def sqrtCmd():
    global operation
    operation = lambda b: 0
    temp = int(entry.get())
    temp = int(temp ** 0.5)
    entry.delete(0, END)
    entry.insert(0, temp)
    return
def clrCmd():
    global operation
    operation = lambda b: 0
    entry.delete(0, END)
    return
def equCmd():
    global operation
    temp = operation(int(entry.get()))
    entry.delete(0, END)
    entry.insert(0, temp)
    return

buttons.append(Button(root, text="+", padx=39, pady=20, command=addCmd))
buttons.append(Button(root, text="-", padx=40, pady=20, command=subCmd))
buttons.append(Button(root, text="C", padx=39, pady=20, command=clrCmd))
buttons.append(Button(root, text="x", padx=40, pady=20, command=mulCmd))
buttons.append(Button(root, text="/", padx=40, pady=20, command=divCmd))
buttons.append(Button(root, text="x^y", padx=33, pady=20, command=powCmd))
buttons.append(Button(root, text="sqrt", padx=33, pady=20, command=sqrtCmd))
buttons.append(Button(root, text="=", padx=38, pady=20, command=equCmd))

for b in range(len(buttons)):
    buttons[b].grid(row=(int(b / 3) + 1), column=(b % 3))
buttons[len(buttons) - 1].grid(columnspan=(4 - (len(buttons) % 3)))

root.mainloop()
