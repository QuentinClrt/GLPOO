import re
import logging


from model.dao.admin_dao import AdminDAO

from exceptions import Error, InvalidData


class AdminController:
	
	def __init__(self, database_engine):
		self._database_engine = database_engine

	def create_admin(self, data):
		try:
			with self._database_engine.new_session() as session:
				dao = AdminDAO(session)
				admin = dao.create(data)
				admin_data = admin.to_dict()
				return admin_data
		except Error as error:
			 raise error

	def list_admins(self, person_type=None):
		with self._database_engine.new_session() as session:
			admins = AdminDAO(session).get_all()
			admins_data = [admins.to_dict() for admin in admins]
		return admins_data

	def get_admin(self, admin_id):
		with self._database_engine.new_session() as session:
			admin = AdminDAO(session).get(admin_id)
			admin_data = admin.to_dict()
		return admin_data

	def update_admin(self, admin_id, admin_data):
		with self._database_engine.new_session() as session:
			dao = AdminDAO(session)
			admin = dao.get(admin_id)
			admin = dao.update(admin, admin_data)
			return admin.to_dict()

	def delete_admin(self, admin_id):
		with self._database_engine.new_session() as session:
			dao = AdminDAO(session)
			admin = dao.get(admin_id)
			dao.delete(admin)

	def search_admin(self, login, firstname, lastname):
		with self._database_engine.new_session() as session:
			dao = adminDAO(session)
			admin = dao.get_by_name(login, firstname, lastname)
			return admin.to_dict()