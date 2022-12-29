import random 
import items, world
from sounds import sounds
from util import util
 
class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Pillow(), items.Rock(), 
        items.Slingshot(), items.Revolver(), items.Projectile(), 
        items.Moltov(), items.Crossbow(), items.SmallPotion(), items.BigPotion(), items.Sword()
        ] #Inventory on startup
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up
        self.util= util()
        self.sound= sounds()
        self.currentWpn=None
        self.chemical=False

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)
    
    def status(self, player):
        self.util.printGameText("Your hp status:")
        print("Current HP: ", self.hp)

    def heal(self, player):
        try:            
            print('\nThese are the potions you currently posses.\n')
            potion_list=[]        
            for potion in self.inventory:
                if isinstance(potion, items.Potion):
                    if potion.hp<=0:
                        self.inventory.remove(potion)
                    else:
                        potion_list.append(potion)
            i=1
            for potion in potion_list:
                print(i,". ", potion.name, sep='')
                i+=1
            while True:
                if len(potion_list)==0:
                    print("You have no potions")
                    return None
                
                itemChoice = self.util.getIntInput(description='Select the number of potion to heal: ')-1
                if itemChoice not in range(0, len(potion_list)):
                    print('\nInvalid choice')
                    self.sound.errorSound()
                    continue
                break
            self.healToPlayer(itemChoice=itemChoice, potionList=potion_list)
        except Exception as ex:
            print(ex)
    
    def healToPlayer(self, itemChoice, potionList):
        chosenPotion = potionList[itemChoice]
        self.util.printGameText("\nYou were healed for {}".format(chosenPotion.hp))
        self.util.printGameText("hp\n")
        if not(self.hp+chosenPotion.hp>100):
            self.hp=self.hp+chosenPotion.hp
        else:
            self.hp=100
        chosenPotion.hp=0
        self.sound.drinkSound()       

    def equip(self, player):
        try:            
            print("\nThese are the weapons availalbe.\n")
            weapon_list =[]
            for item in self.inventory:
                if isinstance(item, items.Weapon):
                    weapon_list.append(item)
            i = 1
            for weapon in weapon_list:
                print(i, ". ", weapon.name, sep='')
                i+=1
            
            while True:
                itemChoice = self.util.getIntInput(description='Select the number of weapon to equip: ')-1
                if itemChoice not in range(0, len(weapon_list)):
                    print('Invalid weapon choice')
                    sounds.errorSound()
                    continue
                break
            print('\n')        
            print(weapon_list[itemChoice].name, "equipped.\n")
            self.currentWpn= weapon_list[itemChoice]
                 
            #add util.py                                                       
        except Exception as ex:
            print(ex)



    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        
        # for i in self.inventory:
        #  if isinstance(i, items.Weapon):             
        #     if i.maxDamage > max_dmg:
        #         max_dmg = i.maxDamage
        #         best_weapon = i
        if self.currentWpn==None:
            self.currentWpn= items.Rock()

        self.currentWpn.soundeffect()
        print("You use {} against {}!".format(self.currentWpn.name, enemy.name))
        enemy.hp -= random.randint(self.currentWpn.minDamage, self.currentWpn.maxDamage)        
        if not enemy.is_alive():
            self.sound.KillSound()
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):        
        try:
            action_method = getattr(self, action.method.__name__)
            if action_method:
                action_method(**kwargs)
        except Exception as ex:
            print(ex)