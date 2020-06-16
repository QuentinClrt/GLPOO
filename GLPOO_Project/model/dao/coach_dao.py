import logging

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.coach import Coach
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(filename="log_file.log", format='%(asctime)s - %(levelname)s - %(message)s')

"""
Coach Mapping DAO
"""
class CoachDAO(DAO):
	def __init__(self, database_session):
		super().__init__(database_session)

	def get(self, id):
		try:
			logging.debug("CoachDAO:get() on id : {}".format(id))
			return self._database_session.query(Coach).filter_by(id=id).order_by(Coach.firstname).one()
		except NoResultFound:
			logging.error("CoachDAO:get() on id : {}".format(id))
			raise ResourceNotFound()

	def get_all(self):
		try: 
			logging.debug("CoachDAO:get_all()")
			return self._database_session.query(Coach).filter_by(Admin.firstname).all()
		except NoResultFound:
			logging.error("CoachDAO:get_all()")
			raise ResourceNotFound()

	def get_by_name(self, firstname: str, lastname: str):
		try:
			logging.debug("CoachDAO:get_by_name() on firstname : {}, lastname : {}".format(firstname, lastname))
			return self._database_session.query(Coach).filter_by(firstname=firstname, lastname=lastname).order_by(Coach.firstname).one()
		except NoResultFound:
			logging.error("CoachDAO:get_all() on firstname : {}, lastname : {}".format(firstname, lastname))
			raise ResourceNotFound()

	def create(self, data: dict):
		try:
			coach = Coach(firstname=data.get('firstname'), lastname=data.get('lastname'), email=data.get('email'), phone_number=data.get('phone_number'), degree=data.get('degree'), specialties=data.get('specialties'))
			self._database_session.add(coach)
			self._database_session.flush()
			logging.debug("CoachDAO:create() on firstname : {}, lastname {}".format(data['firstname'], data['lastname']))
		except NoResultFound:
			logging.error("CoachDAO:create() on firstname : {}, lastname {}".format(data['firstname'], data['lastname']))
			raise Error("ERROR (during creation) : Coach already exist.")

		return admin

	def update(self, coach: Coach, data: dict):
		if 'firstname' in data:
			coach.firstname = data['firstname']

		if 'lastname' in data:
			coach.lastname = data['lastname']

		if 'email' in data:
			coach.email = data['email']

		if 'phone_number' in data:
			coach.phone_number = data['phone_number']

		if 'degree' in data:
			coach.degree = data['degree']

		if 'specialties' in data:
			coach.specialties = data['specialties']

		try:
			self._database_session.merge(coach)
			self._database_session.flush()
			logging.debug("CoachDAO:update() on firstname : {}, lastname : {}".format(data['firstname'], data['lastname']))
		except IntegrityError:
			logging.error("CoachDAO:update() on firstname : {}, lastname : {}".format(data['firstname'], data['lastname']))
			raise Error("ERROR (during update) : Coach doesn't exist.")

		return coach

	def delete(self, entity):
		try: 
			self._database_session.delete(entity)
			logging.debug("CoachDAO:delete()")
		except SQLAlchemyError as error:
			logging.error("CoachDAO:delete()")
			raise Error(str(error))