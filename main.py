import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from config import host, port, db_name, user, password
from models.models import Master, ServiceType, Component, Service, Storage, Application

engine = db.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()

service_types = session.query(Application)

for service_type in service_types:
    print(service_type.application_id, service_type.application_date, service_type.service.service_name, service_type.master.master_name, service_type.storage.storage_address)

session.close()

# engine = db.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
#
# connection = engine.connect()
#
# ans = connection.execute("""SELECT * from Master""")
# print(ans.fetchall())
#
# connection.close()


# try:
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db_name,
#         port=port
#     )
#     connection.autocommit = True
#
#     with connection.cursor() as cursor:
#         cursor.execute("""
#         SELECT APPLICATION.application_date AS date, SERVICE.service_name AS service, SERVICE_TYPE.service_type_name AS service_type, MASTER.master_name AS master
# FROM APPLICATION JOIN SERVICE
# ON APPLICATION.application_id = SERVICE.service_id
# JOIN SERVICE_TYPE
# ON SERVICE.service_type_id = SERVICE_TYPE.service_type_id
# JOIN MASTER
# ON APPLICATION.master_id = MASTER.master_id;
#         """)
#         for i in cursor.fetchall():
#             print(i)
#
# except Exception as ex:
#     print("[INFO] Error while working with PostgreSQL", ex)
# finally:
#     if connection:
#         connection.close()
#     print("[INFO] PostgreSQL connection closed")
