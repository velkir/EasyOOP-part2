class Player:
    def __init__(self, name, hp, mp, skills=None, guild="Unaffiliated"):
        self.name = name
        self.hp = hp
        self.mana = mp
        self.skills = skills if skills else {}
        self.guild = guild

    def add_skill(self, skill_name, mana_cost):
        if not self.skills.get(skill_name):
            self.skills[skill_name]=mana_cost
            print(f"Skill {skill_name} added to {self.name}")
        else:
            print("Such a skill has already been added")

    def player_info(self):
        print(f"Name: {self.name}\n"
              f"Hp: {self.hp}\n"
              f"Mana: {self.mana}")
        if len(self.skills) > 0:
            print("Skills:")
            for skill_name, mana_cost in self.skills.items():
                print(f"Skill {skill_name} costs {mana_cost} mana")
        print(f"Guild: {self.guild}")

# player = Player("Adolf", 50, 35)
# player.player_info()
