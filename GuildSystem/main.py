from guild import Guild
from player import Player

guild = Guild("Hueta")
guild.guild_info()

hueglot = Player("Hueglot", 50, 30)
hueglot.add_skill("Harcha", 0)
hueglot.add_skill("Zaglot", 5)
hueglot.add_skill("Rasengan", 50)

kakashi = Player("Kakashi", 1000, 500)
kakashi.add_skill("Chidori", 200)
kakashi.add_skill("Katon: Gokakyu no Jutsu", 100)
kakashi.add_skill("Rasengan", 300)

guild.assign_player(hueglot)
guild.assign_player(kakashi)

guild.guild_info()

guild.assign_player(kakashi)
guild2 = Guild("Conter Hueta")
guild2.assign_player(kakashi)