from tkinter import messagebox
from tkinter import *


from view.base_frame import BaseFrame
from controller.machine_controller import MachineController
from exceptions import Error

class CreateMachineFrame(BaseFrame) :
	def __init__(self, machine_controller : MachineController, main_frame : Frame):
		super().__init__(main_frame)
		self._machine_controller = machine_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="New Machine", height=3)

		self.title.grid(row=1, column=1)

		self.name = self.create_entry("Name : ", row=2, columnspan=2)
		self.brand = self.create_entry("Brand : ", row=3, columnspan=4)
		self.provider = self.create_entry("Provider : ", row=4, columnspan=6)
		self.muscular_group = self.create_entry("Muscular group : ", row=5, columnspan=8)
		self.validate = Button(self, bg="green", fg="white", text="Validate", width=14, height=1, pady=4, padx=10, command=self.validate)

		self.name.grid(row=2, column=1)
		self.brand.grid(row=3, column=1)
		self.provider.grid(row=4, column=1)
		self.muscular_group.grid(row=5, column=1)
		self.validate.grid(row=7, column=2)

		#gym to attribute to the machine

	def validate(self) :

		data = {
			"name" : "Anonymous",
			"brand" : "Anonymous",
			"provider" : "Anonymous",
			"muscular_group" : "Legs"
		}

		data['name'] = self.name.get()
		data['brand'] = self.brand.get()
		data['provider'] = self.provider.get()
		data['muscular_group'] = self.muscular_group.get()

		try:
			self._machine_controller.create_machine(data)
			messagebox.showinfo("Success", "Machine created !")

		except Error as e:
			messagebox.showerror("Error", str(e))
			return

		self.show_menu()