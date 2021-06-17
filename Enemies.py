class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super(Goblin, self).__init__(100, 5)
        print("Glbglbglb, I am a goblin and will slash you")


class Rat(Enemy):
    def __init__(self):
        super(Rat, self).__init__(100, 10)
        print("I am a super rat and will eat your brains")


class Orc(Enemy):
    def __init__(self):
        super(Orc, self).__init__(100, 15)
        print("Wroooaarr, I am an orc and will crush you")

