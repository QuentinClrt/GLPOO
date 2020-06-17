from model.mapping import Base
import uuid

from sqlalchemy import Column, String, Integer

class Admin(Base) :
	__tablename__ = 'admin'


	id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)
	
	firstname = Column(String(30), nullable=False)
	lastname = Column(String(30), nullable=False)
	login = Column(String(128), nullable=False, unique=True)
	phone_number = Column(String(10), nullable=False, unique=True)
	password = Column(String(256), nullable=False)


	def __repr__(self) :
		return "<Admin(%d, %s, %s, %s, %s, %s)>" % (self.id, self.firstname, self.lastname.upper(), self.login, self.phone_number, self.password)

	def to_dict(self) :
		return {
			"id" : self.id,
			"firstname" : self.firstname,
			"lastname" : self.lastname,
			"login" : self.login,
			"phone_number" : self.phone_number,
			"password" : self.password
		}