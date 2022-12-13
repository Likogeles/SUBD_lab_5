from models.models import ServiceType


class ServiceTypeLogic:
    def __init__(self, session):
        self.session = session

    def add(self, service_type_name, service_director_id, service_director_premium):
        new_id = self.session.query(ServiceType).order_by(ServiceType.service_type_id.desc()).first()
        if new_id:
            new_id = new_id.service_type_id + 1
        else:
            new_id = 1
        new_service_type = ServiceType(service_type_id=new_id,
                                       service_type_name=service_type_name,
                                       service_director_id=service_director_id,
                                       service_director_premium=service_director_premium)
        self.session.add(new_service_type)
        self.session.commit()

    def edit(self, service_type_id, service_type_name, service_director_id, service_director_premium):
        self.session.query(ServiceType).where(ServiceType.service_type_id == service_type_id).\
            update({'service_type_name': service_type_name,
                    'service_director_id': service_director_id,
                    'service_director_premium': service_director_premium,
                    })
        self.session.commit()

    def find(self, name):
        return self.session.query(ServiceType)\
            .where(ServiceType.service_type_name == name)\
            .first()

    def remove(self, service_type_id):
        self.session.query(ServiceType).filter(ServiceType.service_type_id == service_type_id).delete()
        self.session.commit()

    def get(self, service_type_id):
        return self.session.query(ServiceType).where(ServiceType.service_type_id == service_type_id).first()

    def get_all(self):
        return self.session.query(ServiceType).order_by(ServiceType.service_type_id)
