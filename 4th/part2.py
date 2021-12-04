import numpy as np

def calc_sum(board, winning_number):
    board[board == -1] = 0

    print("We have a loser!")
    board_sum = np.concatenate(board).sum()
    print("board_sum = {}".format(board_sum))
    print("winning_number = {}".format(winning_number))

    return board_sum * winning_number

if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    # get bingo list
    bingo_list = clean_lines.pop(0).split(",")  # split commas
    bingo_list = list(map(int, bingo_list))  # make int
    print(bingo_list)

    # convert input to numpy matrix
    board_dim = 5
    n_boards = clean_lines.count('')
    table = np.zeros([n_boards, board_dim, board_dim])
    for i in range(n_boards):
        tmp_board = clean_lines[i * 6 + 1: (i + 1) * 6]
        for j in range(board_dim):
            table[i, j] = tmp_board[j].split()

    # LETS START THE BINGOOO
    score = 0
    for k in range(len(bingo_list)):
        table[table == bingo_list[k]] = -1

        # check for bingo
        col_vals = table.sum(axis=1)
        if np.any(col_vals == -5):
            winner_board = np.where(col_vals == -5)[0]
            if table.shape[0] == 1:
                score = calc_sum(table[0], bingo_list[k])
                break
            else:
                table = np.delete(table, winner_board, 0)

        row_vals = table.sum(axis=2)
        if np.any(row_vals == -5):
            winner_board = np.where(row_vals == -5)[0]
            if table.shape[0] == 1:
                score = calc_sum(table[0], bingo_list[k])
                break
            else:
                table = np.delete(table, winner_board, 0)

    print(score)




