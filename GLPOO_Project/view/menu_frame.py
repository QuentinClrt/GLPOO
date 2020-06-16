from tkinter import *
from view.base_frame import BaseFrame
from controller.gym_controller import GymController
from controller.admin_controller import AdminController

class MenuFrame(BaseFrame):

	def __init__(self, main_frame):
		super().__init__(main_frame)
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Gym'Administration - Menu", height=5)
		
		self.gym = Button(self, bg="grey", fg="white", text="Gym Informations", width=40, height=3, pady=6, padx=15, command=self._main_frame.list_gym_frame)
		self.admin = Button(self, bg="grey", fg="white", text="Admin Interface", width=40, height=3, pady=6, padx=15, command=self._main_frame.admin_frame)
		self.quit = Button(self, text="EXIT", fg="red", width=12, padx=3, command=self.quit)
		
		self.title.grid(row=1, column=2)
		self.gym.grid(row=2, column=1)
		self.admin.grid(row=2, column=3)
		self.quit.grid(row=3, column=2)