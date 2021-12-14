import pandas as pd
import numpy as np


def template_str_to_list(input):
    output = []
    for i in range(len(input) - 1):
        output.append(input[i:i + 2])
    return output


if __name__ == "__main__":
    # read input
    f = open(r"example.txt")
    # f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    template_str = np.array(list(clean_lines[0])).astype('S1')

    # make conversion dict
    cdict = dict()
    for j in range(2, len(clean_lines)):
        line = clean_lines[j]
        line_split = (line.split(' -> '))
        cdict[line_split[0]] = line_split[1]

    # perform conversions
    n_steps = 10
    for step in range(n_steps):
        template_new = np.chararray(template_str.size * 2)

        # fill out pairs
        for k in range(len(template_str)):
            pair = template_str[k:k + 2].tostring().decode("utf-8")
            if str(pair) in cdict:
                template_new[k*2:k*2 + 2] = [pair[0], cdict[pair]]
            else:
                template_new[k*2] = pair[0]
            # print(new_template)

        # start over
        template_str = np.array(list(filter(None, template_new))).astype('S1')
        # print(template_str)

        print(step)

    # count score
    u, count = np.unique(template_str, return_counts=True)
    print(count)
    print("Score: Largest val={}, smallest val={}, diff={}".format(count[0], count[-1],
                                                                   count[0] - count[-1]))
