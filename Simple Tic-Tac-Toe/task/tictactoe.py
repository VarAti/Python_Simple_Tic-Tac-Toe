# write your code here
board_state = ""


def check_horizontal_rows(symbol):
    horizontal_row_count = 0
    for i in range(3):
        for k in range(3):
            if board[i][k] != symbol:
                break
        else:
            horizontal_row_count += 1
    return horizontal_row_count


def check_vertical_rows(symbol):
    vertical_row_count = 0
    for i in range(3):
        for k in range(3):
            if board[k][i] != symbol:
                break
        else:
            vertical_row_count += 1
    return vertical_row_count


def check_diagonal_rows(symbol):
    diagonal_row_count = 0
    for i in range(3):
        if board[i][i] != symbol:
            break
    else:
        diagonal_row_count += 1
    k = 0
    for i in range(2, -1, -1):
        if board[i][k] != symbol:
            break
        k += 1
    else:
        diagonal_row_count += 1
    return diagonal_row_count


def count_cells(symbol):
    count = 0
    for row in board:
        for cell in row:
            if cell == symbol:
                count += 1
    return count


def check_board_is_valid():
    global board_state
    rows_count_o = check_horizontal_rows('O') + check_vertical_rows('O') + check_diagonal_rows('O')
    rows_count_x = check_horizontal_rows('X') + check_vertical_rows('X') + check_diagonal_rows('X')

    if rows_count_x > 2 or rows_count_o > 2:
        board_state = "Impossible"
        return False
    elif rows_count_x == 1 and rows_count_o == 1:
        board_state = "Impossible"
        return False
    elif abs(count_cells('O') - count_cells('X')) > 1:
        board_state = "Impossible"
        return False
    elif rows_count_x == 1:
        board_state = "X wins"
        return False
    elif rows_count_o == 1:
        board_state = "O wins"
        return False
    elif count_cells(' ') > 0:
        board_state = "Game not finished"
        return True
    else:
        board_state = "Draw"
        return False


def print_board():
    print("---------")
    for row in board:
        print('| ' + " ".join(row) + ' |')
    print("---------")


# only used during testing the game logic
def init_test_board():
    cells = input("Enter cells: ")
    cells = cells.replace("_", " ", cells.count('_'))
    print("---------")
    for i in range(0, 9, 3):
        row = [cells[i] for i in range(i, i + 3)]
        board.append(row)
        print('| ' + " ".join(row) + ' |')
    print("---------")


board = [[' ' for i in range(3)] for k in range(3)]
player_symbol = (' ', 'O', 'X')
symbol_index = 1
while check_board_is_valid():
    try:
        x, y = input("Enter the coordinates: ").split()
        x = int(x) - 1
        y = int(y) - 1
        assert (x < 3 and y < 3)
    except AssertionError:
        print("Coordinates should be from 1 to 3!")
        continue
    except TypeError:
        print("You should enter numbers!")
        continue
    if board[x][y] != ' ':
        print("This cell is occupied! Choose another one!")
        continue
    else:
        board[x][y] = player_symbol[symbol_index]
        symbol_index = -symbol_index
        print_board()

print(board_state)
