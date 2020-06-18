
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
		self.mail_content = self.create_entry("Mail content : ", row=4, columnspan=10, cursor="arrow", justify="center", selectborderwidth=10)
		self.validate = Button(self, bg="green", fg="white", text="Validate", width=14, height=1, pady=4, padx=10, command=self.validate)

		#If we get all the emails without any problem, it will be possible to then validate and "send an email", else, you can not validate
		try :
			emails = self._admin_controller.get_mail()

			self.list_emails = Text(self, width=30, height=10)


			for i in emails:
				self.list_emails.insert(END, i[0]+'\n')

			self.list_emails.grid(row=2, column=2)

		except Error as e:
			self.validate.config(state=DISABLED)
			messagebox.showerror("Error", str(e))


		self.title.grid(row=1, column=2)
		self.mail_content.grid(row=4, column=2)
		self.validate.grid(row=5, column=3)


	def validate(self):

		mail_content = self.mail_content.get()

		try:
			#SEND EMAIL... (Easter Egg). This part was created to list admins only because send emails to unknown addresses is forbidden (cf. phising next)

			messagebox.showinfo("Success", "Email sent to all administrators !")

		except Error as e:
			messagebox.showerror("Error", str(e))
			return


		self.show_menu()


