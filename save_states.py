from database.db import session, User, SaveFile


class SaveState:
    def __init__(self, session=session, user=User, savefile=SaveFile):
        self.session = session
        self.user = user
        self.savefile = savefile

    def save_game(self, game_stage, user_name):
        rows_users = self.session.query(self.user).all()
        user_found = False

        for row in rows_users:
            if user_name == row.user_name:
                user_found = True
                user_row_id = row.id
                save_o = self.savefile(game_stage=game_stage, user_id=user_row_id)
                session.add(save_o)
                session.commit()
                print("Game saved!")

        if not user_found:
            user_o = User(user_name=user_name)
            session.add(user_o)
            session.commit()
            rows_users = session.query(User).all()
            for row in rows_users:
                if user_name == row.user_name:
                    user_row_id = row.id
                    save_o = SaveFile(game_stage=game_stage, user_id=user_row_id)
                    session.add(save_o)
                    session.commit()
                    print("Game saved!")

    def load_game_display(self):
        rows_users = self.session.query(self.user).all()


# def load_gameffff():
#     try:
#         with open(SAVE_FILE, 'rb') as f:
#             state = pickle.load(f)
#         print("Game loaded!")
#         return state
#     except FileNotFoundError:
#         print("No saved game found!")
#         return None
