from models.models import Master


class MasterLogic:
    def __init__(self, session):
        self.session = session

    def add_master(self, name, surname, patronymic, date_of_birth):
        new_id = self.session.query(Master).order_by(Master.master_id.desc()).first().master_id + 1
        new_master = Master(master_id=new_id,
                            master_name=name,
                            master_surname=surname,
                            master_patronymic=patronymic,
                            master_date_of_birth=date_of_birth)
        self.session.add(new_master)
        self.session.commit()

    def get(self, master_id):
        return self.session.query(Master).where(Master.master_id == master_id).first()

    def get_all(self):
        return self.session.query(Master)
