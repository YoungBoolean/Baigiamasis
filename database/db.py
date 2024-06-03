from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, SaveFile

engine = create_engine("sqlite:///user_database.db")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


rows_users = session.query(User).all()
for row in rows_users:
    if row.user_name == user_name:
        print('User by that name already has previous saves, delete old saves or choose different name')
        raise Exception

rows_users = session.query(User).all()
user_row_id = 0
for row in rows_users:
    if row.user_name == user_name:
        user_row_id = row.id

save_o1 = SaveFile(game_stage='INTRO_SCENE 3', user_id=user_row_id)
save_o2 = SaveFile(game_stage='BEDROOM_SCENE 9', user_id=user_row_id)
session.add(save_o1)
session.add(save_o2)
session.commit()

rows_save_files = session.query(SaveFile).all()
for row in rows_save_files:
    print(row)
