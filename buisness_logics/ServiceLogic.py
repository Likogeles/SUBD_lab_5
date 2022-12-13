from models.models import Service


class ServiceLogic:
    def __init__(self, session):
        self.session = session

    def add(self, service_name, component_id, service_type_id, service_cost):
        new_id = self.session.query(Service).order_by(Service.service_id.desc()).first()
        if new_id:
            new_id = new_id.service_id + 1
        else:
            new_id = 1
        new_service = Service(service_id=new_id,
                              service_name=service_name,
                              component_id=component_id,
                              service_type_id=service_type_id,
                              service_cost=service_cost)
        self.session.add(new_service)
        self.session.commit()

    def edit(self, service_id, service_name, component_id, service_type_id, service_cost):
        self.session.query(Service).where(Service.service_id == service_id).\
            update({'service_name': service_name,
                    'component_id': component_id,
                    'service_type_id': service_type_id,
                    'service_cost': service_cost
                    })
        self.session.commit()

    def remove(self, service_id):
        self.session.query(Service).filter(Service.service_id == service_id).delete()
        self.session.commit()

    def get(self, service_id):
        return self.session.query(Service).where(Service.service_id == service_id).first()

    def get_all(self):
        return self.session.query(Service).order_by(Service.service_id)
