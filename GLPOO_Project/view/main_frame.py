from tkinter import *

from view.menu_frame import MenuFrame
from view.frames.admin_frame import AdminFrame
from view.frames.list_gym_frame import ListGymFrame


class MainFrame(Frame) :

	def __init__(self, gym_controller, admin_controller, master=None) :
		super().__init__(master)
		self._gym_controller = gym_controller
		self._admin_controller = admin_controller
		self._menu_frame = MenuFrame(self)
		self._frames = []

	def list_gym_frame(self) :
		self.hide_frames()
		list_gym_frame = ListGymFrame(self._gym_controller, self, person_type='gym')
		list_gym_frame.show()
		self._frames.append(list_gym_frame)

	def admin_frame(self):
		self.hide_frames()
		admin_frame = AdminFrame(self._admin_controller, self, person_type='admin')
		admin_frame.show()
		self._frames.append(admin_frame)

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