def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]

    # print(clean_lines)

    code_length = len(clean_lines[0])
    array_length = len(clean_lines)

    counter_list = [0] * code_length
    for i in range(code_length):
        for number in clean_lines:
            counter_list[i] += int(number[i])

    # print(counter_list)

    diff_list = [x - array_length / 2 for x in counter_list]
    # print(diff_list)

    gamma_list = [x > 0 for x in diff_list]
    epsilon_list = [x < 0 for x in diff_list]

    gamma = binatodeci(gamma_list)
    epsilon = binatodeci(epsilon_list)

    print("gamme", gamma)
    print("epsilon", epsilon)
    print("gamma*epsilon", gamma*epsilon)
