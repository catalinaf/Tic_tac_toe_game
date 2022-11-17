from os import system

cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

cells_mapping = {
    'a1': 0, 'b1': 1, 'c1': 2,
    'a2': 3, 'b2': 4, 'c2': 5,
    'a3': 6, 'b3': 7, 'c3': 8,
}

possible_input = list(cells_mapping.keys())

def get_input(symbol):
    player_input = ' '

    while player_input not in possible_input:
        player_input = input(f"{symbol} turn: ").lower()
    possible_input.remove(player_input)

    return player_input


def update_and_print_grid():
    grid = f'''
        a   b   c 
    
    1   {cells[0]} | {cells[1]} | {cells[2]} 
       -----------
    2   {cells[3]} | {cells[4]} | {cells[5]} 
       -----------
    3   {cells[6]} | {cells[7]} | {cells[8]} 
    '''

    print(grid)

def check_winner(introduced_symbol):
    winning_sets = [
        [cells[0], cells[1], cells[2]], 
        [cells[3], cells[4], cells[5]], 
        [cells[6], cells[7], cells[8]],
        [cells[0], cells[3], cells[6]],                
        [cells[1], cells[4], cells[7]],                   
        [cells[2], cells[5], cells[8]],                                   
        [cells[0], cells[4], cells[8]], 
        [cells[2], cells[4], cells[6]]                                
    ]

    game_on = True
    for set in winning_sets:
        if all(x==set[0] for x in set) and introduced_symbol in set:
            print(f"{introduced_symbol} is the winner!")
            game_on = False
    
    return game_on

update_and_print_grid()

game_on = True
while game_on:
    x_player_input = get_input('X')
    cells[cells_mapping[x_player_input]] = 'X'
    system('clear')
    update_and_print_grid()
    game_on = check_winner(cells[cells_mapping[x_player_input]])
    if ' ' not in cells:
        print("It's a draw.")
        break
    elif game_on == False:
        break

    o_player_input = get_input('O')
    cells[cells_mapping[o_player_input]] = 'O'
    system('clear')
    update_and_print_grid()
    game_on = check_winner(cells[cells_mapping[o_player_input]])
