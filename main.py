from tkinter import *
from PIL import Image, ImageTk
import math
import random
import time

class Demo():

	def __init__(self):
		self.window = Tk()
		self.window.geometry("1000x700")
		self.window.title("Demo for n-prisoner & light bulb")
		self.load_images()
		
		self.state = 0

		self.prison_space = {"start_x" : 150, "end_x" : 950, "start_y" : 150, "end_y" : 550}
		self.all_prisoners = []

		self.n_fn = StringVar()
		self.n_label = Label(self.window, text="Enter number of prisoners (n) :", font=("bold", 15))
		self.n_label.place(x=50,y=75)

		self.n_value = Entry(self.window, width=10, relief="solid", textvar=self.n_fn)
		self.n_value.place(x=375,y=75)

		self.v = IntVar()
		self.v.set(1)
		self.strat_radio1 = Radiobutton(self.window, text="Strategy 1", variable=self.v, value=1)
		self.strat_radio1.place(x=370,y=100)
		self.strat_radio2 = Radiobutton(self.window, text="Strategy 2", variable=self.v, value=2)
		self.strat_radio2.place(x=370,y=120)

		self.interval = IntVar()
		self.interval.set(1500)
		self.strat_radio1 = Radiobutton(self.window, text="Slow", variable=self.interval, value=3000)
		self.strat_radio1.place(x=300,y=560)
		self.strat_radio2 = Radiobutton(self.window, text="Normal", variable=self.interval, value=1500)
		self.strat_radio2.place(x=400,y=560)
		self.strat_radio2 = Radiobutton(self.window, text="Fast", variable=self.interval, value=750)
		self.strat_radio2.place(x=500,y=560)
		self.strat_radio2 = Radiobutton(self.window, text="Crazy fast", variable=self.interval, value=50)
		self.strat_radio2.place(x=600,y=560)

		self.visited = []
		self.done = []
		self.counter = 0
		self.days = 0
		self.all_counters = []
		self.bulb = 0
		self.room = Label(self.window, image=self.off)
		self.room.place(x=50,y=250)

		self.days_passed = Label(self.window, text="Days passed: "+str(self.days), font=("bold", 15))
		self.days_passed.place(x=575, y=100)

		self.counter_value = Label(self.window, text="Global Counter: "+str(self.counter), font=("bold", 15))
		self.counter_value.place(x=575, y=75)
		
		self.s_button = Button(self.window, text="Start", fg="black", bg="brown", command=self.start, relief=GROOVE, font=("ariel",12,"bold")).place(x=300,y=600)
		self.e_button = Button(self.window, text="Exit", fg="black", bg="brown", command=self.end, relief=GROOVE, font=("ariel",12,"bold")).place(x=600,y=600)

		self.window.mainloop()

	def load_images(self):

		self.off_img = Image.open("./off.png")
		self.off_img = self.off_img.resize((75, 75), Image.ANTIALIAS)
		self.off = ImageTk.PhotoImage(self.off_img)

		self.on_img = Image.open("./on.png")
		self.on_img = self.on_img.resize((75, 75), Image.ANTIALIAS)
		self.on = ImageTk.PhotoImage(self.on_img)

		self.star_img = Image.open("./star.png")
		self.star_img = self.star_img.resize((12, 12), Image.ANTIALIAS)
		self.star = ImageTk.PhotoImage(self.star_img)

		self.prisoner_img = Image.open("./prisoner.png")
		self.prisoner_img = self.prisoner_img.resize((50, 60), Image.ANTIALIAS)
		self.prisoner = ImageTk.PhotoImage(self.prisoner_img)

		self.prisoner_star = Image.open("./counter.png")
		self.prisoner_star = self.prisoner_star.resize((50, 60), Image.ANTIALIAS)
		self.prisoner_counter = ImageTk.PhotoImage(self.prisoner_star)

		self.prisoner_done_img = Image.open("./done.png")
		self.prisoner_done_img = self.prisoner_done_img.resize((50, 60), Image.ANTIALIAS)
		self.prisoner_done = ImageTk.PhotoImage(self.prisoner_done_img)

	def create_prisoners(self, n, strat):
		if n <=100:
			flag = 0
			rows = columns = math.ceil((math.sqrt(n)))
			dist_x = (self.prison_space["end_x"] - self.prison_space["start_x"]) / rows
			dist_y = (self.prison_space["end_y"] - self.prison_space["start_y"]) / columns

			for i in range(rows):
				for j in range(columns):
					if i==j==0:
						star_label = Label(self.window, image=self.star)
						star_label.place(x=self.prison_space["start_x"]+17+dist_x*j, y=self.prison_space["start_y"]-15+dist_y*i)

					if strat == 2:
						c = Label(self.window, text=str(0), font=("bold", 15))
						c.place(x=self.prison_space["start_x"]-15+dist_x*j, y=self.prison_space["start_y"]+17+dist_y*i)
						self.all_counters.append([c,0,0])

					bad_ppl = Label(self.window, image=self.prisoner)
					bad_ppl.place(x=self.prison_space["start_x"]+dist_x*j, y=self.prison_space["start_y"]+dist_y*i)
					self.all_prisoners.append(bad_ppl)
					flag = flag + 1
					
					if flag == n:
						break
				
				else:
					continue

				break

		else:
			print("Enter n<=100")

	def refresh(self):
		self.state = 0
		self.visited = []
		self.done = []
		self.done.append(0)
		self.counter = 0
		self.selected = 0
		self.days = 0
		self.days_passed.configure(text="Days passed: "+str(self.days))
		self.counter_value.configure(text="Global Counter: "+str(self.counter))
		if self.all_prisoners:
			for i in range(len(self.all_prisoners)):
				self.all_prisoners[i].destroy()
			self.all_prisoners = []

		if self.all_counters:
			for i in range(len(self.all_counters)):
				self.all_counters[i][0].destroy()
			self.all_counters = []

	def perform_Ncounter(self, n):
		if self.state == 0:
			self.selected = random.randint(0,n-1)
			self.all_prisoners[self.selected].configure(image='')
			self.state = 1
			self.days += 1
			self.days_passed.configure(text="Days passed: "+str(self.days))
			self.window.after(self.interval.get(), self.perform_Ncounter, n)

		elif self.state == 1:
			if self.selected not in self.visited:
				if self.selected == 0:
					self.counter = self.counter + 1
					self.visited.append(self.selected)
				elif self.bulb == 0:
					self.room.configure(image=self.on)
					self.visited.append(self.selected)
					self.bulb = 1

			if self.selected == 0:
				if self.bulb == 1:
					self.counter = self.counter + 1
					self.bulb = 0
					self.room.configure(image=self.off)

			self.counter_value.configure(text="Global Counter: "+str(self.counter))

			if self.counter < n:
				self.state = 0
				self.window.after(self.interval.get(), self.perform_Ncounter, n)	
			else:
				self.counter_value.configure(text="Global Counter: "+str(self.counter)+" Finished!!!")
			
			self.all_prisoners[self.selected].configure(image=self.prisoner_done)

	def perform_improved(self, n):
		if self.state == 0:
			self.selected = random.randint(0,n-1)
			self.all_prisoners[self.selected].configure(image='')
			self.state = 1
			self.days += 1
			self.days_passed.configure(text="Days passed: "+str(self.days))
			self.window.after(self.interval.get(), self.perform_improved, n)

		elif self.state == 1:
			[label,pc,prev_state] = self.all_counters[self.selected]

			if self.selected not in self.visited:
				if self.selected == 0:
					self.visited.append(self.selected)
				elif self.bulb == 0:
					pc = pc + 1
					self.room.configure(image=self.on)
					self.visited.append(self.selected)
					self.bulb = 1
				elif self.bulb == 1:
					if prev_state == 0:
						pc = pc + 1
			elif self.bulb == 1:
				if self.selected !=0:
					if prev_state == 0:
						pc = pc + 1

			if self.selected == 0:
				if self.bulb == 1:
					pc = pc + 1
					self.bulb = 0
					self.room.configure(image=self.off)


			prev_state = self.bulb
			label.configure(text=str(pc))
			self.all_counters[self.selected] = [label,pc,prev_state]
			self.counter_value.configure(text="Global Counter: "+str(self.all_counters[0][1]))

			if pc < n - 1:
				self.state = 0
				self.window.after(self.interval.get(), self.perform_improved, n)				
			else:
				self.counter_value.configure(text="Prisoner "+str(self.selected+1)+" has made the announcement, everyone is free!!")
						
			self.all_prisoners[self.selected].configure(image=self.prisoner_done)


	def start(self):
		self.refresh()
		self.room.configure(image=self.off)

		try:
			n = int(self.n_fn.get())
			strategy = self.v.get()
			self.create_prisoners(n,strategy)

			if strategy == 1:
				self.window.after(self.interval.get(), self.perform_Ncounter, n)
			elif strategy == 2:
				self.window.after(self.interval.get(), self.perform_improved, n)
		except:
			print("Enter a valid value for n")

	def end(self):
		exit()


if __name__ == "__main__":
	demo = Demo()