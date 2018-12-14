import tkinter as tk
from PIL import Image, ImageTk

class Base(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.shared_data = {
            "Name": tk.StringVar(),
            "Class": tk.StringVar()
        }

		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		
		frame = Introduction(container, self)
		self.frames[Introduction] = frame

		frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(Introduction)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

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

		main = tk.Button(self, text="Moving on to the real game", command=lambda: self.submit())
		main.grid(row=2, column=1)

	def func(self, value):
		self.controller.shared_data['Class'] = value

	def submit(self):
		Name = self.controller.shared_data['Name'].get()
		Class = self.controller.shared_data['Class']
		print(Name)
		print(Class)



app=Base()
app.mainloop()
