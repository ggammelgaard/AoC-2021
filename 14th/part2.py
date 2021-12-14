import pandas as pd


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

    template_str = clean_lines[0]

    # make conversion dict
    cdict = dict()
    for j in range(2, len(clean_lines)):
        line = clean_lines[j]
        line_split = (line.split(' -> '))
        cdict[line_split[0]] = line_split[1]

    # perform conversions
    n_steps = 40
    for step in range(n_steps):
        template_new = ""

        # fill out pairs
        for k in range(len(template_str)):
            pair = template_str[k:k+2]
            if pair in cdict:
                template_new = template_new + pair[0] + cdict[pair]
            else:
                template_new = template_new + pair[0]
            # print(new_template)

        # start over
        template_str = template_new
        # print(template_str)

        print(step)

    # count score
    value_counting = pd.Series(list(template_str)).value_counts()
    print(value_counting)
    print("Score: Largest val={}, smallest val={}, diff={}".format(value_counting[0], value_counting[-1],
                                                                   value_counting[0] - value_counting[-1]))
