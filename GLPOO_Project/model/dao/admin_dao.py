import logging

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.admin import Admin
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(filename="log_file.log", format='%(asctime)s - %(levelname)s - %(message)s')

"""
Admin Mapping DAO
"""
class AdminDAO(DAO):
	def __init__(self, database_session):
		super().__init__(database_session)

	def get(self, id):
		try:
			logging.debug("AdminDAO:get() on id : {}".format(id))
			return self._database_session.query(Admin).filter_by(id=id).order_by(Admin.firstname).one()
		except NoResultFound:
			logging.error("AdminDAO:get() on id : {}".format(id))
			raise ResourceNotFound()

	def get_all(self):
		try:
			logging.debug("AdminDAO:get_all()")
			return self._database_session.query(Admin).order_by(Admin.firstname).all()
		except NoResultFound:
			logging.error("AdminDAO:get_all()")
			raise ResourceNotFound()

	def get_by_name(self, login: str, firstname: str, lastname: str):
		try: 
			logging.debug("AdminDAO:get_by_name() on login : {}, firstname : {}, lastname : {}".format(login, firstname, lastname))
			return self._database_session.query(Admin).filter_by(firstname=firstname, lastname=lastname).order_by(Admin.firstname).one()
		except NoResultFound:
			logging.error("AdminDAO:get_by_name() on login : {}, firstname : {}, lastname : {}".format(login, firstname, lastname))
			raise ResourceNotFound()


	def get_all_mail(self):
		try:
			return self._database_session.query(Admin.login).all()
		except NoResultFound :
			raise ResourceNotFound()


	def create(self, data: dict):
		try:
			admin = Admin(login=data.get('login'), password=data.get('password'), firstname=data.get('firstname'), lastname=data.get('lastname'), phone_number=data.get('phone_number'))
			self._database_session.add(admin)
			self._database_session.flush()
			logging.debug("AdminDAO:create() on login : {}, firstname : {}, lastname : {}".format(data['login'], data['firstname'], data['lastname']))
		except IntegrityError:
			logging.error("AdminDAO:create() on login : {}, firstname : {}, lastname : {}".format(data['login'], data['firstname'], data['lastname']))
			raise Error("ERROR (during creation) : Administrator already exist.")
		
		return admin

	def update(self, admin: Admin, data: dict):
		if 'login' in data:
			admin.login = data['login']

		if 'password' in data:
			admin.password = data['password']

		if 'firstname' in data:
			admin.first = data['firstname']

		if 'lastname' in data:
			admin.lastname = data['lastname']

		if 'phone_number' in data:
			admin.phone_number = data['phone_number']

		try:
			self._database_session.merge(admin)
			self._database_session.flush()
			logging.debug("AdminDAO:update() on login : {}, firstname : {}, lastname : {}".format(data['login'], data['firstname'], data['lastname']))
		except IntegrityError:
			logging.error("AdminDAO:update() on login : {}, firstname : {}, lastname : {}".format(data['login'], data['firstname'], data['lastname']))
			raise Error("ERROR (during update) : Administrator doesn't exist.")
		
		return admin

	def delete(self, entity):
		try:
			self._database_session.delete(entity)
			logging.debug("AdminDAO:delete()")
		except SQLAlchemyError as error:
			logging.error("AdminDAO:delete()")
			raise Error(str(error))