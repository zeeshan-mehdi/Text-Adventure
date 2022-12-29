class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class Dog(Enemy):
    def __init__(self):
        super().__init__(name="Dog", hp=20, damage=10)

class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=15)
class Dead(Enemy):
    def __init__(self):
        super().__init__(name="Dead", hp=25, damage=15)
class StrangeCreature(Enemy):
    def __init__(self):
        super().__init__(name="Strange Creature", hp=25, damage=15)
class Hellhound(Enemy):
    def __init__(self):
        super().__init__(name="Hellhound", hp=15, damage=15)

class RatHumanoid(Enemy):
    def __init__(self):
        super().__init__(name="RatHumanoid", hp=45, damage=5)

class Bats(Enemy):
    def __init__(self):
        super().__init__(name="Bats", hp=15, damage=5)

class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", hp=15, damage=5)

class Crawler(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", hp=15, damage=3)

class TigerHerd(Enemy):
    def __init__(self):
        super().__init__(name="Tiger", hp=25, damage=15)


class Elephant(Enemy):
    def __init__(self):
        super().__init__(name="Elephant", hp=50, damage=20)

class Bear(Enemy):
    def __init__(self):
        super().__init__(name="Bear", hp=20, damage=5)

class Snake(Enemy):
    def __init__(self):
        super().__init__(name="Snake", hp=5, damage=5)


class Lion(Enemy):
    def __init__(self):
        super().__init__(name="Lion", hp=40, damage=20)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=50, damage=25)