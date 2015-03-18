import pickle
class Game:
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.players = None
        self.online = None
game_file = []
def load_games(filename):
    games = []
    try:
        with open("games.dat", mode = "rb")as binary_file:
           games = pickle.load(binary_file)
    except IOError:
        print("Error: can't find file or read data")
    return games

def save_games(filename, games):
    with open ("games.dat", mode = "wb")as binary_file:     
        pickle.dump(games,binary_file)

#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games):  
    print("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|".format("Name", "Platform", "Genre", "Cost", "Players", "Online ability"))
    for game in games:
        print("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|".format(game.name, game.platform, game.genre, game.cost, game.players, game.online))

def get_game_from_user(games):
    carry_on_asking = False
    while not carry_on_asking:
        game = Game()
        game.name = input("Enter the game name: ")
        if game.name == "-1":
            carry_on_asking = True
        else:
            game.platform = input("Enter the platform: ")
            game.genre = input("Enter the game genre: ")
            game.cost = float(input("Enter the game cost: "))
            game.players = int(input("Enter the number of players: "))
            game.online = input("Enter the online functionality of the game: ")
            games.append(game)
    return games

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    exit_program = False
    games = []
    filename = "games.dat"
    games = load_games("games.dat")
    while not exit_program:
        display_menu()
        selected_option = input("Please select a menu option: ")
        if selected_option == "1":
            games = get_game_from_user(games)
        elif selected_option == "2":
            display_games(games)
        elif selected_option == "3":
            save_games("games.dat", games)
            exit_program = True
        else:
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()
