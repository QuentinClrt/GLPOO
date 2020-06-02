from tkinter import *
from functools import partial

class BaseFrame(Frame):
	"""docstring for BaseFrame"""

	def __init__(self, main_frame):
		super().__init__(main_frame.master, width=500)
		self._main_frame = main_frame
		
	def show(self) :
		self.grid(padx=20, pady=20)

	def hide(self):
		self.grid_forget()

	def quit(self) :
		self._main_frame.quit()

	def back(self) :
		self._main_frame.back()

	def show_menu(self) :
		self._main_frame.show_menu()

	def create_entry(self, label, row=0, width=80, validate_callback=None, text="Insert value...", disabled=False, columnspan=3, **options) :
		Label(self, text=label).grid(row=row, sticky="w")
		entry=Entry(self, width=width, fg='black', **options)
		if text:
			entry.insert(0, text)
		if disabled:
			entry.config(state=DISABLED)
		if validate_callback:
			entry.bind('<KeyRelease>', partial(validate_callback, entry=entry))
		entry.grid(row=row, column=1, columnspan=columnspan)
		return entry
