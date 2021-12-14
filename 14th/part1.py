import pandas as pd


def template_str_to_list(input):
    output = []
    for i in range(len(input) - 1):
        output.append(input[i:i + 2])
    return output


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    template_raw = clean_lines[0]
    template = template_str_to_list(template_raw)

    # make conversion dict
    cdict = dict()
    for j in range(2, len(clean_lines)):
        line = clean_lines[j]
        line_split = (line.split(' -> '))
        cdict[line_split[0]] = line_split[1]

    # perform conversions
    n_steps = 40
    for step in range(n_steps):
        new_template = ""

        # fill out pairs
        for k in range(len(template)):
            pair = template[k]
            if pair in cdict:
                new_template = new_template + pair[0] + cdict[pair]
            else:
                new_template = new_template + pair[0]
            # print(new_template)

        # add last character
        new_template = new_template + template[-1][-1]
        # print(new_template)

        # create new list
        template = template_str_to_list(new_template)

    # count score
    value_counting = pd.Series(list(new_template)).value_counts()
    print(value_counting)
    print("Score: Largest val={}, smallest val={}, diff={}".format(value_counting[0], value_counting[-1],
                                                                   value_counting[0] - value_counting[-1]))
