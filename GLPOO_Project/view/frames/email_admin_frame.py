
from tkinter import messagebox
from tkinter import *

from view.base_frame import BaseFrame
from controller.admin_controller import AdminController
from exceptions import Error

class EmailAdminFrame(BaseFrame) :

	def __init__(self, admin_controller : AdminController, main_frame : Frame):
		super().__init__(main_frame)
		self._admin_controller = admin_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="Send email to admins", height=3)

		self.title.grid(row=1, column=1)