import random

class Mage:
    def __init__(self):
        self.hp = random.randint(50, 70)
        self.dmg = random.randint(20, 30)
        self.mana = random.randint(100, 120)
        self.armor = random.randint(10, 30)
        self.weapon_type = "staff"
        self.armor_type = "cloth"
        self.abilities = ["Fireball", "Frostbolt", "Meditate"]


class Warrior:
    def __init__(self):
        self.hp = random.randint(100, 130)
        self.dmg = random.randint(30, 40)
        self.armor = random.randint(50, 70)
        self.weapon_type = "sword"
        self.armor_type = "mail"
        self.abilities = ["Slam", "Taunt", "Bash"]


class Rogue:
    def __init__(self):
        self.hp = random.randint(70, 100)
        self.dmg = random.randint(50, 60)
        self.armor = random.randint(50, 70)
        self.weapon_type = "dagger"
        self.armor_type = "leather"
        self.abilities = ["Shiv", "Stealth", "Backstab"]


class HeroClass:
    hero_classes = ["Mage", "Warrior", "Rogue"]
    mage_ults = ["Meteor Shower", "Blizzard"]
    warrior_ults = ["Earth Quake", "Whirlwind"]
    rogue_ults = ["Rupture", "Assassinate"]

    def __init__(self, hero_class):
        self.hero_class = hero_class
        if self.hero_class not in self.hero_classes:
            raise ValueError("Invalid Hero Class")

    def hp(self):
        match self.hero_class:
            case "Mage":
                return random.randint(50, 70)
            case "Warrior":
                return random.randint(80, 105)
            case "Rogue":
                return random.randint(75, 85)

    def ult(self):
        match self.hero_class:
            case "Mage":
                return random.choice(self.mage_ults)
            case "Warrior":
                return random.choice(self.warrior_ults)
            case "Rogue":
                return random.choice(self.rogue_ults)

    def __str__(self):
        return f"This champion is a {self.hero_class()}. They have {self.hp()} hit points and their ult is {self.ult()}"


class Battle(Hero, Enemy):
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy


jane = HeroClass("Mage")
print(jane.hero_class)
print(jane.hp())
print(jane.ult())


class Hero(HeroClass):
    pass
