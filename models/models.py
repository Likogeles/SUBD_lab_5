from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

base = declarative_base()


class Master(base):
    __tablename__ = "master"
    master_id = Column(Integer, primary_key=True)
    master_name = Column(String, nullable=False)
    master_surname = Column(String, nullable=False)
    master_patronymic = Column(String, nullable=False)
    master_date_of_birth = Column(DateTime, nullable=False)


class ServiceType(base):
    __tablename__ = "service_type"
    service_type_id = Column(Integer, primary_key=True)
    service_type_name = Column(String, nullable=False)
    service_director_id = Column(Integer, ForeignKey('master.master_id'), nullable=False)
    service_director_premium = Column(String, nullable=False)
    service_director = relationship(Master, uselist=False)


class Component(base):
    __tablename__ = "component"

    component_id = Column(Integer, primary_key=True)
    component_name = Column(String, nullable=False)
    number_in_storage = Column(Integer, nullable=False)
    component_cost = Column(Integer, nullable=False)
    component_purveyor = Column(String, nullable=False)


class Service(base):
    __tablename__ = "service"
    service_id = Column(Integer, primary_key=True)
    service_name = Column(String, nullable=False)
    component_id = Column(Integer, ForeignKey('component.component_id'), nullable=False)
    service_component = relationship(Component, uselist=False)
    service_type_id = Column(Integer, ForeignKey('service_type.service_type_id'), nullable=False)
    service_type = relationship(ServiceType, uselist=False)
    service_cost = Column(Integer, nullable=False)


class Storage(base):
    __tablename__ = "storage"

    storage_id = Column(Integer, primary_key=True)
    number_of_plates = Column(Integer, nullable=False)
    number_of_free_plates = Column(Integer, nullable=False)
    storage_address = Column(String, nullable=False)


class Application(base):
    __tablename__ = "application"

    application_id = Column(Integer, primary_key=True)
    application_date = Column(DateTime, nullable=False)
    service_id = Column(Integer, ForeignKey('service.service_id'), nullable=False)
    service = relationship(Service, uselist=False)
    master_id = Column(Integer, ForeignKey('master.master_id'), nullable=False)
    master = relationship(Master, uselist=False)
    storage_id = Column(Integer, ForeignKey('storage.storage_id'), nullable=False)
    storage = relationship(Storage, uselist=False)
