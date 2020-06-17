import re
import logging


from model.dao.coach_dao import CoachDAO

from exceptions import Error, InvalidData


class CoachController:
	"""


	"""

	def __init__(self, database_engine):
		self._database_engine = database_engine

	def list_gyms(self, person_type=None):
		logging.debug("Coach interface")
		

		return 