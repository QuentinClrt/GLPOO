import logging
import sys
from model.database import DatabaseEngine

from controller.admin_controller
from controller.gym_controller
from controller.machine_controller



from vue.root_frame


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
	debug_logger.info("Running Gym'Administration app")

	#Init database
	debug_logger.info("Init database")
	database_engine = DatabaseEngine(url='sqlite:///database.db')
	database_engine.create_database()
	
	#Controller

	#Vue

	#Start

if __name__ == "__main__":
	main()