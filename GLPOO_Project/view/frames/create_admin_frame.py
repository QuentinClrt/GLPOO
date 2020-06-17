
from tkinter import messagebox
from tkinter import *

from view.base_frame import BaseFrame
from controller.admin_controller import AdminController
from exceptions import Error

class CreateAdminFrame(BaseFrame) :

	def __init__(self, admin_controller : AdminController, main_frame : Frame):
		super().__init__(main_frame)
		self._admin_controller = admin_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Admin creation", height=3)
		self.login = self.create_entry("Email (=login) : ", row=2, columnspan=2)
		self.password = self.create_entry("Password : ", row=3, columnspan=4)
		self.firstname = self.create_entry("Firstname : ", row=4, columnspan=6)
		self.lastname = self.create_entry("Lastname : ", row=5, columnspan=8)
		self.phone_number = self.create_entry("Phone number : ", row=6, columnspan=10)
		self.validate = Button(self, bg="green", fg="white", text="Validate", width=14, height=1, pady=4, padx=10, command=self.validate)

		self.title.grid(row=1, column=1)
		self.login.grid(row=2, column=1)
		self.password.grid(row=3, column=1)
		self.firstname.grid(row=4, column=1)
		self.lastname.grid(row=5, column=1)
		self.phone_number.grid(row=6, column=1)
		self.validate.grid(row=7, column=2)

	def validate(self) :

		data = {
			"login" : "Anonymous",
			"password" : "Anonymous",
			"firstname" : "Anonymous",
			"lastname" : "Anonymous",
			"phone_number" : "0666666666"
		}

		data['login'] = self.login.get()
		data['password'] = self.password.get()
		data['firstname'] = self.firstname.get()
		data['lastname'] = self.lastname.get()
		data['phone_number'] = self.phone_number.get()

		try:
			validated_data = self._admin_controller.create_admin(data)
			messagebox.showinfo("Success", "Administrator created !")

		except Error as e:
			messagebox.showerror("Error", str(e))
			return

		self.show_menu()