import re
import logging


from model.dao.coach_dao import CoachDAO

from exceptions import Error, InvalidData


class CoachController:
	
	def __init__(self, database_engine):
		self._database_engine = database_engine

	def create_coach(self, data):
		try:
			with self._database_engine.new_session() as session:
				dao = CoachDAO(session)
				coach = dao.create(data)
				coach_data = coach.to_dict()
				return coach_data
		except Error as error:
			raise error

	def list_coaches(self, person_type=None):
		with self._database_engine.new_session() as session:
			coaches = CoachDAO(session).get_all()
			coaches_data = [coaches.to_dict() for coach in coaches]
		return coaches_data
	
	def get_coach(self, coach_id):
		with self._database_engine.new_session() as session:
			coach = CoachDAO(session).get(coach_id)
			coach_data = coach.to_dict()
		return coach_data

	def update_coach(self, coach_id, coach_data):
		with self._database_engine.new_session() as session:
			dao = CoachDAO(session)
			coach = dao.get(coach_id)
			coach = dao.update(coach, coach_data)
			return coach.to_dict()

	def delete_coach(self, coach_id):
		with self._database_engine.new_session() as session:
			dao = CoachDAO(session)
			coach = dao.get(coach_id)
			dao.delete(coach)

	def search_coach(self, firstname, lastname):
		with self._database_engine.new_session() as session:
			dao = coachDao(session)
			coach = dao.get_by_name(firstname, lastname)
			return coach.to_dict()