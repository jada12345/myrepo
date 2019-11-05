from tkinter import * 
import random
import time

## intial setup of GUI
root = Tk()
root.title("Crossroads")
root.resizable(0,0)
canvas = Canvas(root, width = 1000, height = 1000, bg = "grey")
canvas.pack()
cwidth = int(canvas.cget("width"))
cheight = int(canvas.cget("height"))

## Generating roads
RoadSize = 50 #Increasing this, increases the distance between the road lines 

## 1st part of vertical + horizontal road 
x = cwidth / 2 - RoadSize #used to find width midpoint of canvas then places it upwards by road size on canvas for the road line 
y = cheight / 2 - RoadSize #used to find height midpoint of canvas then places it upwards by road size on canvas for the road line

for i in range(2):
	canvas.create_rectangle(0,y,x,y) # first x,y is the beginning of the line, second is end of the line. 
	y += RoadSize * 2 # * 2 as this is for the second line to move first down to the midpoint, then down by Roadsize amount so it is an equal distance away from the first line
for i in range(2):
	canvas.create_rectangle(x,0,x,y - RoadSize * 4) # y - RoadSize * 4 as this is the inverse as it resets y and saves redefining the y variable
	x += RoadSize * 2 

## Horizontal road yellow lines
x = 10
y = cheight / 2 	
for i in range(x):
	canvas.create_rectangle(x, y, x + 40, y + 5, fill = "yellow")
	if i != 4:
		x += 90
	else:
		x += 210

## 2nd part of vertical + horizontal road
x = cwidth / 2 - RoadSize
y = cheight / 2 - RoadSize
for i in range(2):
	canvas.create_rectangle(x + RoadSize * 2,y,cwidth,y)
	y += RoadSize * 2
for i in range(2):
	canvas.create_rectangle(x,y - RoadSize * 2,x,cheight)
	x += RoadSize * 2

## Vertical road yellow lines
x = cwidth / 2
y = 10	
for i in range(y):
	canvas.create_rectangle(x, y, x + 5, y + 40, fill = "yellow")
	if i != 4:
		y += 90
	else:
		y += 210 

#Traffic lights
canvas.create_text(35, 15, text = "Lights", font = ("dubai light", 12, "bold italic underline")) # these are just the headers for the lights
canvas.create_text(100, 15, text = "Direction", font = ("dubai light", 12, "bold italic underline"))

lights = [None,None,None,None] 

x = 10 # x and y of first rectangle
y = 25

counter = 0 # used for second nested for loop as i value resets so it is useless to use as a incremented counter

#first loop creates rectangle border, second creates circle lights for the border 
for i in range(2):
	canvas.create_rectangle(x,y + 2,x + 50, y + 90) # first border

	for i in range(2): #creates two lights for border (red and green)
		lights[counter] = canvas.create_oval(x + 5, y + 5, x + 45, y + 45) #you can see the use for counter here as i is reset when the loop re-runs so can't asign 2 and 3 index in light array if i is used 
		
		y += 43 # spaces the next light distance
		counter += 1 

	y -= 86 #resets y for next border
	y += 100 # moves it 90 + 10 away from previous border

PossibleLightColours = ["green", "red"] #initial lights setup

def LightsSwitching(top_light): #in order for the lights to switch colour 
	if top_light == "green":
		canvas.itemconfig(lights[0], fill = "grey")
		canvas.itemconfig(lights[1], fill = "red")
		canvas.itemconfig(lights[2], fill = "green")
		canvas.itemconfig(lights[3], fill = "grey")
	else:
		canvas.itemconfig(lights[0], fill = "green")
		canvas.itemconfig(lights[1], fill = "grey")
		canvas.itemconfig(lights[2], fill = "grey")
		canvas.itemconfig(lights[3], fill = "red")

LightsSwitching(random.choice(PossibleLightColours)) #starts the first light colour

#direction indictaor arrows, these just show which car directions the lights control, helps user
canvas.create_polygon(95 , 45, 85, 60, 105, 60, fill = "black")
canvas.create_text(95, 67, text = "and", font = ("dubai light", 11))
canvas.create_polygon(95 , 90, 85, 75, 105, 75, fill = "black")

canvas.create_polygon(65 , 167, 80, 157, 80, 177, fill = "black")
canvas.create_text(95, 167, text = "and", font = ("dubai light", 11))
canvas.create_polygon(125 , 167, 110, 157, 110, 177, fill = "black")
	
#Car spawners
CarSpawners = [None,None,None,None]
Spawner0 = canvas.create_polygon(-40, cwidth / 2 - 45)
Spawner1 = canvas.create_polygon(cwidth + 40, cwidth / 2 + 48)
Spawner2 = canvas.create_polygon(cheight / 2 - 45, -40)
Spawner3 = canvas.create_polygon(cheight / 2 + 48, cheight + 40)
CarSpawners[0], CarSpawners[1], CarSpawners[2], CarSpawners[3] = Spawner0, Spawner1, Spawner2, Spawner3 # adds to car spawners list

#Car creation
Cars = {} #empty list to store currently created cars 
Colours = ["yellow","green","red","blue","pink","orange","purple"] 
NumberOfCars = 0
speeds = [10,1]

def car():
	global NumberOfCars
	
	if NumberOfCars >= 30: #limits number allowed
		pass

	else:
		Spawner = random.choice(CarSpawners) #randomly chooses a spawn
		coords = canvas.coords(Spawner) #gets coords of spawn in a list with 4 items, x,y and second x,y which are used for sizing the shape in the x and y direction 
		spawnX = coords[0] #x of spawn
		spawnY = coords[1] #y of spawn

		Sizer = 0 #used to give the car its size

		#the following is used to check which way the car will be expanded by, if 0 then needs to +40 as -40 would be off the GUI and vice versa
		if spawnX == -40 or spawnY == -40: 
			Sizer = 40

			if spawnX == cheight / 2 - 45:

				Direction = "down" #used to determine which roads the cars are on 
				MovementX = 0 #how much it moves by X amounts
				MovementY = 1 #how much it moves by Y amounts
				CrossoverCoords = cheight / 2 - RoadSize #this is the crossover point where the roads meet where the car needs to stop
				DeletionCoord = cheight #where the car has completed its travel and must be deleted
				LightIndex = 1 #which light the car obeys from the lights list
				FrontOfCarIndex = 3 #which coord indicates the front of the car its coords list
				BehindOfCarIndex = 1 #which coord indicates the back of the car its coords list

			else:
				Direction = "right"
				MovementX = 1
				MovementY = 0
				CrossoverCoords = cwidth / 2 - RoadSize
				DeletionCoord = cwidth
				LightIndex = 3
				FrontOfCarIndex = 2
				BehindOfCarIndex = 0

		elif spawnX == cwidth + 40 or spawnY == cheight + 40:
			Sizer = - 40

			if spawnX == cheight / 2 + 48:
				Direction = "up"
				MovementX = 0
				MovementY = -1
				CrossoverCoords = cheight / 2 + RoadSize
				DeletionCoord = 0
				LightIndex = 1
				FrontOfCarIndex = 1
				BehindOfCarIndex = 3

			else:
				Direction = "left"
				MovementX = -1
				MovementY = 0
				CrossoverCoords = cwidth / 2 + RoadSize
				DeletionCoord = 0
				LightIndex = 3
				FrontOfCarIndex = 0
				BehindOfCarIndex = 2

		Car = canvas.create_oval(spawnX, spawnY, spawnX + Sizer, spawnY + Sizer, fill = random.choice(Colours)) # creates the car (circle)

		Attributes = [Direction, MovementX, MovementY, CrossoverCoords, DeletionCoord, LightIndex, FrontOfCarIndex, BehindOfCarIndex] # value used for each car saved in a dictionairy to be looped around 

		Cars[str(Car)] = Attributes #adds to car dictionairy and assigns value of the list of it's personal attributes

		NumberOfCars += 1 

def move(**kwargs):
	for Car, attributes in kwargs.items(): # loops each item in car dictionary, so goes and adjysts each car spawned in one at a time
		global NumberOfCars

		#put in try as this function sometimes the function runs faster than variables below can be created and rasies an error forcing the program to crash therefore this stops it
		Coords = canvas.coords(Car) #assigning the cars attributes 
		Direction = attributes[0]
		MovementX = attributes[1] * random.choice(speeds)
		MovementY = attributes[2] * random.choice(speeds)
		CrossoverCoords = attributes[3]
		DeletionCoord = attributes[4]
		LightIndex = attributes[5]
		FrontOfCarIndex = attributes[6]
		BehindOfCarIndex = attributes[7]

		if Coords[BehindOfCarIndex] == DeletionCoord: #if the cars behind coords are == to end of its road
			#canvas.delete(Car) #then removes the car
			NumberOfCars -= 1

		else:
			if Coords[FrontOfCarIndex] == CrossoverCoords and canvas.itemcget(lights[LightIndex], "fill") == "red": #if front of car is at the crossover point and light is red 
				MovementX = 0 #stops car going right or left
				MovementY = 0 #stops car going up or down
			else:
				canvas.move(int(Car),MovementX,MovementY) #final movements done here 

		root.update() #updates GUI


def CarSpacer(Direction, XofCar, YofCar, **kwargs):
	for Cars, attributes in kwargs.items(): #runs through each car created
		if Direction == attributes[0]: #direction of car going to spawn == Car in dictionary
			if Direction == "right" or Direction == "left":
				pass
			
			else:
				pass

		else:
			SpawnOk == True
			return SpawnOk

root.update()

LightCounter = 0
delay = 0.01

while True:
	if LightCounter == (4 / delay): 
		LightsSwitching(canvas.itemcget(lights[0], "fill"))
		LightCounter = 0
	car()
	move(**Cars)
	LightCounter += 1
	time.sleep(delay)
	
root.mainloop()
#add to, spacing between cars, speed