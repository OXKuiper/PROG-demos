def game_easy(rows, cols, nbombs=1):
    """Bomb finding game"""

    import random
    # get a random list of bombs-and-blanks equal amount of the total fields
    grid_as_list = (['_']*(rows*cols-nbombs) + ['B']*nbombs)
    random.shuffle(grid_as_list)
    print(grid_as_list)

    # generate a grid of size rows*cols based on list
    grid = [] # lege grid
    for i in range(rows):
        row = [] # we voegen per row toe
        for j in range(cols):
            # We pakken element i*cols+j uit de lijst... Reden:
            # Door i*cols pak je eerst de eerste rij (i=0), dan de 2e rij (i=1) etc
            # Bijv bij 2*3 grid, doen we eerst de eerste row van 3, dan de 2e row
            #                    [00,01,02,  10,11,12]
            # print(f'We nemen item uit lijst {i*cols+j}')
            row.append(grid_as_list[i*cols+j])
        grid.append(row) # Volgende i, dus volgende row

    # printen
    for row in grid:
        for col in row:
            print(' ' + col + ' ', end='') # geen \n zodat op zelfde regel geprint
        print('')

    # #  simple way to get input
    while True:
        pos = input(f'Enter next position (format: row (1-{rows}) col (1-{cols}): ')
        guess_row, guess_col = pos.split()
        if grid[int(guess_row)-1][int(guess_col)-1] == 'B':
            print('Bomb found!')
            break
        else:
            print('Guess again!')

game_easy(3,4)
