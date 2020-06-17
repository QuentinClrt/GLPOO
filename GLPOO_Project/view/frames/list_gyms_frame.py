from tkinter import messagebox
from tkinter import *


from view.base_frame import BaseFrame
from controller.gym_controller import GymController
from exceptions import Error

class ListGymsFrame(BaseFrame) :
	def __init__(self, gym_controller : GymController, main_frame : Frame):
		super().__init__(main_frame)
		self._gym_controller = gym_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="List Gyms", height=3)

		self.title.grid(row=1, column=1)