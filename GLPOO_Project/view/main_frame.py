from tkinter import *

from view.menu_frame import MenuFrame
from view.frames.admin_frame import AdminFrame
from view.frames.gym_frame import GymFrame
from view.frames.create_admin_frame import CreateAdminFrame
from view.frames.email_admin_frame import EmailAdminFrame
from view.frames.list_coaches_frame import ListCoachesFrame
from view.frames.list_machines_frame import ListMachinesFrame
from view.frames.list_gyms_frame import ListGymsFrame


class MainFrame(Frame) :

	def __init__(self, gym_controller, admin_controller, coach_controller, machine_controller, master=None) :
		super().__init__(master)
		self._gym_controller = gym_controller
		self._admin_controller = admin_controller
		self._coach_controller = coach_controller
		self._machine_controller = machine_controller
		self._menu_frame = MenuFrame(self)
		self._frames = []


	#Personalized frames

	def gym_frame(self) :
		self.hide_frames()
		gym_frame = GymFrame(self._gym_controller, self)
		gym_frame.show()
		self._frames.append(gym_frame)

	def admin_frame(self):
		self.hide_frames()
		admin_frame = AdminFrame(self._admin_controller, self)
		admin_frame.show()
		self._frames.append(admin_frame)

	def email_admin_frame(self):
		self.hide_frames()
		email_admin_frame = EmailAdminFrame(self._admin_controller, self)
		email_admin_frame.show()
		self._frames.append(email_admin_frame)

	def create_admin_frame(self):
		self.hide_frames()
		create_admin_frame = CreateAdminFrame(self._admin_controller, self)
		create_admin_frame.show()
		self._frames.append(create_admin_frame)

	def list_coaches_frame(self):
		self.hide_frames()
		list_coaches_frame = ListCoachesFrame(self._coach_controller, self)
		list_coaches_frame.show()
		self._frames.append(list_coaches_frame)

	def list_machines_frame(self):
		self.hide_frames()
		list_machines_frame = ListMachinesFrame(self._machine_controller, self)
		list_machines_frame.show()
		self._frames.append(list_machines_frame)

	def list_gyms_frame(self):
		self.hide_frames()
		list_gyms_frame = ListGymsFrame(self._gym_controller, self)
		list_gyms_frame.show()
		self._frames.append(list_gyms_frame)



	def hide_frames(self):
		for frame in self._frames:
			frame.hide()

	def show_menu(self):
		for frame in self._frames:
			frame.destroy()
		self._frames = []
		self._menu_frame.show()

	def hide_menu(self):
		self._menu_frame.hide()

	def back(self):
		if len(self._frames) <= 1:
			self.show_menu()
			return
		last_frame = self._frames[-1]
		last_frame.destroy()
		del(self._frames[-1])
		last_frame = self._frames[-1]
		last_frame.show()

	def cancel(self):
		self.show_menu()

	def quit(self):
		self.master.destroy()