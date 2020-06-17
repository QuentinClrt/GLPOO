
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
		self.title=Label(self, text="Send email to all adminstrators", height=3)
		self.mail_content = self.create_entry("Mail content : ", row=2, columnspan=2, cursor="arrow", justify="center", selectborderwidth=3)
		self.validate = Button(self, bg="green", fg="white", text="Validate", width=14, height=1, pady=4, padx=10, command=self.validate)

		self.title.grid(row=1, column=2)
		self.mail_content.grid(row=2, column=2)
		self.validate.grid(row=3, column=3)


	def validate(self):

		mail_content = self.mail_content.get()

		#print(mail_content)

		try:
			#validated_data = self._admin_controller.send_email(data)

			#SEND EMAIL... (Easter Egg)

			messagebox.showinfo("Success", "Email sent to all administrators !")

		except Error as e:
			messagebox.showerror("Error", str(e))
			return


		self.show_menu()


