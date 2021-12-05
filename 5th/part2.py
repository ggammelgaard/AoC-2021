import numpy as np


def min_max(in_list):
    return min(in_list), max(in_list)


def coord_converter(_line):
    output_coords = []
    diff = (_line[2] - _line[0], _line[3] - _line[1])

    if diff[1] == 0:
        _min, _max = min_max((_line[0], _line[0] + diff[0]))
        for i in np.arange(_min, _max + 1):
            output_coords.append([i, _line[1]])
    elif diff[0] == 0:
        _min, _max = min_max((_line[1], _line[1] + diff[1]))
        for i in np.arange(_min, _max + 1):
            output_coords.append([_line[0], i])
    else:
        x_step = diff[0] / abs(diff[0])
        y_step = diff[1] / abs(diff[1])

        for i in range(abs(max(diff)) + 1):
            output_coords.append([int(_line[0] + i * x_step), int(_line[1] + i * y_step)])

    return output_coords


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    # get coordinate pairs
    coordinates = []
    for input in clean_lines:
        line_split = input.replace(' ', ',').split(',')
        coordinates.append([int(line_split[0]), int(line_split[1]), int(line_split[3]), int(line_split[4])])

    # make coordinate system
    np_coords = np.asarray(coordinates)
    # print(np_coords)
    x_max = np_coords[:, [0, 2]].max()
    y_max = np_coords[:, [1, 3]].max()
    ocean_floor = np.zeros([x_max + 1, y_max + 1])

    # fill coordinate system
    for line in np_coords:
        coord_set = coord_converter(line)
        for coord in coord_set:
            ocean_floor[coord[0], coord[1]] += 1

        # print(ocean_floor.T)
        # pass

    # number of overlapping points
    count = np.count_nonzero(ocean_floor > 1)
    print(count)
