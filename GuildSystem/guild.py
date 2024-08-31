from player import Player
class Guild:
    def __init__(self, name, players=None):
        self.name = name
        self.players = players if players else []

    def assign_player(self, player):
        if isinstance(player, Player):
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                print(f"Player {player.name} assigned to {self.name} guild.")
            else:
                print(f"Player {player.name} is already in {player.guild} guild.")
        else:
            print("Error.")

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                print(f"Player {player_name} successfully kicked from {self.name}")
                break
        print(f"There is no player {player_name} in {self.name}")

    def guild_info(self):
        print(f"Guild name: {self.name}")
        if len(self.players) > 0:
            print("Players: ")
            for player in self.players:
                player.player_info()
                print()
        else:
            print(f"Guild {self.name} has no players yet")

