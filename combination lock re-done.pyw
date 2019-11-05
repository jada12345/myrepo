from tkinter import *
from time import sleep, time as now_time
from threading import Thread
root = Tk()

root.title("Combination lock")
root.resizable(0,0)

canvas = Canvas(root, height = 300, width = 300, bg = "black")
canvas.pack()

Display = canvas.create_text(150,35, text = "", font = ("Dubai light",30), fill = "light green") #where code appears

code = "153270"

#Setting keypad numbers
counter = 1
numbers = [None,None,None,None,None,None,None,None,None,None] # empty lost to store numbers on keypad
x = 0
y = 50

numbers[0] = canvas.create_text(150,250, text = 0, font = ("Dubai light",25), fill = "white") #done by itself as doesn't follow pattern

for i in range(0,9):
	if i % 3 == 0:
		x = 0
		y += 50
	x += 75 # moves 75 pixels across for each number
	numbers[counter] = canvas.create_text(x,y, text = counter, font = ("Dubai light",25), fill = "white") #number layout
	counter += 1

def Message(Message, delay, notfinal): #used to display messages 
	canvas.itemconfig(Display, text = Message)
	sleep(delay)
	if notfinal:
		canvas.itemconfig(Display, text = "")
	else:
		sleep(1)
		canvas.itemconfig(Display, text = "Press to exit")

def Threader(function): #used to run the message code in parallel to GUI as it would freeze
	T1 = Thread(target = function)
	T1.start()

#taking in user clicks
prev_time = 0 #used to compare times for whether user is too late from previous button click

def fetch(event, number): #when user clicks number
	global prev_time
	global end
	now = now_time() #gets current time in seconds
	if now - prev_time >= 2 and len(canvas.itemcget(Display,"text")) != 0: #checks if time between last button click is more than 2 seconds then resets and also the other part is so the user is not penalized on first number entry
		Threader(lambda : Message("Too slow, repeat", 1, True)) # lambda used as requires a parameter
	else:
		x = canvas.itemcget(Display,"text") #gets currently displayed text
		new_text = x + str(number) #adds number clicked to display
		if len(new_text) >= len(code): #checks if the length of display against code, used to check code and prevent user clicking after 6 numbers
			if new_text == code: #checks if code entered is correct
				Threader(lambda : Message("Correct", 0, False))
				canvas.tag_bind(Display,"<Button-1>", lambda x: exit())
			else:
				Threader(lambda : Message("Incorrect", 1, True)) #if code is wrong
		else:
			canvas.itemconfig(Display, text = new_text) #this is if there are still more numbers to enter then that the number clicked is added to the display

	prev_time = now_time() #creates the previous time to compare on next button click

#binding number keys
canvas.tag_bind(numbers[0],"<Button-1>", lambda x: fetch(x, 0))
canvas.tag_bind(numbers[1],"<Button-1>", lambda x: fetch(x, 1))
canvas.tag_bind(numbers[2],"<Button-1>", lambda x: fetch(x, 2))
canvas.tag_bind(numbers[3],"<Button-1>", lambda x: fetch(x, 3))
canvas.tag_bind(numbers[4],"<Button-1>", lambda x: fetch(x, 4))
canvas.tag_bind(numbers[5],"<Button-1>", lambda x: fetch(x, 5))
canvas.tag_bind(numbers[6],"<Button-1>", lambda x: fetch(x, 6))
canvas.tag_bind(numbers[7],"<Button-1>", lambda x: fetch(x, 7))
canvas.tag_bind(numbers[8],"<Button-1>", lambda x: fetch(x, 8))
canvas.tag_bind(numbers[9],"<Button-1>", lambda x: fetch(x, 9))

root.mainloop()
