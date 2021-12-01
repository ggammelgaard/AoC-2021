import os


def convert_to_three(list):
    out_list = []
    for i in range(0, len(clean_lines) - 2):
        out_list.append(sum(list[i:i + 3]))
    return out_list


if __name__ == "__main__":
    counter = 0

    with open(r"input.txt") as f:
        lines = f.readlines()
        clean_lines = [int(s.rstrip('\n')) for s in lines]

        three_list = convert_to_three(clean_lines)

        for i in range(1, len(three_list)):
            if three_list[i] > three_list[i - 1]:
                counter += 1

        print(counter)
