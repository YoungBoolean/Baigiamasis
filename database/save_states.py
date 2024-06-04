from .db import session
from .models import SaveFile, User


class SaveState:
    """Responsible for creating database queries, returning save_game rows from database"""
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
            save_files = self.session.query(self.savefile).filter_by(user_id=row.id).order_by(
                self.savefile.id.desc()).all()
            for save_file in save_files:
                savegame_list.append([row.id, row.user_name, save_file.game_stage, save_file.date])

        return savegame_list if savegame_list else None

    def get_last_save(self):
        last_save = self.session.query(self.savefile).order_by(self.savefile.id.desc()).first()
        if last_save:
            savegame = last_save.game_stage
            user_id = last_save.user_id
            user = self.session.query(self.user).filter_by(id=user_id).first()
            if user:
                username = user.user_name
                return savegame, username
        return None, None

    def delete_user(self, username):
        """Delete user and it's save files when game over or delete user button is pressed"""
        user_to_delete = self.session.query(self.user).filter_by(user_name=username).first()
        if user_to_delete:
            self.session.delete(user_to_delete)
            self.session.commit()
            print(f"User '{username}' and their save files have been deleted!")
        else:
            print(f"No user found with the name '{username}'.")


savestate = SaveState()
