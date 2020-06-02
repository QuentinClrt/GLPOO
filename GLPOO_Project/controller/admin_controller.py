import re
import logging


from model.dao.admin_dao import AdminDao

from exceptions import Error, InvalidData


class AdminController:
	"""


	"""

	def __init__(self, database_engine):
		self._database_engine = database_engine

	def list_gyms(self, person_type=None):
		logging.debug("Admin Interface")
		

		return 