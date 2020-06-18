from tkinter import messagebox
from tkinter import *


from view.base_frame import BaseFrame
from controller.gym_controller import GymController
from exceptions import Error

class CreateGymFrame(BaseFrame) :
	def __init__(self, gym_controller : GymController, main_frame : Frame):
		super().__init__(main_frame)
		self._gym_controller = gym_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="New Gym", height=3)

		self.name = self.create_entry("Name : ", row=2, columnspan=2)
		self.phone_number = self.create_entry("Phone number : ", row=3, columnspan=4)
		self.address = self.create_entry("Address : ", row=4, columnspan=6)

		#machines to list

		#coaches to list



		self.validate = Button(self, bg="green", fg="white", text="Validate", width=14, height=1, pady=4, padx=10, command=self.validate)

		self.title.grid(row=1, column=1)
		self.name.grid(row=2, column=1)
		self.phone_number.grid(row=3, column=1)
		self.address.grid(row=4, column=1)
		self.validate.grid(row=5, column=2)


	def validate(self) :

		data = {
			"name" : "Basic Gym",
			"phone_number" : "0123456789",
			"address" : "Somewhere",
			"machines" : [],
			"coaches" : []
		}

		data['name'] = self.name.get()
		data['phone_number'] = self.phone_number.get()
		data['address'] = self.address.get()

		try:
			self._gym_controller.create_gym(data)
			messagebox.showinfo("Success", "Gym added !")

		except Error as e:
			messagebox.showerror("Error", str(e))
			return

		self.show_menu()