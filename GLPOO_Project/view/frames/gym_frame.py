from tkinter import *

from view.base_frame import BaseFrame
from controller.gym_controller import GymController

class GymFrame(BaseFrame) :

	def __init__(self, gym_controller : GymController, main_frame : Frame):
		super().__init__(main_frame)
		self._gym_controller = gym_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Gym", height=3)
		self.title2=Label(self, text="Informations", height=3)


		self.coach_create = Button(self, bg="grey", fg="white", text="New Coach", width=25, height=2, pady=6, padx=15, command=self._main_frame.create_coach_frame)
		self.machine_create = Button(self, bg="grey", fg="white", text="New Machine", width=25, height=2, pady=6, padx=15,  command=self._main_frame.create_machine_frame)
		self.gym_create = Button(self, bg="grey", fg="white", text="New Gym", width=25, height=2, pady=6, padx=15, state=DISABLED, command=self._main_frame.create_gym_frame)
		self.coaches_list = Button(self, bg="grey", fg="white", text="List Coaches", width=25, height=2, pady=6, padx=15, command=self._main_frame.list_coaches_frame)

		self.title.grid(row=1, column = 2)
		self.title2.grid(row=1, column = 3)


		self.machine_create.grid(row=2, column=1)
		self.coach_create.grid(row=2, column=2)
		self.coaches_list.grid(row=2, column=3)
		self.gym_create.grid(row=2, column=4)

