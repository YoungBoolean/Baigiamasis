"""
save_states.py

This module contains SQLAlchemy imports.
This module provides functionality related to saving game states in the database.
"""

from .db import session
from .models import SaveFile, User, Items


class SaveState:
    """Responsible for creating database queries, returning save_game rows from database"""

    def __init__(self, session=session, user=User, savefile=SaveFile):
        self.session = session
        self.user = user
        self.savefile = savefile

    def save_game(self, game_stage, user_name, items: list):
        """
        Saves the current game state for the specified user. If user does not exist in the database,
        it is created and the game is saved to it.
        """
        rows_users = self.session.query(self.user).all()
        user_found = False

        for row in rows_users:
            if user_name == row.user_name:
                user_found = True
                user_row_id = row.id
                save_o = self.savefile(game_stage=game_stage,
                                       user_id=user_row_id)
                self.session.add(save_o)
                break

        if not user_found:
            user_o = User(user_name=user_name)
            self.session.add(user_o)
            self.session.commit()
            user_row_id = user_o.id
            save_o = SaveFile(game_stage=game_stage,
                              user_id=user_row_id)
            self.session.add(save_o)

        # Add items to the save file
        new_item = Items(
            money=items[0],
            pigeon_money=items[1],
            camel_blue=items[2],
            save_file=save_o)

        self.session.add(new_item)

        # Commit the transaction
        self.session.commit()
        print("Game saved!")

    def get_saved_games(self):
        """
        Returns saved games from the database.
        The saved games are filtered by user and ordered in a descending order
        """
        savegame_list = []
        rows_users = self.session.query(self.user).all()
        for row in rows_users:
            save_files = self.session.query(self.savefile).filter_by(user_id=row.id).order_by(
                self.savefile.id.desc()).all()
            for save_file in save_files:
                for item in save_file.items:
                    savegame_list.append(
                        [row.id, row.user_name, save_file.game_stage, save_file.date, item.money, item.pigeon_money,
                         item.camel_blue])

        return savegame_list if savegame_list else None

    def get_last_save(self):
        """Returns the last saved game from the database."""
        last_save = self.session.query(self.savefile).order_by(self.savefile.id.desc()).first()
        if last_save:
            savegame = last_save.game_stage
            items = [(item.money, item.pigeon_money, item.camel_blue) for item in last_save.items]
            user_id = last_save.user_id
            user = self.session.query(self.user).filter_by(id=user_id).first()
            if user:
                username = user.user_name
                return savegame, username, items
        return None, None, None

    def delete_user(self, username):
        """Deletes user and it's save files when the game_state is game_over"""
        user_to_delete = self.session.query(self.user).filter_by(user_name=username).first()
        if user_to_delete:
            self.session.delete(user_to_delete)
            self.session.commit()
            print(f"User '{username}' and their save files have been deleted!")
        else:
            print(f"No user found with the name '{username}'.")


savestate = SaveState()
