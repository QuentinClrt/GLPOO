from model.mapping import Base
import uuid

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Coach(Base) :
	__tablename__ = 'coach'


	id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)
	
	firstname = Column(String(30), nullable=False)
	lastname = Column(String(30), nullable=False)
	email = Column(String(128), nullable=False, unique=True)
	phone_number = Column(String(10), nullable=False, unique=True)
	degree = Column(String(128))
	specialties = Column(String(256))
	gym = relationship("Gym", back_populates="coaches")


	def __repr__(self) :
		return "%s, %s, %s, %s, %s, %s, %s" % (self.id, self.firstname, self.lastname.upper(), self.email, self.phone_number, self.degree, self.specialties)

	def to_dict(self) :
		return {
			"id" : self.id,
			"firstname" : self.firstname,
			"lastname" : self.lastname,
			"email" : self.email,
			"phone_number" : self.phone_number,
			"degree" : self.degree,
			"specialties" : self.specialties
		}


	def return_basic_informations(self) :
		return {
			"firstname" : self.firstname,
			"lastname" : self.lastname,
			"email" : self.email,
			"phone_number" : self.phone_number,
			"degree" : self.degree,
			"specialties" : self.specialties
		}