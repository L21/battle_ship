# Use these constants in your code 

MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_GRID_SIZE = 10
UNKNOWN = '-'
EMPTY = '.'
HIT = 'X'
MISS = 'M'


def read_ship_data(game_file):

    """ (file open for reading) -> list of list of objects

    Return a list containing the ship characters in game_file as a list 
    of strings at index 0, and ship sizes in game_file as a list of ints 
    at index 1.
    """

    # complete the function body for read_ship_data here
    #read the ship character and ship size in the file
    ship_character_string = game_file.readline().strip("\n")
    ship_size_string = game_file.readline().strip("\n")
    ship_character_list = []
    ship_size_list = []
    #loop the ship character string and ship size string
    #add ship character and ship size to corresponding list
    for index in range(0, len(ship_character_string),2):
        ship_character_list.append(ship_character_string[index])
        ship_size_list.append(int(ship_size_string[index]))
    #return the final list
    return [ship_character_list, ship_size_list]




# Write the rest of the required functions here
# Don't forget to follow the Function Design Recipe
def has_ship(fleet_grid, row_index, column_index, ship_character, size):
    
    '''list of list of str, int, int, str, int) -> bool

    Return True iff the ship(depend on ship_character) appears with the correct
    size at the starting point(row_index, column_index), completely 
    in a row or a completely in a column at the given starting cell.

    >>> grid = [['a','a','.'],['.','a','.'],['.','a','.']]
    >>> has_ship(grid, 0, 0, 'a', 3)
    False

    >>> grid = [['a','.','a'],['.','a','.'],['.','a','.']]
    >>> has_ship(grid, 1, 1, 'a', 2)
    True

    >>> grid = [['a','.','a'],['.','a','.'],['.','a','.']]
    >>> has_ship(grid, 0, 0, 'a', 3)
    False
    '''
   
    #use row_ship_number to record the continous cell of the ship
    row_ship_number = 0
    #loop the right side of the starting point
    for index in range(0, len(fleet_grid[row_index])):
        if index >= column_index:
            if fleet_grid[row_index][index] == ship_character:
                row_ship_number += 1
                #if number of continous cell of the ship reach the ship size
                #it means there is a ship
                if (size <= row_ship_number):
                    return True
            else:
                row_ship_number = 0
    #use column_ship_number to record the continous cell of the ship
    column_ship_number = 0
    #loop the bottom side of the starting point
    for index in range(0, len(fleet_grid)):
        if index >= row_index:
            if fleet_grid[index][column_index] == ship_character:
                column_ship_number += 1
                #if number of continous cell of the ship reach the ship size
                #it means there is a ship
                if (size <= column_ship_number):
                    return True
            else:
                column_ship_number = 0
    #if there is no ship here, then it should be false
    return False


def validate_character_count(fleet_grid, ship_character, ship_size):
    
    """(list of list of str, list of str, list of int) -> bool

    Return True iff the grid contains the correct number of ship 
    characters for each ship(equals to the number in ship_size), 
    and the correct number of EMPTY characters.

    >>> grid = [['a','.','.'],['.','a','.'],['.','a','.']]
    >>> validate_character_count(grid, ['a'], [3])
    True
    >>> grid = [['a','p','.'],['.','a','.'],['.','a','.']]
    >>> validate_character_count(grid, ['a'], [3])
    False
    """

    #put all the elemnet in fleet_grid in one list
    grid_list = []
    for index_row in range(0, len(fleet_grid)):
        for index_column in range(0, len(fleet_grid[index_row])):
            grid_list.append(fleet_grid[index_row][index_column])
    #use the count to check whether it is the correct number of 
    #each ship character
    for index_ship in range(0, len(ship_character)):
        if grid_list.count(ship_character[index_ship]) \
        != ship_size[index_ship]:
            return False
    #get the fleet_grid size
    fleet_grid_size = len(fleet_grid) * len(fleet_grid[0])
    #if sum of the ship size add number of '.' not equals to 
    #the fleet_grid size, then it should return false
    if (fleet_grid_size - grid_list.count(EMPTY)) != sum(ship_size):
        return False

    return True


def validate_ship_positions(fleet_grid, ship_character, ship_size):
    
    """(list of list of str, list of str, list of int) -> bool

    Return True iff the fleet_grid contains each ship(depend on ship_character)
    aligned completely in a row or column.

    >>> grid = [['a','.','.'],['.','a','.'],['.','a','.']]
    >>> validate_ship_positions(grid, ['a'], [3])
    False
    >>> grid = [['p','p'],['.','.']]
    >>> validate_ship_positions( grid, ['p'], [2])
    True
    """
    #use correct to record the number of ship character 
    #which satisfied the ship position
    correct = 0
    #check each character in ship_character
    for ship in ship_character:
        #use finish to check whether we found a ship or not
        finish = False
        for index_row in range(0, len(fleet_grid)):
            if not finish:
                for column_index in range(0, len(fleet_grid[index_row])):
                    if not finish:
                        #if the element is the character which we need to check
                        #then call the has_ship function to find a valid ship
                        if fleet_grid[index_row][column_index] == ship:
                            if has_ship(fleet_grid, index_row, column_index, \
                                ship, ship_size[ship_character.index(ship)]):
                                finish = True
                #if found a ship, then add one to correct
                if finish:
                    correct += 1
    #if correct = the number of ship character we need to check
    #it means all the for every character there is a valid ship
    return correct == len(ship_character)





def validate_fleet_grid(fleet_grid, ship_character, ship_size):
    
    """(list of list of str, list of str, list of int) -> bool

    Return True iff the potential fleet grid is a valid fleet grid
    depend on ship_character and ship_size 

    >>> grid = [['a','a','.'],['.','a','.'],['.','a','.']]
    >>> validate_fleet_grid( grid, ['a'], [3])
    False
    >>> grid = [['.','a','.'],['.','a','.'],['.','a','.']]
    >>> validate_fleet_grid( grid, ['a'], [3])
    True
    >>> grid = [['p','a','.'],['.','a','.'],['.','a','.']]
    >>> validate_fleet_grid( grid, ['a'], [3])
    False
    """
    #if the number is correct and for all the character, there exits a ship
    #then this function should return True. Otherwise, return False
    return (validate_character_count(fleet_grid, ship_character, ship_size)) \
    and (validate_ship_positions(fleet_grid, ship_character, ship_size))
    
def valid_cell(row_index, column_index, grid_size):
    
    """(int, int, int) -> bool

    Return True iff the cell specified by the row_index and the 
    column_index is a valid cell inside a square grid of that size.

    >>> valid_cell(0, 1, 2)
    True
    >>> valid_cell(5, 1, 5)
    False
    """
    #the max of row_index and column size is grid_size - 1
    return ((row_index <= (grid_size - 1)) \
        and (column_index <= (grid_size - 1)))

def is_not_given_char(row_index, column_index, grid, given_char):
    
    """(int, int, list of list of str, str) -> bool

    Return True iff the cell specified by the row_index and 
    column_index is not the given character.

    >>> grid = [['p','a','.'],['.','a','.'],['.','a','.']]
    >>> is_not_given_char( 0, 0, grid, 'p')
    False
    >>> grid = [['p','a','.'],['.','a','.'],['.','a','.']]
    >>> is_not_given_char( 0, 1, grid, 'p')
    True
    """
    #check whether grid[row_index][column_index] is the given char or not
    return (grid[row_index][column_index] != given_char)

def update_fleet_grid(row_index, column_index, fleet_grid, ship_character, 
    size, hit_list):
    
    """(int, int, list of list of str, list of str, list of int, 
        list of int) -> NoneType

    Update the fleet grid(depend on row_index and column_index) by converting
    the ship character in the cell to upper-case, and also update hits list 
    to show that there has been a hit. If a ship is sunk then call the 
    print_sunk_message() to show the message

    >>> grid = [['p','a','.'],['.','a','.'],['.','a','.']]
    >>> hit_list = [2, 0]
    >>> update_fleet_grid( 0, 1, grid, ['a', 'p'],[3, 1],hit_list)
    The size 3 a ship has been sunk!
    >>> grid
    [['p', 'A', '.'], ['.', 'a', '.'], ['.', 'a', '.']]
    >>> hit_list
    [3, 0]
    
    """
    #get the ship character
    ship = fleet_grid[row_index][column_index]
    #change to upper case
    fleet_grid[row_index][column_index] = ship.upper()
    #get the index of that character in ship_character
    ship_index = ship_character.index(ship)
    #update the hit_list, add one arrcoding to the corresponding index
    hit_list[ship_index] += 1
    #check whether the ship is sunk or not
    if hit_list[ship_index] == size[ship_index]:
        print_sunk_message(size[ship_index], ship)

def update_target_grid(row_index, column_index, target_grid, fleet_grid):
    
    """(int, int, list of list of str, list of list of str) -> NoneType

    Set the element of the specified cell(depend on row_index and column_index)
    in the target grid to HIT or MISS using the information from the 
    corresponding cell from the fleet grid.

    >>> target_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> fleet_grid = [['p', 'A', '.'], ['.', 'a', '.'], ['.', 'a', '.']]
    >>> update_target_grid(0, 1, target_grid, fleet_grid)
    >>> target_grid
    [['-', 'X', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> update_target_grid(0, 0, target_grid, fleet_grid)
    >>> target_grid
    [['M', 'X', '-'], ['-', '-', '-'], ['-', '-', '-']]
    """
    #check the hit or miss by '.' or lower case
    cell = fleet_grid[row_index][column_index]
    if (cell !=  EMPTY)  and cell.isupper():
        target_grid[row_index][column_index] = HIT
    else:
        target_grid[row_index][column_index] = MISS

def is_win(ship_size, hit_list):
    
    """(list of int, list of int) -> bool

    Return True iff the number of hits for each ship in the hits list
    is the same as the size of each ship in ship_size

    >>> ship_size = [2, 0]
    >>> hit_list = [1, 0]
    >>> is_win(ship_size, hit_list)
    False

    >>> ship_size = [2, 0]
    >>> hit_list = [2, 0]
    >>> is_win(ship_size, hit_list)
    True
    """
    #if one element of the hit_list is not equal to 
    #correspond number in ship size, then it means that the ship is not sunk
    #then return False
    for index in range(0, len(ship_size)):
        if ship_size[index] != hit_list[index]:
            return False
    return True
##################################################
## Helper function to call in update_fleet_grid
## Do not change!
##################################################

def print_sunk_message(ship_size, ship_character):
    """ (int, str) -> NoneType
  
    Print a message telling player that a ship_size ship with ship_character
    has been sunk.
    """

    print('The size {0} {1} ship has been sunk!'.format(ship_size, ship_character))
    
    
if __name__ == '__main__':
    import doctest
   
    # uncomment the line below to run the docstring examples     
    doctest.testmod()
           
