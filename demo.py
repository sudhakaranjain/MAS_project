from tkinter import *
from PIL import Image, ImageTk
import math
import random
import time

window = Tk()
window.geometry("1000x700")
window.title("Demo for n-prisoner & light bulb")

state = 0

prison_space = {"start_x" : 150, "end_x" : 950, "start_y" : 150, "end_y" : 550}
all_prisoners = []

n_fn = StringVar()
n_label = Label(window, text="Enter number of prisoners (n) :", font=("bold", 15))
n_label.place(x=50,y=75)

n_value = Entry(window, width=10, relief="solid", textvar=n_fn)
n_value.place(x=375,y=75)

off_img = Image.open("./off.png")
off_img = off_img.resize((75, 75), Image.ANTIALIAS)
off = ImageTk.PhotoImage(off_img)

on_img = Image.open("./on.png")
on_img = on_img.resize((75, 75), Image.ANTIALIAS)
on = ImageTk.PhotoImage(on_img)

star_img = Image.open("./star.png")
star_img = star_img.resize((12, 12), Image.ANTIALIAS)
star = ImageTk.PhotoImage(star_img)

prisoner_img = Image.open("./prisoner.png")
prisoner_img = prisoner_img.resize((50, 60), Image.ANTIALIAS)
prisoner = ImageTk.PhotoImage(prisoner_img)

prisoner_star = Image.open("./counter.png")
prisoner_star = prisoner_star.resize((50, 60), Image.ANTIALIAS)
prisoner_counter = ImageTk.PhotoImage(prisoner_star)

prisoner_done_img = Image.open("./done.png")
prisoner_done_img = prisoner_done_img.resize((50, 60), Image.ANTIALIAS)
prisoner_done = ImageTk.PhotoImage(prisoner_done_img)

visited = []
counter = 0
bulb = 0
room = Label(window, image=off)
room.place(x=50,y=250)

counter_value = Label(window, text="Counter: "+str(counter), font=("bold", 15))
counter_value.place(x=575, y=75)

def create_prisoners(n):
	if n <=100:
		flag = 0
		rows = columns = math.ceil((math.sqrt(n)))
		dist_x = (prison_space["end_x"] - prison_space["start_x"]) / rows
		dist_y = (prison_space["end_y"] - prison_space["start_y"]) / columns

		for i in range(rows):
			for j in range(columns):
				if i==j==0:
					star_label = Label(window, image=star)
					star_label.place(x=prison_space["start_x"]+17+dist_x*j, y=prison_space["start_y"]-15+dist_y*i)

				bad_ppl = Label(window, image=prisoner)
				bad_ppl.place(x=prison_space["start_x"]+dist_x*j, y=prison_space["start_y"]+dist_y*i)
				all_prisoners.append(bad_ppl)
				flag = flag + 1
				
				if flag == n:
					break
			
			else:
				continue

			break

	else:
		print("Enter n<=100")

def refresh():
	global all_prisoners
	global counter
	global visited
	global state
	global counter_value
	state = 0
	visited = []
	counter = 0
	counter_value.configure(text="Counter: "+str(counter))
	if all_prisoners:
		for i in range(len(all_prisoners)):
			all_prisoners[i].destroy()
		all_prisoners = []

def perform_Ncounter(n):
	global bulb
	global visited
	global counter
	global selected
	global state
	
	if state == 0:
		selected = random.randint(0,n-1)
		all_prisoners[selected].configure(image='')
		state = 1
		window.after(1500, perform_Ncounter, n)

	elif state == 1:
		if selected not in visited:
			if selected == 0:
				counter = counter + 1
				visited.append(selected)
			elif bulb == 0:
				room.configure(image=on)
				visited.append(selected)
				bulb = 1

		if selected == 0:
			if bulb == 1:
				counter = counter + 1
				bulb = 0
				room.configure(image=off)

		counter_value.configure(text="Counter: "+str(counter))

		if counter < n:
			state = 0
			window.after(1500, perform_Ncounter, n)	
		else:
			counter_value.configure(text="Counter: "+str(counter)+" Finished!!!")
			print("Done!!")

		all_prisoners[selected].configure(image=prisoner_done)


def start():
	refresh()
	room.configure(image=off)
	n = int(n_fn.get())
	create_prisoners(n)
	window.after(1500, perform_Ncounter, n)
	# try:

	# 	# perform_improved()
	# except:
	# 	print("n should be an integer")

def end():
	exit()

s_button = Button(window, text="Start", fg="black", bg="brown", command=start, relief=GROOVE, font=("ariel",12,"bold")).place(x=300,y=600)
e_button = Button(window, text="Exit", fg="black", bg="brown", command=end, relief=GROOVE, font=("ariel",12,"bold")).place(x=600,y=600)

window.mainloop()