from tkinter import messagebox
from tkinter import *


from view.base_frame import BaseFrame
from controller.machine_controller import MachineController
from exceptions import Error

class ListMachinesFrame(BaseFrame) :
	def __init__(self, machine_controller : MachineController, main_frame : Frame):
		super().__init__(main_frame)
		self._machine_controller = machine_controller
		self.create_widgets()

	def create_widgets(self):
		self.title=Label(self, text="List Machines", height=3)

		self.title.grid(row=1, column=1)


	#def list_coaches_frame(self) :

	#	pass

		#try:
		#	validated_data = self._admin_controller.create_admin(data)
		#	messagebox.showinfo("Success", "Administrator created !")

		#except Error as e:
		#	messagebox.showerror("Error", str(e))
		#	return

	#	pass