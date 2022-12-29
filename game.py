# Author: Zeeshan Mehdi
# Course : Advanced Programming
# Professor : Joseph Oakes
# Last Modified : 29 Dec 2022

from os import truncate
from types import new_class
import world
from player import Player
import pyfiglet

def play(self):
    print(pyfiglet.figlet_format("Welcome to Text Adventure Game!!"))
    print('You have three choices\n 1. Catacombs of Paris \n 2. Woods Adventure\n 3. Zombies Hunt')
    roomnumber = input('\nEnter your choice:')
    world.load_tiles(roomnumber)
    player = Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    action_input = None
    while player.is_alive():
        try:
            if player.victory==True:
                player = None
                playagain = input('\nWant to play next level. Type y/n: ')
                if playagain=='y':
                    player = Player()
                    roomnumber= ChooseGameArcade(roomnumber)
                    #room = world.tile_exists(player.location_x, player.location_y)
                else:
                    exit()
            room = world.tile_exists(player.location_x, player.location_y)        
            if not(action_input=='h' or action_input== 'p' or action_input == 't'):
                room.modify_player(player)
            # Check again since the room could have changed the player's state
            if player.is_alive() and not player.victory:
                print("Choose an action:\n")
                available_actions = room.available_actions(player)
                for action in available_actions:
                    print(action)
                action_input = input('Action: ')
                for action in available_actions:
                    if action_input == action.hotkey:
                        player.do_action(action, **action.kwargs)
                        break
        except Exception as ex:
            print(ex)

def ChooseGameArcade(roomnumber):   
    if roomnumber =='1':
        print('You have two choices\n 2. Woods Adventure\n 3. Zombies Hunt')
        
    elif roomnumber =='2':
        print('You have two choices\n 1. Catacombs of Paris\n 3. Zombies Hunt')

    else:
        print('You have two choices\n 1. Catacombs of Paris\n 2. Woods Adventure')
        
    roomnumber = input('\nEnter your choice:')      
    world.load_tiles(roomnumber)
    return roomnumber
    

if __name__ == "__main__":
    play(None)