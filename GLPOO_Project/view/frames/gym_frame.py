from tkinter import *

from view.base_frame import BaseFrame
from controller.gym_controller import GymController

class GymFrame(BaseFrame) :

	def __init__(self, gym_controller : GymController, main_frame : Frame):
		super().__init__(main_frame)
		self._gym_controller = gym_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Gym Informations", height=3)

		self.gyms_list = Button(self, bg="grey", fg="white", text="List Gyms", width=25, height=2, pady=6, padx=15)
		self.coach_list = Button(self, bg="grey", fg="white", text="List Coaches", width=25, height=2, pady=6, padx=15)
		self.machine_list = Button(self, bg="grey", fg="white", text="List Machines", width=25, height=2, pady=6, padx=15)

		self.title.grid(row=1, column = 2)
		self.gyms_list.grid(row=2, column=1)
		self.coach_list.grid(row=2, column=2)
		self.machine_list.grid(row=2, column=3)

