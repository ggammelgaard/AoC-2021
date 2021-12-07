import numpy as np


def min_max(in_list):
    return min(in_list), max(in_list)


if __name__ == "__main__":
    # read input
    f = open(r"example.txt")
    # f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    fish_ages = list(map(int, clean_lines[0].split(',')))
    fish_ages = np.array(fish_ages)

    days = 80
    for day in range(1, days+1):
        fish_ages -= 1
        birth_fishes = np.where(fish_ages == -1)[0]
        if birth_fishes.size != 0:
            fish_ages[birth_fishes] = 6
            fish_ages = np.append(fish_ages, [8]*birth_fishes.size)
        print("After {:2} days: {}".format(day, fish_ages))

    print("After {:2} days: Total of {} fish".format(days, fish_ages.size))


    # TODO: Lav det om så man har en counter for hver alder en fisk kan have
    # Så skal jeg ikke rode med arrays