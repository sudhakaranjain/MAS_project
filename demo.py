from tkinter import *
from PIL import Image, ImageTk
import math

window = Tk()
window.geometry("1000x700")
window.title("Demo for n-prisoner & light bulb")

prison_space = {"start_x" : 150, "end_x" : 950, "start_y" : 125, "end_y" : 550}
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

prisoner_img = Image.open("./prisoner.png")
prisoner_img = prisoner_img.resize((50, 60), Image.ANTIALIAS)
prisoner = ImageTk.PhotoImage(prisoner_img)

prisoner_star = Image.open("./counter.png")
prisoner_star = prisoner_star.resize((50, 60), Image.ANTIALIAS)
prisoner_counter = ImageTk.PhotoImage(prisoner_star)

room = Label(window, image=off)
room.place(x=50,y=250)

def create_prisoners(n):
	if n <=100:
		prison = []
		counter = 0
		rows = columns = math.ceil((math.sqrt(n)))
		dist_x = (prison_space["end_x"] - prison_space["start_x"]) / rows
		dist_y = (prison_space["end_y"] - prison_space["start_y"]) / columns

		for i in range(rows):
			for j in range(columns):
				if i==j==0:
					bad_ppl = Label(window, image=prisoner_counter)
				else:
					bad_ppl = Label(window, image=prisoner)

				bad_ppl.place(x=prison_space["start_x"]+dist_x*j, y=prison_space["start_y"]+dist_y*i)
				all_prisoners.append(bad_ppl)
				counter = counter + 1
				
				if counter == n:
					break
			
			else:
				continue

			break

	else:
		print("Enter n<=100")

def refresh():
	global all_prisoners
	if all_prisoners:
		for i in range(len(all_prisoners)):
			all_prisoners[i].destroy()
		all_prisoners = []

def start():
	refresh()
	room.configure(image=off)
	try:
		n = int(n_fn.get())
		create_prisoners(n)
	except:
		print("n should be an integer")

def end():
	exit()

s_button = Button(window, text="Start", fg="black", bg="brown", command=start, relief=GROOVE, font=("ariel",12,"bold")).place(x=300,y=600)
e_button = Button(window, text="Exit", fg="black", bg="brown", command=end, relief=GROOVE, font=("ariel",12,"bold")).place(x=600,y=600)

window.mainloop()