class Warrior:
    def __init__(self, kick_pow, health):
        self.kick_pow = kick_pow
        self.health = health
        self.team = None


    def get_team(self):
        return self.team


class Knight(Warrior):
    def __init__(self, kick_pow=5, health=20):
        super().__init__(kick_pow, health)

    def __repr__(self):
        return "\nKnight: 5, 20"


class Archer(Warrior):
    def __init__(self, kick_pow=4, health=15):
        super().__init__(kick_pow, health)

    def __repr__(self):
        return "\nArcher: 4, 15"


class Spy(Warrior):
    def __init__(self, kick_pow=2, health=12):
        super().__init__(kick_pow, health)

    def __repr__(self):
        return "\nSpy: 2, 12"