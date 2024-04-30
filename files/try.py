class Monster:
    def __int__(self, health, energy, speed):
        self.health = health
        self.energy = energy
        self.speed = speed

    def move(self):
        print(f"the monster has moved with a speed of {self.speed}")


monster = Monster(100,10,111)
