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

		self.visited = []
		self.counter = 0
		self.bulb = 0
		self.room = Label(self.window, image=self.off)
		self.room.place(x=50,y=250)

		self.counter_value = Label(self.window, text="Counter: "+str(self.counter), font=("bold", 15))
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

	def create_prisoners(self, n):
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
		self.counter = 0
		self.selected = 0
		self.counter_value.configure(text="Counter: "+str(self.counter))
		if self.all_prisoners:
			for i in range(len(self.all_prisoners)):
				self.all_prisoners[i].destroy()
			self.all_prisoners = []

	def perform_Ncounter(self, n):

		if self.state == 0:
			self.selected = random.randint(0,n-1)
			self.all_prisoners[self.selected].configure(image='')
			self.state = 1
			self.window.after(1500, self.perform_Ncounter, n)

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

			self.counter_value.configure(text="Counter: "+str(self.counter))

			if self.counter < n:
				self.state = 0
				self.window.after(1500, self.perform_Ncounter, n)	
			else:
				self.counter_value.configure(text="Counter: "+str(self.counter)+" Finished!!!")
				print("Done!!")
			
			self.all_prisoners[self.selected].configure(image=self.prisoner_done)

	def start(self):
		self.refresh()
		self.room.configure(image=self.off)

		try:
			n = int(self.n_fn.get())
			self.create_prisoners(n)
			self.window.after(1500, self.perform_Ncounter, n)

			# perform_improved()
		except:
			print("Enter a valid value for n")

	def end(self):
		exit()


if __name__ == "__main__":
	demo = Demo()