import re
import logging


from model.dao.gym_dao import GymDao

from exceptions import Error, InvalidData


class GymController:
	"""


	"""

	def __init__(self, database_engine):
		self._database_engine = database_engine

	def list_gyms(self, person_type=None):
		logging.debug("Gyms Interface")
		

		return 