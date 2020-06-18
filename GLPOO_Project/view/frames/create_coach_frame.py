from tkinter import messagebox
from tkinter import *


from view.base_frame import BaseFrame
from controller.coach_controller import CoachController
from exceptions import Error

class CreateCoachFrame(BaseFrame) :
	def __init__(self, coach_controller : CoachController, main_frame : Frame):
		super().__init__(main_frame)
		self._coach_controller = coach_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="New coach", height=3)

		self.title.grid(row=1, column=1)


		self.firstname = self.create_entry("Firstname : ", row=2, columnspan=2)
		self.lastname = self.create_entry("Lastname : ", row=3, columnspan=4)
		self.email = self.create_entry("Email : ", row=4, columnspan=6)
		self.phone_number = self.create_entry("Phone Number : ", row=5, columnspan=8)
		self.degree = self.create_entry("Degree : ", row=6, columnspan=10)
		self.specialties = self.create_entry("Specialties : ", row=7, columnspan=12)

		self.validate = Button(self, bg="green", fg="white", text="Validate", width=14, height=1, pady=4, padx=10, command=self.validate)

		self.firstname.grid(row=2, column=1)
		self.lastname.grid(row=3, column=1)
		self.email.grid(row=4, column=1)
		self.phone_number.grid(row=5, column=1)
		self.degree.grid(row=6, column=1)
		self.specialties.grid(row=7, column=1)
		self.validate.grid(row=8, column=2)

		#gym to attribute to the coach

	def validate(self) :

		data = {
			"firstname" : "Anonymous",
			"lastname" : "Anonymous",
			"email" : "Anonymous",
			"phone_number" : "0666666666",
			"degree" : "Unknown",
			"specialties" : "Training"
		}

		data['firstname'] = self.firstname.get()
		data['lastname'] = self.lastname.get()
		data['email'] = self.email.get()
		data['phone_number'] = self.phone_number.get()
		data['degree'] = self.degree.get()
		data['specialties'] = self.specialties.get()

		try:
			self._coach_controller.create_coach(data)
			messagebox.showinfo("Success", "Coach added !")

		except Error as e:
			messagebox.showerror("Error", str(e))
			return

		self.show_menu()