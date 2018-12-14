import tkinter as tk
from PIL import Image, ImageTk
import time

class Base(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.shared_data = {
			"Name": tk.StringVar(),
			"Class": tk.StringVar(),
			"Choice": tk.StringVar()
		}

		self.stats = {
			"Strength": tk.StringVar(),
			"Defence": tk.StringVar(),
			"Agility": tk.StringVar(),
			"Health": tk.StringVar(),
			"Max_Health": tk.StringVar(),
			"Money": tk.StringVar()
		}

		self.monster = {
			"Monster": tk.StringVar(),
		}

		self.bandit = {
			"Strength": 7,
			"Defence": 7,
			"Agility": 7,
			"Health": 27
		}

		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (Introduction, Main):
			frame = F(container, self)
			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(Introduction)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	def get_page(self, page_name):
		return self.frames[page_name]

class Introduction(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller=controller

		label=tk.Label(self, text="What is your first name:       ", bg="#b3b3ff")
		label.grid(row=0,column=0)

		name = tk.Entry(self, textvariable=self.controller.shared_data["Name"])
		name.grid(row=0, column=1)

		pclass = tk.Label(self, text="What weapon do you want to use", bg="#b3b3ff")
		pclass.grid(row=1, column=0)

		var = tk.StringVar(self)
		choices = {'Sword', 'Bow'}
		var.set("Sword")

		dropdown = tk.OptionMenu(self, var, *choices, command=self.func)
		dropdown.grid(row=1, column=1)

		main = tk.Button(self, text="Moving on to the real game", command=lambda: controller.show_frame(Main))
		main.grid(row=2, column=1)

	def func(self, value):
		self.controller.shared_data['Class'] = value

class Main(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller=controller
		
		Name = self.controller.shared_data['Name'].get()
		Class = self.controller.shared_data['Class']

		self.controller.stats['Money'] = 20

		if Class == "Sword":
			self.controller.stats['Strength'] = 10
			self.controller.stats['Agility'] = 7
			self.controller.stats['Defence'] = 12
			self.controller.stats['Health'] = 40
			self.controller.stats['Max_Health'] = 40
		else:
			self.controller.stats['Strength'] = 15
			self.controller.stats['Agility'] = 12
			self.controller.stats['Defence'] = 7
			self.controller.stats['Health'] = 30
			self.controller.stats['Max_Health'] = 30

		choice1 = tk.Button(self, text = "Choice 1", bg="#b3b3ff", command=lambda: self.chosen1(1))
		choice2 = tk.Button(self, text = "Choice 2", bg="#b3b3ff", command=lambda: self.chosen1(2))
		choice3 = tk.Button(self, text = "Choice 3", bg="#b3b3ff", command=lambda: self.chosen1(3))
		choice4 = tk.Button(self, text = "Choice 4", bg="#b3b3ff", command=lambda: self.chosen1(4))

		self.story = tk.Text(self, relief="groove", bg="#C8D0FF")
		self.story.configure(state="disabled")
		#python3 NewGame.py
		img = ImageTk.PhotoImage(Image.open("Sword.jpeg"))
		image = tk.Label(self, image=img, height=50, width=50)
		self.stats = tk.Text(self, relief="groove", bg="#C8D0FF")
		self.stats.configure(state="disabled")

		self.stat_reset()

		self.story.grid(row=0, column=0)
		image.grid(row=4, column=1)
		self.stats.grid(row=0, column=1)

		choice1.grid(row=1, column=0, pady=10, padx=10)
		choice2.grid(row=1, column=1)
		choice3.grid(row=2, column=0)
		choice4.grid(row=2, column=1)

		self.story.configure(state='normal')
		self.story.insert(tk.INSERT, "Hello there. Welcome to 'The Hero's Journey'\n")
		self.story.insert(tk.INSERT, "a game that teaches you how to become an hero \n")
		self.story.insert(tk.INSERT, "Random Plot that I can add later\n")
		self.story.insert(tk.INSERT, "You get attacked by a bandit! Do you either: \n")
		self.story.insert(tk.INSERT, "Choice 1: FIght, \n")
		self.story.insert(tk.INSERT, "Choice 2: Flee, \n")
		self.story.insert(tk.INSERT, "Choice 3: Bargain, \n")
		self.story.insert(tk.INSERT, "Choice 4: Intimidate\n")
		self.story.configure(state='disabled')
		self.controller.shared_data['monster'] = "Bandit"


	def chosen1(self, number):
		MainStory = self.controller.get_page(Main)
		story = MainStory.story.get("1.0", "end-1c")

		if number == 1:
			MainStory.story.configure(state='normal')
			self.controller.monster['Monster'] = "Bandit"
			#Base.show_frame(Attack)

		elif number == 2:
			MainStory.story.configure(state='normal')
			if self.controller.stats['Agility'] > self.controller.bandit['Agility']:
				MainStory.story.insert("end", "You ran away successfully")
			else:
				MainStory.story.insert("end", "You didn't ran away successfully, and was forced to fight the bandit")

		elif number == 3:
			MainStory.story.configure(state='normal')
			self.controller.stats['Money'] = 0
			MainStory.story.insert("end", "The bandit took all of your money")

		elif number ==4:
			MainStory.story.configure(state='normal')
			if self.controller.stats['Strength'] > self.controller.bandit['Strength']:
				MainStory.story.insert("end", "Your intimidation worked, the bandit ran away \n")
				time.sleep(0.2)

	def stat_reset(self):
		self.stats.config(state = "normal")
		self.stats.delete('1.0', tk.END)

		self.stats.insert(tk.INSERT, "Strength: {0} \n".format(self.controller.stats['Strength']))
		self.stats.insert(tk.INSERT, "Defence: {0} \n".format(self.controller.stats['Agility']))
		self.stats.insert(tk.INSERT, "Agility: {0} \n".format(self.controller.stats['Defence']))
		self.stats.insert(tk.INSERT, "Health: {0} \n".format(self.controller.stats['Health']))

		self.stats.configure(state="disabled")

		#1) The colour selection is ascetically pleasing and results in easy readability
		#2) The User can easily understand the usage of GUI (Buttons etc) 
		#3) The base code is clean and concise 

'''
class Attack(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller	

		attack = tk.Button(self, text='Attack', command=self.on_click(1))
		item = tk.Button(self, text='Item', command=self.on_click(2))
		
		if self.controller.shared_data['Class'] == "Sword":
			picture = ['Sword1', 'Sword2', 'Sword3']
		else:
			picture = ['Bow1', 'Bow2', 'Bow3']

		if self.controller.monster['Monster'] == 'Bandit':
			picture2 = ['Bandit1', 'Bandit2', 'Bandit3']
		else:
			picutre2 = ['Goblin1', 'Goblin2', 'Goblin3']

		namel = tk.Label(self, text=self.controller.shared_data['Name'].get())
		enemyl = tk.Label(self, text=self.controller.shared_data['monster'])

		img1 = ImageTk.PhotoImage(Image.open(picture[0]))
		characteri = tk.Label(self, image=img1)

		img2 = ImageTk.PhotoImage(Image.open(picture2[0]))
		banditi = tk.Label(self, image=img2)

		namel.grid(row=0, column=0)
		enemyl.grid(row=0, column=1)

		characteri.grid(row=1, column=0)
		banditi.grid(row=1, column=1)

		attack.grid(row=2, column=0)
		item.grid(row=2, column=1)

	def on_click(self, integer):
		if integer == 1:
			attack.configure(text='Swing')
			item.configure(text='Jab')
		elif integer == 2:
			attack.configure(text='Health Pot', command=on_click(3))
			item.configure(text='Big health pot', command=on_click(4))
		elif integer == 3:
			self.controller.stats['Health']+= 10
		elif integer == 4:
			self.controller.stats['Health']+=20


		#img = ImageTk.PhotoImage(Image.open("Sword.gif"))
		#self.image = tk.Label(self.root, image=img)
'''


app=Base()
app.mainloop()