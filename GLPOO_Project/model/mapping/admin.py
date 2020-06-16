from model.mapping import Base
import uuid

from sqlalchemy import Column, String, Integer

class Admin(Base) :
	__tablename__ = 'admin'


	id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)
	
	firstname = Column(String(30), nullable=False)
	lastname = Column(String(30), nullable=False)
	email = Column(String(128), nullable=False, unique=True)
	phone_number = Column(String(10), nullable=False, unique=True)
	passwd = Column(String(256), nullable=False)


	def __repr__(self) :
		return "<Admin(%d, %s, %s, %s, %s, %s)>" % (self.id, self.firstname, self.lastname.upper(), self.email, self.phone_number, self.passwd)

	def to_dict(self) :
		return {
			"id" : self.id,
			"firstname" : self.firstname,
			"lastname" : self.lastname,
			"email" : self.email,
			"phone_number" : self.phone_number,
			"passwd" : self.passwd
		}