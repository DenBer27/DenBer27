import random


def get_attack_power(min_attack, max_attack):
    return random.randint(min_attack, max_attack)

class Hero():

    def __init__(self, race, name, lvl=1):
        self.race = race
        self.name = name
        self.lvl = lvl
        # self.team = team

    def __str__(self):
        return f"\nИнформация о герое '{self.name}' расы {self.race}\nсила = {self._strong}\nинтеллект = {self._intelligence}\nвыносливость = {self._resistance}\nздоровье = {self._health}\nмагия = {self._magic}\nуровень = {self.lvl}"

    def increase_level(self):
        # if my_hero1 is win:
        self.lvl += 1


    def get_attack_power(min_attack, max_attack):
        return random.randint(min_attack, max_attack)


class Human(Hero):
    def __init__(self, race, name):
        super().__init__(race, name)
        self.attack_power = 18
        self.intelligence = 12
        self.defence = 6
        self.health = 80
        self.magic = 80


class Dwarf(Hero):
    def __init__(self, race, name):
        super().__init__(race, name)
        self.attack_power = 22
        self.intelligence = 7
        self.defence = 10
        self.health = 50
        self.magic = 50



class Elf(Hero):
    def __init__(self, race, name):
        super().__init__(race, name)
        self.attack_power = 16
        self.intelligence = 15
        self.defence = 8
        self.health = 100
        self.magic = 100



