import numpy as np


def low_point(hmap, x, y):
    center = hmap[x, y]

    if center < hmap[x + 1, y] and \
            center < hmap[x - 1, y] and \
            center < hmap[x, y + 1] and \
            center < hmap[x, y - 1]:
        return True
    else:
        return False


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    hmap_input = np.array([[int(s) for s in list(x)] for x in clean_lines])
    hmap = np.pad(hmap_input, 1, 'constant', constant_values=9)  # add an edge to the matrix

    summed_risk = 0
    for x in range(1, hmap.shape[0] - 1):
        for y in range(1, hmap.shape[1] - 1):
            if low_point(hmap, x, y):
                # print("Low point found at x,y: {},{}".format(x, y))
                summed_risk += 1 + hmap[x, y]

    print("Summed risk is: {}".format(summed_risk))
