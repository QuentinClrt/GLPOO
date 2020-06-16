from model.mapping import Base
import uuid

from sqlalchemy import Column, String, Integer

class Machine(Base) :
	__tablename__ = 'machine'

	id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

	name = Column(String(128), nullable=False)
	brand = Column(String(128), nullable=False)
	provider = Column(String(128), nullable=False)
	muscular_group = Column(String(128), nullable=False)

	def __repr__(self) :
		return "<Machine(%d, %s, %s, %s, %s)>" % (self.id, self.name, self.brand, self.provider, self.muscular_group)

	def to_dict(self) :
		return {
			"id" : self.id,
			"name" : self.name,
			"brand" : self.brand,
			"provider" : self.provider,
			"muscular_group" : self.muscular_group
		}