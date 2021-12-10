CHAR_MAP = ['()', '[]', '{}', '<>']
ipar = 0
ifir = 1
itub = 2
ikro = 3


def check_inconsistensies(counter, querying_index, char, line, i):
    for j in range(4):
        if j == querying_index:
            continue

        if counter[j] != 0:
            print("ERROR! Char '{}' interrupts".format(char, CHAR_MAP[j], i))
            print(line[:i + 1])
            return False
    return True


def find_scope(_line, end_idx, querying_index):
    start_idx = 0
    counter = 0
    for j in range(end_idx, 0, -1):
        if _line[j] == CHAR_MAP[querying_index][0]:
            counter += 1
        elif _line[j] == CHAR_MAP[querying_index][1]:
            counter -= 1

        if counter == 0:
            start_idx = j
            break

    return _line[start_idx:end_idx + 1]


def check_line(line):
    counter = [0, 0, 0, 0]

    for i in range(len(line)):
        char = line[i]

        if char == CHAR_MAP[ipar][0]:
            counter[ipar] += 1
        elif char == CHAR_MAP[ipar][1]:
            counter[ipar] -= 1
            if not check_inconsistensies(counter, ipar, char, line, i):
                return False

        elif char == CHAR_MAP[ifir][0]:
            counter[ifir] += 1
        elif char == CHAR_MAP[ifir][1]:
            counter[ifir] -= 1
            if not check_inconsistensies(counter, ifir, char, line, i):
                return False

        elif char == CHAR_MAP[itub][0]:
            counter[itub] += 1
        elif char == CHAR_MAP[itub][1]:
            counter[itub] -= 1
            if not check_inconsistensies(counter, itub, char, line, i):
                return False

        elif char == CHAR_MAP[ikro][0]:
            counter[ikro] += 1
        elif char == CHAR_MAP[ikro][1]:
            counter[ikro] -= 1
            if not check_inconsistensies(counter, ikro, char, line, i):
                return False
    return True


if __name__ == "__main__":
    # read input
    f = open(r"example.txt")
    # f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    print(clean_lines)

    for line in clean_lines:
        for i in range(len(line)):
            char = line[i]

            if char == CHAR_MAP[ipar][1]:
                scope = find_scope(line, i, ipar)
                print(scope)
                if not check_line(scope):
                    break

            if char == CHAR_MAP[ifir][1]:
                scope = find_scope(line, i, ifir)
                print(scope)
                if not check_line(scope):
                    break

            if char == CHAR_MAP[itub][1]:
                scope = find_scope(line, i, itub)
                print(scope)
                if not check_line(scope):
                    break

            if char == CHAR_MAP[ikro][1]:
                scope = find_scope(line, i, ikro)
                print(scope)
                if not check_line(scope):
                    break
