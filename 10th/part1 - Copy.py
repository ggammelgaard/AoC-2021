CHAR_MAP = ['()', '[]', '{}', '<>']
ipar = 0
ifir = 1
itub = 2
ikro = 3



if __name__ == "__main__":
    # read input
    f = open(r"example.txt")
    # f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    print(clean_lines)

    scope_list = []
    for line in clean_lines:
        for i in range(len(line)):
            char = line[i]

            if char == CHAR_MAP[ipar][0]:
                scope_list.append('(')
            elif char == CHAR_MAP[ipar][1]:
                if scope_list[-1] == CHAR_MAP[ipar][0]:
                    scope_list.__delitem__(-1)
                else:
                    print("ERROR! Char '{}' interrupts".format(char, CHAR_MAP[j], i))


                # scope_list.append('(')

        #
        #     elif char == CHAR_MAP[ifir][0]:
        #         counter[ifir] += 1
        #     elif char == CHAR_MAP[ifir][1]:
        #         counter[ifir] -= 1
        #         if not check_inconsistensies(counter, ifir, char, line, i):
        #             return False
        #
        #     elif char == CHAR_MAP[itub][0]:
        #         counter[itub] += 1
        #     elif char == CHAR_MAP[itub][1]:
        #         counter[itub] -= 1
        #         if not check_inconsistensies(counter, itub, char, line, i):
        #             return False
        #
        #     elif char == CHAR_MAP[ikro][0]:
        #         counter[ikro] += 1
        #     elif char == CHAR_MAP[ikro][1]:
        #         counter[ikro] -= 1
        #         if not check_inconsistensies(counter, ikro, char, line, i):
        #             return False
        # return True
