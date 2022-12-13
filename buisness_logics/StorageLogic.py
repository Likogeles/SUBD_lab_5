from models.models import Storage


class StorageLogic:
    def __init__(self, session):
        self.session = session

    def add(self, number_of_plates, number_of_free_plates, storage_address):
        new_id = self.session.query(Storage).order_by(Storage.storage_id.desc()).first().storage_id + 1
        new_storage = Storage(storage_id=new_id,
                              number_of_plates=number_of_plates,
                              number_of_free_plates=number_of_free_plates,
                              storage_address=storage_address)
        self.session.add(new_storage)
        self.session.commit()

    def edit(self, storage_id, number_of_plates, number_of_free_plates, storage_address):
        self.session.query(Storage).where(Storage.storage_id == storage_id).\
            update({'number_of_plates': number_of_plates,
                    'number_of_free_plates': number_of_free_plates,
                    'storage_address': storage_address,
                    })
        self.session.commit()

    def remove(self, storage_id):
        self.session.query(Storage).filter(Storage.storage_id == storage_id).delete()
        self.session.commit()

    def get(self, storage_id):
        return self.session.query(Storage).where(Storage.storage_id == storage_id).first()

    # def find(self, name):
    #     return self.session.query(Component)\
    #         .where(Component.component_name == name)\
    #         .first()

    def get_all(self):
        return self.session.query(Storage).order_by(Storage.storage_id)
