CHAR_DICT = {')': '(', ']': '[', '}': '{', '>': '<', }
SCORE_DICT = {')': 3, ']': 57, '}': 1197, '>': 25137, }


def error_msg(_char, idx):
    print("ERROR! Char '{}' interrupts at i={}".format(char, idx))


if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    score = 0
    scope_list = []
    for line in clean_lines:
        for i in range(len(line)):
            char = line[i]

            if char in ['(', '[', '{', '<']:
                scope_list.append(char)

            elif char in [')', ']', '}', '>', ]:
                if scope_list[-1] == CHAR_DICT[char]:
                    scope_list.pop()
                else:
                    # error_msg(char, i)
                    score += SCORE_DICT[char]
                    break

    print("Final score: {}".format(score))
