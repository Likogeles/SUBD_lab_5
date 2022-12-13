from models.models import Component


class ComponentLogic:
    def __init__(self, session):
        self.session = session

    def add(self, name, number_in_storage, component_cost, component_purveyor):
        new_id = self.session.query(Component).order_by(Component.component_id.desc()).first().component_id + 1
        new_component = Component(component_id=new_id,
                                  component_name=name,
                                  number_in_storage=number_in_storage,
                                  component_cost=component_cost,
                                  component_purveyor=component_purveyor)
        self.session.add(new_component)
        self.session.commit()

    def edit(self, component_id, name, number_in_storage, component_cost, component_purveyor):
        self.session.query(Component).where(Component.component_id == component_id).\
            update({'component_name': name,
                    'number_in_storage': number_in_storage,
                    'component_cost': component_cost,
                    'component_purveyor': component_purveyor,
                    })
        self.session.commit()

    def remove(self, component_id):
        self.session.query(Component).filter(Component.component_id == component_id).delete()
        self.session.commit()

    def get(self, component_id):
        return self.session.query(Component).where(Component.component_id == component_id).first()

    # def find(self, surname, name):
    #     return self.session.query(Master)\
    #         .where(Master.master_surname == surname)\
    #         .where(Master.master_name == name)\
    #         .first()

    def get_all(self):
        return self.session.query(Component).order_by(Component.component_id)
