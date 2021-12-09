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

    # print(hmap)

    # find seed points
    seeds = list()
    for x in range(1, hmap.shape[0] - 1):
        for y in range(1, hmap.shape[1] - 1):
            if low_point(hmap, x, y):
                seeds.append((x, y))

    # grow each seed until it does not change between iterations
    basins = np.zeros_like(hmap)
    size_check = 0
    for i in range(1, len(seeds) + 1):
        sx = seeds[i - 1][0]
        sy = seeds[i - 1][1]
        basins[sx, sy] = i

        size_check = 0
        while True:
            idx_list = np.argwhere(basins == i)  # for all values equal to i
            for [ix, iy] in idx_list:
                icenter = hmap[ix, iy]

                # expand to neighbours
                if icenter < hmap[ix + 1, iy] < 9:
                    basins[ix + 1, iy] = i
                if icenter < hmap[ix - 1, iy] < 9:
                    basins[ix - 1, iy] = i
                if icenter < hmap[ix, iy + 1] < 9:
                    basins[ix, iy + 1] = i
                if icenter < hmap[ix, iy - 1] < 9:
                    basins[ix, iy - 1] = i

            # calculate size
            tmp_size = np.count_nonzero(basins == i)

            # print(tmp_size)
            if size_check == tmp_size:
                break
            else:
                size_check = tmp_size

    # print(basins)
    b, count = np.unique(basins, return_counts=True)
    count_sorted = np.argsort(-count)

    t1 = count[count_sorted[1]]
    t2 = count[count_sorted[2]]
    t3 = count[count_sorted[3]]
    print("Top 3: {}, {}, {}, sum = {}".format(t1, t2, t3, t1 * t2 * t3))
