import re
import logging


from model.dao.machine_dao import MachineDAO

from exceptions import Error, InvalidData


class MachineController:
	
	def __init__(self, database_engine):
		self._database_engine = database_engine

	def create_machine(self, data):
		try:
			with self._database_engine.new_session() as session:
				dao = MachineDAO(session)
				machine = dao.create(data)
				machine_data = machine.to_dict()
				return machine_data
			except Error as error:
				raise error

	def list_machines(self, person_type=None):
		with self._database_engine.new_session() as session:
			machines = MachineDAO(session).get_all()
			machines_data = [machines.to_dict() for machine in machines]
		return machine_data

	def get_machine(self, machine_id):
		with self._database_engine.new_session() as session:
			machine = MachineDAO(session).get(machine_id)
			machine_data = machine.to_dict()
		return machine_data

	def update_machine(self, machine_id, machine_data):
		with self._database_engine.new_session() as session:
			dao = MachineDAO(session)
			machine = dao.get(machine_id)
			machine = dao.update(machine, machine_data)
			return machine.to_dict()

	def delete_machine(self, machine_id):
		with self._database_engine.new_session() as session:
			dao = MachineDAO(session)
			machine = dao.get(machine_id)
			dao.delete(machine)

	def search_machine(self, name):
		with self._database_engine.new_session() as session:
			dao = MachineDAO(session)
			machine = dao.get_by_name(name)
			return machine.to_dict()