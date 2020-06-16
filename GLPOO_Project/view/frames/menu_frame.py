from tkinter import *
from view.base_frame import BaseFrame

class MenuFrame(BaseFrame):

	def __init__(self, main_frame):
		super().__init__(main_frame)
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Gym'Administration - Menu")
		
		self.gym = Button(self, text="Gym Informations", width=70, pady=15, padx=60, command=self._main_frame.list_gym_frame)
		self.admin = Button(self, text="Admin Interface", width=70, pady=15, padx=60, command=self._main_frame.admin_frame)
		self.quit = Button(self, text="EXIT", fg="red", width=50, pady=15, padx=60, command=self.quit)
		
		self.title.pack(side="top")
		self.gym.pack()
		self.admin.pack()
		self.quit.pack(side="bottom")