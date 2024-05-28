import pickle

SAVE_FILE = 'save_file.pkl'


def save_game(state):
    with open(SAVE_FILE, 'wb') as f:
        pickle.dump(state, f)
    print("Game saved!")


def load_game():
    try:
        with open(SAVE_FILE, 'rb') as f:
            state = pickle.load(f)
        print("Game loaded!")
        return state
    except FileNotFoundError:
        print("No saved game found!")
        return False
