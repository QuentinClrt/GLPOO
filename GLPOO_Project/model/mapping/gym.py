from model.mapping import Base
import uuid

from sqlalchemy import Colum, String, Integer
from sqlalchemy.orm import relationship
from model.mapping.coach import coaches_pop
from model.mapping.machine import machines_pop

class Gym(Base) :
	__tablename__ = 'gym'


	id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

	name = Column(String(128), nullable=False)
	phone_number = Column(Integer(10), nullable=False, unique=True)
	address = Column(String(256), nullable=False)

	machines = relationship("Machine", back_populates="machines_pop")
	coaches = relationship("Coaches", back_populates="coaches_pop")

	def __repr__(self) :
		return "<Gym(%d, %s, %s, %d)>" % (self.id, self.name, self.address, self.phone_number)

	def to_dict(self) :
		_data {
			"id" : self.id,
			"name" : self.name,
			"phone_number" : self.phone_number,
			"address" : self.address,
			"machines" : [],
			"coaches" : []
		}

		for machine in self.machines:
			_data['machines'].append({"id" : machine.id,
									  "name" : machine.name,
									  "brand" : machine.brand })
		for coach in self.coaches:
			_data['coaches'].append({"id" : coach.id,
									 "firstname" : coach.firstname,
									 "lastname" : coach.lastname,
									 "phone_number" : coach.phone_number,
									 "email" : coach.email })

		return _data