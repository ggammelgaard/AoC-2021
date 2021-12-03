def most_significant(code_list, index):
    array_length = len(code_list)

    counter = 0
    for number in code_list:
        counter += int(number[index])

    comparison = counter - array_length / 2
    if comparison > 0:
        return 1
    elif comparison == 0:
        return 1
    else:
        return 0


def least_significant(code_list, index):
    opposite = most_significant(code_list, index)
    if opposite == 1:
        return 0
    else:
        return 1


def filter_out(code_list, index, filter_val):
    out_list = []
    for number in code_list:
        if int(number[index]) == filter_val:
            out_list.append(number)

    return out_list


def binatodeci(binary):
    return sum(val * (2 ** idx) for idx, val in enumerate(reversed(binary)))


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]

    print(clean_lines)

    code_length = len(clean_lines[0])

    oxygen_list = clean_lines.copy()
    for i in range(code_length):
        filter_val = most_significant(oxygen_list, i)
        # new list
        filter_list = filter_out(oxygen_list, i, filter_val)
        oxygen_list = filter_list  # update tmp list
        if len(oxygen_list) == 1:
            break

    co2_list = clean_lines.copy()
    for i in range(code_length):
        filter_val = least_significant(co2_list, i)
        # new list
        filter_list = filter_out(co2_list, i, filter_val)
        co2_list = filter_list  # update tmp list
        if len(co2_list) == 1:
            break

    pass
    print(oxygen_list[0])
    print(co2_list[0])

    oxygen = int(oxygen_list[0], 2)
    co2 = int(co2_list[0], 2)

    print("oxygen", oxygen)
    print("co2", co2)
    print("oxygen*co2", oxygen * co2)
