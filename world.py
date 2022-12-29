import pyfiglet
_world = {}
starting_position = (0, 0)
 
def load_tiles(roomnumber):
    """Parses a file that describes the world space into the _world object"""
    if roomnumber == '1':
        print(pyfiglet.figlet_format("Welcome to Catacombs of Paris!!"))
        with open('paris-map.txt', 'r') as f:
            rows = f.readlines()

    elif roomnumber == '2':
        print(pyfiglet.figlet_format("Welcome to Woods Adventure!!"))
        with open('advent-map.txt', 'r') as f:
            rows = f.readlines()
    else:
        print(pyfiglet.figlet_format("Welcome to Zombies Hunt!!"))
        with open('zombie-map.txt', 'r') as f:
            rows = f.readlines()
    x_max = len(rows[0].split('|')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('|')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            if tile_name == 'StartingRoom' or tile_name == 'StartingWoodsAdvent' or tile_name == 'StartingZombiesHunt':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))