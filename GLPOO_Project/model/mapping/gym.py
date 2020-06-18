from model.mapping import Base
import uuid

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.mapping.coach import Coach
from model.mapping.machine import Machine

class Gym(Base) :
	__tablename__ = 'gym'


	id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

	name = Column(String(128), nullable=False)
	phone_number = Column(Integer(), nullable=False, unique=True)
	address = Column(String(256), nullable=False)

	machines_id = Column(String(36), ForeignKey("machine.id"), nullable=True)
	coaches_id = Column(String(36), ForeignKey("coach.id"), nullable=True)
	machines = relationship("Machine", back_populates="gym")
	coaches = relationship("Coach", back_populates="gym")

	def __repr__(self) :
		return "<Gym(%d, %s, %s, %d)>" % (self.id, self.name, self.address, self.phone_number)

	def to_dict(self) :
		_data = {
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

	def set_machine(self, name: str, brand: str, provider: str, muscular_group: str):
		self.machine = Machine(name=name, brand=brand, provider=provider, muscular_group=muscular_group)

	def set_coach(self, firstname: str, lastname: str, phone_number: str, email: str, degree: str, specialties: str):
		self.coach = Coach(firstname=firstname, lastname=lastname, email=email, phone_number=phone_number, degree=degree, specialties=specialties)
