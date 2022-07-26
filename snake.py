print('Hello player! This is a game called "Snake" where you eat food and grow.\nFirst of all, decide what size a filed should be.')
row_n = int(input('Enter number of rows: '))
column_n = int(input('Enter number of columns: '))

def draw_map(snake, food):
    table = []
    for row in range(row_n):
        row = []
        for column in range(column_n):
            row.append(".")
        table.append(row)

    for row, column in snake:
        table[row][column] = 'X'
    
    for row, column in food:
        table[row][column] = '♥'

    for row in table:
        print(" ".join(row))
        
from random import randrange

def add_food(list_coordinates, food):
    while True:
        random_coordinates = (randrange(0,row_n), randrange(0,column_n))
        if random_coordinates not in list_coordinates:
            food.append(random_coordinates)
            break

def move(list_coordinates, direction_key, food): 
    
    directions = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1),'w': (0, -1)}
    move_side = directions[direction_key]
    last_coordinates = list_coordinates[-1]
    new_coordinates = (last_coordinates[0] + move_side[0], last_coordinates[1] + move_side[1])
    
    if new_coordinates in list_coordinates:
        input('Snake tried to eat itself! Try another direction: ')
    elif new_coordinates[0]<0 or new_coordinates[0]>row_n-1 or new_coordinates[1]<0 or new_coordinates[1]>column_n-1:
        input('Snake tried to move out of the map. Try another direction: ')
    else:    
        list_coordinates.append(new_coordinates)

    if new_coordinates in food:
        food.remove(new_coordinates)
        if not food:
            add_food(list_coordinates, food)
    else:
        list_coordinates.pop(0)
  
def snake_game():
    list_coordinates = [(0,0),(0,1),(0,2)]
    food = [(2,3)]
    draw_map(list_coordinates, food)
    while True: 
        direction = input('Enter the direction of movement: "n" - north, "e" - east, "s" - south, "w" - west:\nIf you want to stop the game write "end" ')
        if direction not in "neswend": 
            print("Wrongly entered direction!")
        elif direction == '':
            print("You need to choose a direction!")   
        elif direction == 'end':
            print()
            print("You stopped the game")
            break
        else:
            move(list_coordinates, direction, food)
            draw_map(list_coordinates, food)

snake_game()
