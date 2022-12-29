# Base class for all items
from inspect import classify_class_attrs

from sounds import sounds


class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
        self.sound= sounds()
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt): 
        self.amt = amt # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, minDamage, maxDamage):
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nMinimum Damage: {}\nMaximum Damage: {}".format(self.name, self.description, self.value, self.minDamage, self.maxDamage)
    
    def soundeffect(self):
        self.sound.PunchSound()
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         minDamage=3, maxDamage=5)
    def soundeffect(self):
        self.sound.PunchSound()
 
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         minDamage=8, maxDamage=10)
    def soundeffect(self):
        self.sound.DaggerSound()

class Pillow(Weapon):
    def __init__(self):
        super().__init__(name="Pillow",
                         description="A pillow super soft.",
                         value=1,
                         minDamage=1, maxDamage=1)                         
    
    def soundeffect(self):
        self.sound.PillowSound()

class Projectile(Weapon):
    def __init__(self):
        super().__init__(name="Projectile",
                         description="A Projectile easy to throw, Better than a pillow but not hard like rock.",
                         value=1,
                         minDamage=2, maxDamage=3)

    def soundeffect(self):
        self.sound.ProjectileSound()

class Crossbow(Weapon):
    def __init__(self):
        super().__init__(name="Crossbow",
                         description="A Crossbow lethal as compared to a dagger",
                         value=20,
                         minDamage=20, maxDamage=25)
    
    def soundeffect(self):
        self.sound.CrossbowSound()

class Moltov(Weapon):
    def __init__(self):
        super().__init__(name="Moltov",
                         description="A Moltov best weapon to distract, yes it is dangerous",
                         value=20,
                         minDamage=10, maxDamage=15)

    def soundeffect(self):
        self.sound.MoltovSound()

class Revolver(Weapon):
    def __init__(self):
        super().__init__(name="Revolver",
                         description="A Revolver lethal modern weapon to kill",
                         value=25,
                         minDamage=15, maxDamage=30)
    
    def soundeffect(self):
        self.sound.RevolverSound()

class Slingshot(Weapon):
    def __init__(self):
        super().__init__(name="Slingshot",
                         description="A Slingshot hits harder than a rock",
                         value=2,
                         minDamage=3, maxDamage=5)

    def soundeffect(self):
        self.sound.SlingshotSound()

class Potion(Item):
    def __init__(self, name, description, value, hp):        
        self.hp = hp
        super().__init__(name, description, value)
 
    def __str__(self):
        return "\nValue: {}\nHeal: {}".format(self.name, self.hp)

class SmallPotion(Potion):
    def __init__(self):
        super().__init__(name="Small Potion",description= "Small potion will add 15 hp", value=0, hp=15)

class BigPotion(Potion):
    def __init__(self):
        super().__init__(name="Big Potion",description= "Big potion will add 30 hp", value=0, hp=30)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A Sword lethal ancient weapon ",
                         value=20,
                         minDamage=20, maxDamage=25)

    def soundeffect(self):
        self.sound.SwordSound()