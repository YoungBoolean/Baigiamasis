from database.db import session
from database.models import SaveFile, User


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
                self.session.add(save_o)
                self.session.commit()
                print("Game saved!")
                break

        if not user_found:
            user_o = User(user_name=user_name)
            self.session.add(user_o)
            self.session.commit()
            user_row_id = user_o.id
            save_o = SaveFile(game_stage=game_stage, user_id=user_row_id)
            self.session.add(save_o)
            self.session.commit()
            print("Game saved!")

    def get_saved_games(self):
        savegame_list = []
        rows_users = self.session.query(self.user).all()
        for row in rows_users:
            for save_row in row.save_files:
                savegame_list.append([row.id, row.user_name, save_row.game_stage, save_row.date])

        if savegame_list:
            return savegame_list
        else:
            return None

    def get_last_save(self):
        savegame = None
        username = None
        user_id = None
        rows_savefiles = self.session.query(self.savefile).all()
        if rows_savefiles:
            for row in rows_savefiles:
                savegame = row.game_stage
                user_id = row.user_id
                break
            rows_users = self.session.query(self.user).all()
            for row in rows_users:
                if row.id == user_id:
                    username = row.user_name
        return savegame, username


savestate = SaveState()
