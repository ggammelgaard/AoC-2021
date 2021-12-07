import numpy as np


def min_max(in_list):
    return min(in_list), max(in_list)


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    fish_ages = list(map(int, clean_lines[0].split(',')))
    fish_ages = np.array(fish_ages)

    days = 256

    # fill intial array
    fish_sorted = np.array([0] * 9).astype(np.longlong)
    for fish in fish_ages:
        fish_sorted[fish] += 1

    # simulate
    for day in range(1, days + 1):
        birth_fishes = fish_sorted[0]
        fish_sorted = np.roll(fish_sorted, -1)
        fish_sorted[-1] = birth_fishes
        fish_sorted[6] = fish_sorted[6] + birth_fishes

    print("After {:2} days: Total of {} fish".format(days, np.sum(fish_sorted)))
