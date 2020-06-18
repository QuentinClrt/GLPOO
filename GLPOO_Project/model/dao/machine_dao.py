import logging

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.machine import Machine
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(filename="log_file.log", format='%(asctime)s - %(levelname)s - %(message)s')

"""
Machine Mapping DAO
"""
class MachineDAO(DAO):
	def __init__(self, database_session):
		super().__init__(database_session)

	def get(self, id):
		try:
			logging.debug("MachineDAO:get() on id : {}".format(id))
			return self._database_session.query(Machine).filter_by(id=id).order_by(Machine.name).one()
		except NoResultFound:
			logging.error("MachineDAO:get() on id : {}".format(id))
			raise ResourceNotFound()

	def get_all(self):
		try:
			logging.debug("MachineDAO:get_all()")
			return self._database_session.query(Machine).filter_by(Machine.name).all()
		except NoResultFound:
			logging.error("MachineDAO:get_all()")
			raise ResourceNotFound()

	def get_by_name(self, name: str):
		try:
			logging.debug("MachineDAO:get_by_name() on name : {}".format(name))
			return self._database_session.query(Machine).filter_by(name=name, brand=brand).order_by(Machine.name).one()
		except NoResultFound:
			logging.error("MachineDAO:get_by_name() on name : {}".format(name))
			raise ResourceNotFound()

	def create(self, data: dict):
		try:
			machine = Machine(name=data.get('name'), brand=data.get('brand'), provider=data.get('provider'), muscular_group=data.get('muscular_group'))
			self._database_session.add(machine)
			self._database_session.flush()
			logging.debug("MachineDAO:create() on name : {}, brand : {}, provider : {}".format(data['name'], data['brand'], data['provider']))
		except IntegrityError:
			logging.error("MachineDao:create() on name : {}, brand : {}, provider : {}".format(data['name'], data['brand'], data['provider']))
			raise Error("ERROR (during creation) : Machine already exist")

		return machine

	def update(self, machine: Machine, data: dict):
		if 'name' in data:
			machine.name = data['name']

		if 'brand' in data:
			machine.brand = data['brand']

		if 'provider' in data:
			machine.provider = data['provider']

		if 'muscular_group' in data:
			machine.muscular_group = data['muscular_group']

		try:
			self._database_session.merge(machine)
			self._database_session.flush()
			logging.debug("MachineDAO:update() on name : {}, brand : {}, provider : {}".format(data['name'], data['brand'], data['provider']))
		except IntegrityError:
			logging.error("MachineDAO:update() on name : {}, brand : {}, provider : {}".format(data['name'], data['brand'], data['provider']))
			raise Error("ERROR (during update) : Machine doesn't exist.")

		return machine

	def delete(self, entity):
		try:
			self._database_session.delete(entity)
			logging.debug("MachineDAO:delete()")
		except SQLAlchemyError as error:
			logging.error("MachineDAO:delet()")
			raise Error(str(error))