import logging
import sys

from model.database import DatabaseEngine
from controller.gym_controller import GymController
from controller.admin_controller import AdminController
from controller.coach_controller import CoachController
from controller.machine_controller import MachineController

from view.main_frame import MainFrame


def main() :

	# here is a logging configuration with three handlers (two handlers configured on one file and one stream)
	logger = logging.getLogger('log_file')
	logger.setLevel(logging.NOTSET)

	debug_logger = logging.FileHandler('log_file.log')
	debug_logger.setLevel(logging.DEBUG)

	error_logger = logging.FileHandler('log_file.log')
	error_logger.setLevel(logging.ERROR)

	console_logger = logging.StreamHandler()
	console_logger.setLevel(logging.ERROR)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	debug_logger.setFormatter(formatter)
	error_logger.setFormatter(formatter)
	console_logger.setFormatter(formatter)


	logger.addHandler(debug_logger)
	logger.addHandler(error_logger)
	logger.addHandler(console_logger)


	#Running app
	logging.debug("Running Gym'Administration app")

	#Init database
	logging.debug("Init database")
	database_engine = DatabaseEngine(url='sqlite:///database.db')
	database_engine.create_database()

	#Controller
	gym_controller = GymController(database_engine)
	admin_controller = AdminController(database_engine)
	coach_controller = CoachController(database_engine)
	machine_controller = MachineController(database_engine)

	#Vue
	root = MainFrame(gym_controller, admin_controller, coach_controller, machine_controller)
	root.master.title("Gym'Administration - Desktop App")
	root.show_menu()

	#Start
	root.mainloop()


if __name__ == "__main__":
	main()