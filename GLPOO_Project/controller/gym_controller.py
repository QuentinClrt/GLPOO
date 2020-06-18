import re
import logging


from model.dao.gym_dao import GymDAO

from exceptions import Error, InvalidData


class GymController:
	
	def __init__(self, database_engine):
		self._database_engine = database_engine

	def create_gym(self, data):
		try:
			with self._database_engine.new_session() as session:
				dao = GymDAO(session)
				gym = dao.create(data)
				gym_data = gym.to_dict()
				return gym_data
		except Error as error:
			raise error

	def list_gyms(self, person_type=None):
		with self._database_engine.new_session() as session:
			gyms = GymDAO(session).get_all()
			print(gyms)
			gyms_data = [gyms.to_dict('dict') for gym in gyms]
		return gyms_data

	def get_gym(self, gym_id):
		with self._database_engine.new_session() as session:
			gym = GymDAO(session).get(gym_id)
			gym_data = gym.to_dict()
		return gym_data

	def update_gym(self, gym_id, gym_data):
		with self._database_engine.new_session() as session:
			dao = GymDAO(session)
			gym = dao.get(gym_data)
			gym = dao.update(gym, gym_data)
			return gym.to_dict()

	def delete_gym(self, gym_id):
		with self._database_engine.new_session() as session:
			dao = GymDAO(session)
			gym = dao.get(gym_id)
			dao.delete(gym)

	def search_gym(self, name):
		with self._database_engine.new_session() as session:
			dao = GymDAO(session)
			gym = dao.get_by_name(name)
			return gym.to_dict()