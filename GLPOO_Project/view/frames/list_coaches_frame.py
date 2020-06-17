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