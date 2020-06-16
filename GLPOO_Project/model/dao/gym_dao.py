import logging

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.gym import Gym
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(filename="log_file.log", format='%(asctime)s - %(levelname)s - %(message)s')

"""
Gym Mapping DAO
"""
class GymDAO(DAO):
	def __init__(self, database_session):
		super().__init__(database_session)

	def get(self, id):
		try:
			logging.debug("GymDAO:get() on id : {}".format(id))
			return self._database_session.query(Gym).filter_by(id=id).order_by(Gym.name).one()
		except NoResultFound:
			logging.error("GymDAO:get() on id : {}".format(id))
			raise ResourceNotFound()

	def get_all(self):
		try:
			logging.debug("GymDAO:get_all()")
			return self._database_session.query(Gym).filter_by(Gym.name).all()
		except NoResultFound:
			logging.error("GymDAO:get_all()")
			raise ResourceNotFound()

	def get_by_name(self, name: str):
		try:
			logging.debug("MachineDAO:get_by_name() on name : {}".format(name))
			return self._database_session.query(Gym).filter_by(name=name).order_by(name=name).all()
		except NoResultFound:
			logging.error("MachineDAO:get_by_name() on name : {}".format(name))
			raise ResourceNotFound()

	def create(self, data: dict):
		try:
			gym = Gym(name=data.get('name'), phone_number=data.get('phone_number'), address=data.get('address'))
			self._database_session.add(gym)
			self._database_session.flush()
			logging.debug("GymDAO:create() on name : {}, address : {}".format(data['name'], data['address']))
		except NoResultFound:
			logging.error("GymDAO:create() on name : {}, address : {}".format(data['name'], data['address']))
			raise Error("ERROR (during creation) : Gym already exist.")

		return gym

	def _update_machines(self, gym, address_data):
		if gym.address is not None:
			if 'name' in address_data:
				gym.address.name = address_data['name']

			if 'brand' in  address_data:
				gym.address.brand = address_data['brand']
		else:
			gym.set_machine(address_data['name'], address_data['brand'], address_data['provider'], address_data['muscular_group'])

	def _update_coaches(self, gym, address_data):
		if gym.address is not None:
			if 'firstname' in address_data:
				gym.address.firstname = address_data['firstname']

			if 'lastname' in address_data:
				gym.address.lastname = address_data['lastname']

			if 'phone_number' in address_data:
				gym.address.phone_number = address_data['phone_number']

			if 'emain' in address_data:
				gym.address.email = address_data['email']
			else:
				gym.set_coach(address_data['firstname'], address_data['lastname'], address_data['phone_number'], address_data['email'], address_data['degree'], address_data['specialties'])

	def update(self, gym: Gym, data: dict):
		if 'name' in data:
			gym.name = data['name']

		if 'address' in data:
			gym.address = data['address']

		if 'phone_number' in data:
			gym.phone_number = data['phone_number']

		if 'machines' in data:
			self._update_machines(gym, data['machines'])

		if 'coaches' in data:
			self._update_coaches(gym, data['coaches'])
		
		try:
			self._database_session.merge(gym)
			self._database_session.flush()
			logging.debug("GymDAO:update() on name : {}, address : {}".format(data['name'], data['address']))
		except IntegrityError:
			logging.error("GymDAO:update() on name : {}, address : {}".format(data['name'], data['address']))
			raise Error("ERROR (during update) : Gym doesn't exist.")

		return gym

	def delete(self, entity):
		try:
			self._database_session.delete(entity)
			logging.debug("GymDAO:delete()")
		except SQLAlchemyError as error:
			logging.error("GymDAO:delete()")
			raise Error(str(error))