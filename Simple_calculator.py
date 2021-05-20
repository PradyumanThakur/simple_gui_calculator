from tkinter import *
from Factorial import factorial

root = Tk()
root.title("Simple Calculator")
root.iconbitmap("images\\Favicon1.ico")
root.geometry("407x408")
root.configure(background="#363538")

e = Entry(root, width=60, borderwidth=10, bg="#363538", fg="#ffffff")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_num))
    elif math == "subtraction":
        e.insert(0, f_num - float(second_num))
    elif math == "multiplication":
        e.insert(0, f_num * float(second_num))
    elif math == "division":
        e.insert(0, f_num / float(second_num))
    elif math == "squareroot":
        e.insert(0, (f_num)**(1/2))
    elif math == "modulus":
        e.insert(0, f_num % float(second_num))
    elif math == "exponent":
        e.insert(0, f_num ** float(second_num))
    elif math == "factorial":
        e.insert(0, factorial(int(f_num)))
    else:
        e.insert(0, "Please press given button for operation.")

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_num)
    e.delete(0, END)

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_num)
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_num)
    e.delete(0, END)

def button_exponent():
    first_num = e.get()
    global f_num
    global math
    math = "exponent"
    f_num = float(first_num)
    e.delete(0, END)

def button_sqr():
    first_num = e.get()
    global f_num
    global math
    math = "squareroot"
    f_num = float(first_num)
    e.delete(0, END)

def button_mod():
    first_num = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = float(first_num)
    e.delete(0, END)

def button_factorial():
    first_num = e.get()
    global f_num
    global math
    math = "factorial"
    f_num = float(first_num)
    e.delete(0, END)

#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="#000000", fg="#ffffff", borderwidth="5", command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_add)
button_equal = Button(root, text="=", padx=40, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_equal)
button_clear = Button(root, text="C", padx=40, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20,bg="#363538", fg="#ffffff", borderwidth="5", command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_divide)
button_exponent = Button(root, text="expo", padx=30, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_exponent)
button_sqr = Button(root, text="sqrt", padx=33, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_sqr)
button_mod = Button(root, text="mod", padx=30, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_mod)
button_factorial = Button(root, text="!", padx=41, pady=20, bg="#363538", fg="#ffffff", borderwidth="5", command=button_factorial)

# Put button on screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)
button_clear.grid(row=1, column=0)
button_equal.grid(row=5, column=3)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_exponent.grid(row=1, column=1)
button_sqr.grid(row=1, column=2)
button_mod.grid(row=5, column=0)
button_factorial.grid(row=5, column=2)

root.mainloop()
