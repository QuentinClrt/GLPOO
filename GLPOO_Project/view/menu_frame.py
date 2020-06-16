from tkinter import *
from view.base_frame import BaseFrame

class MenuFrame(BaseFrame):

	def __init__(self, main_frame):
		super().__init__(main_frame)
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Menu", height=3)
		
		self.gym = Button(self, bg="#666699", fg="black", text="Gym Informations", width=30, height=2, pady=6, padx=15, command=self._main_frame.gym_frame)
		self.admin = Button(self, bg="#666699", fg="black", text="Admin Interface", width=30, height=2, pady=6, padx=15, command=self._main_frame.admin_frame)
		self.quit = Button(self, text="EXIT", fg="red", width=12, height=1, padx=3, command=self.quit)
		
		self.title.grid(row=1, column=2)
		self.gym.grid(row=2, column=1)
		self.admin.grid(row=2, column=3)
		self.quit.grid(row=3, column=2)