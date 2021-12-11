import numpy as np


def flash(table, row, col, _flash_check):
    table[row, col] = 0

    # increase all neighbours
    for _row in range(row - 1, row + 2):
        for _col in range(col - 1, col + 2):
            if _row < 0 or _col < 0:
                continue
            if _row == row and _col == col:
                continue

            try:
                if _flash_check[_row, _col] == 0:
                    table[_row, _col] += 1
            except IndexError:
                pass


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    # convert input to numpy matrix
    board_dim = len(clean_lines[0])
    energy = np.zeros([board_dim, board_dim]).astype(int)
    for i in range(board_dim):
        energy[i] = list(map(int, clean_lines[i]))
    # print("Start:")
    # print(energy)

    n_steps = 300
    flash_counter = 0
    for step in range(1, n_steps + 1):
        energy += 1
        flash_check = np.zeros_like(energy)
        check_size = 0
        while True:
            for row in range(energy.shape[0]):
                for col in range(energy.shape[1]):
                    elem = energy[row, col]
                    if elem > 9:
                        flash(energy, row, col, flash_check)
                        flash_check[row, col] = 1

            # check if size of flash check has not changed
            tmp_check_size = np.count_nonzero(flash_check)
            if tmp_check_size > check_size:
                check_size = tmp_check_size
            else:
                break
        if check_size == 100:
            print("Mega-flash at step {}".format(step))
            break

