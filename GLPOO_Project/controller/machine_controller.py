import re
import logging


from model.dao.machine_dao import MachineDAO

from exceptions import Error, InvalidData


class MachineController:
	"""


	"""

	def __init__(self, database_engine):
		self._database_engine = database_engine

	def list_gyms(self, person_type=None):
		logging.debug("Machine interface")
		

		return 