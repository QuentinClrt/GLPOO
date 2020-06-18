from tkinter import messagebox
from tkinter import *


from view.base_frame import BaseFrame
from controller.coach_controller import CoachController
from exceptions import Error

class ListCoachesFrame(BaseFrame) :
	def __init__(self, coach_controller : CoachController, main_frame : Frame):
		super().__init__(main_frame)
		self._coach_controller = coach_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="List Coaches", height=3)

		self.title.grid(row=1, column=1)

		#We list all the coaches to gather informations and send them back to the customers
		try :
			coaches = self._coach_controller.gather_informations()

			self.list_coaches = Text(self, width=90, height=10)

			for i in coaches :
				self.list_coaches.insert(END, "ID : "+i[0]+'\n'+ "Email : "+i[1]+'\n'+ "Phone number : "+str(i[2])+ '\n'+ "Lastname : "+i[3]+'\n\n')

			self.list_coaches.grid(row=2, column=2)

		except Error as e:
			messagebox.showerror("Error", str(e))