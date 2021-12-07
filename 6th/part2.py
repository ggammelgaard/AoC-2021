import numpy as np


def min_max(in_list):
    return min(in_list), max(in_list)


def calc_score(crab_positions, pos):
    diffs = np.abs(crab_positions - pos)
    fuel_usage = [np.sum(np.arange(x + 1)) for x in diffs]
    score = sum(fuel_usage)

    return score


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    crab_positions = list(map(int, clean_lines[0].split(',')))
    crab_positions = np.array(crab_positions)
    # print(crab_positions)
    cmin, cmax = min_max(crab_positions)

    best_pos = None
    best_score = cmax * len(crab_positions) ** 2
    for pos in range(cmin, cmax):
        tmp_score = calc_score(crab_positions, pos)
        if tmp_score < best_score:
            best_score = tmp_score
            best_pos = pos

    print("best_pos:", best_pos)
    print("best_score:", best_score)
