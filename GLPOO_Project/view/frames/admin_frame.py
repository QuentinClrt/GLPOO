from tkinter import *

from view.base_frame import BaseFrame
from controller.admin_controller import AdminController

class AdminFrame(BaseFrame) :

	def __init__(self, admin_controller : AdminController, main_frame : Frame):
		super().__init__(main_frame)
		self._admin_controller = admin_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Admin Interface", height=3)

		self.create_admin = Button(self, bg="grey", fg="white", text="Create an admin", width=30, height=2, pady=6, padx=15, command=self._main_frame.create_admin_frame)
		self.email_admin = Button(self, bg="grey", fg="white", text="Send email to all admins", width=30, height=2, pady=6, padx=15, command=self._main_frame.email_admin_frame)

		self.title.grid(row=1, column=2)
		self.create_admin.grid(row=2, column=1)
		self.email_admin.grid(row=2, column=3)
