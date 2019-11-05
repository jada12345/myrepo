from tkinter import *
import random
import time

root = Tk()
root.title("Combination lock")
root.wm_attributes("-topmost",1)
canvas = Canvas(root, width = 550, height = 100)
canvas.pack()

x1 = 55 
x2 = 100
number = 1

up_arrow = canvas.create_polygon(27.5,10,5,42.5,50,42.5)
down_arrow = canvas.create_polygon(5,47.5,50,47.5,27.5,80)

for i in range(0,9):
    num_background = canvas.create_rectangle(x1,25,x2,75)
    x1 += 55
    x2 += 55

num1 = canvas.create_text(77.5,50, text = random.randint(0,9), font = ("calibri",15))
num2 = canvas.create_text(132.5,50, text = random.randint(0,9), font = ("calibri",15))
num3 = canvas.create_text(187.5,50, text = random.randint(0,9), font = ("calibri",15))
num4 = canvas.create_text(242.5,50, text = random.randint(0,9), font = ("calibri",15))
num5 = canvas.create_text(297.5,50, text = random.randint(0,9), font = ("calibri",15))
num6 = canvas.create_text(352.5,50, text = random.randint(0,9), font = ("calibri",15))
num7 = canvas.create_text(407.5,50, text = random.randint(0,9), font = ("calibri",15))
num8 = canvas.create_text(462.5,50, text = random.randint(0,9), font = ("calibri",15))
num9 = canvas.create_text(517.5,50, text = random.randint(0,9), font = ("calibri",15))

code_for_lock = "112347383"

def current_numbers(num):
    number = canvas.itemcget(num, "text")
    return number

def selection(event, num):
    global number
    canvas.itemconfig(number, fill = "black")
    number = num
    canvas.itemconfig(number, fill = "red")
    canvas.update()

def num_selector(event, direction):
    try:
        current_number = int(canvas.itemcget(number, "text"))
        if direction == "up":
            if current_number == 9:
                canvas.itemconfig(number, text = "0")
            else:
                current_number += 1
                canvas.itemconfig(number, text = str(current_number))
        else:
            if current_number == 0:
                canvas.itemconfig(number, text = "9")
            else:
                current_number -= 1
                canvas.itemconfig(number, text = str(current_number))
    except Exception:
        pass
    
canvas.tag_bind(num1, "<Button-1>", lambda x: selection(x, num1))
canvas.tag_bind(num2, "<Button-1>", lambda x: selection(x, num2))
canvas.tag_bind(num3, "<Button-1>", lambda x: selection(x, num3))
canvas.tag_bind(num4, "<Button-1>", lambda x: selection(x, num4))
canvas.tag_bind(num5, "<Button-1>", lambda x: selection(x, num5))
canvas.tag_bind(num6, "<Button-1>", lambda x: selection(x, num6))
canvas.tag_bind(num7, "<Button-1>", lambda x: selection(x, num7))
canvas.tag_bind(num8, "<Button-1>", lambda x: selection(x, num8))
canvas.tag_bind(num9, "<Button-1>", lambda x: selection(x, num9))
canvas.tag_bind(up_arrow, "<Button-1>", lambda x: num_selector(x, "up"))
canvas.tag_bind(down_arrow, "<Button-1>", lambda x: num_selector(x, "down"))

while True:
    try:
        n1 = current_numbers(num1)
        n2 = current_numbers(num2)
        n3 = current_numbers(num3)
        n4 = current_numbers(num4)
        n5 = current_numbers(num5)
        n6 = current_numbers(num6)
        n7 = current_numbers(num7)
        n8 = current_numbers(num8)
        n9 = current_numbers(num9)
        currentcode = n1+n2+n3+n4+n5+n6+n7+n8+n9
        if currentcode == code_for_lock:
            break
        root.update()
        root.update_idletasks()
        time.sleep(0.01)
    except Exception:
        pass
    
print("correct")
root.mainloop()
