import numpy as np
import string

if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    digits = [[set(s) for s in x.split()] for x in clean_lines]
    patterns = [[set(s) for s in x[0:10]] for x in digits]
    outputs = [x[-4:] for x in digits]
    assert len(patterns) == len(outputs)

    output_sum = 0
    for i in range(len(outputs)):
        pattern = np.array(patterns[i])
        pattern_len = np.array([len(x) for x in pattern])

        digmap = dict()
        letmap = dict()

        ## find 1, 4, 7 og 8
        digmap[1] = pattern[pattern_len == 2][0]
        digmap[4] = pattern[pattern_len == 4][0]
        digmap[7] = pattern[pattern_len == 3][0]
        digmap[8] = pattern[pattern_len == 7][0]

        ## find a
        letmap['a'] = digmap[1].symmetric_difference(digmap[7])

        ## find 2 - optæl alle uden c og alle uden f. Den hvor der kun er én i er 2
        digit_no_l1_segment = list()
        digit_no_l2_segment = list()
        list_1 = list(digmap[1])
        for digit in pattern:
            if list_1[0] not in digit:
                digit_no_l1_segment.append(digit)
            elif list_1[1] not in digit:
                digit_no_l2_segment.append(digit)
        if len(digit_no_l1_segment) < len(digit_no_l2_segment):
            digmap[2] = digit_no_l1_segment[0]
        else:
            digmap[2] = digit_no_l2_segment[0]
        pass

        ## find c og f
        letmap['f'] = digmap[1] - digmap[2]
        letmap['c'] = digmap[1] - letmap['f']

        ## find 6 - af tal med en len=6, er 6 den eneste uden c
        for digit in pattern[pattern_len == 6]:
            if not letmap['c'] <= digit:
                digmap[6] = digit
                break

        ## find 'b'
        letmap['b'] = digmap[6] - digmap[2] - letmap['f']

        ## find 3 og 5
        for digit in pattern[pattern_len == 5]:
            if digit == digmap[2]:
                continue
            if letmap['c'] <= digit:
                digmap[3] = digit
            else:
                digmap[5] = digit

        ## find 0 og 9
        for digit in pattern[pattern_len == 6]:
            if digit == digmap[6]:
                continue

            if len(digit - digmap[5] - digmap[4]) == 1:
                digmap[0] = digit
            else:
                digmap[9] = digit

        # decode
        output = np.array(outputs[i])
        key_list = list(digmap.keys())
        val_list = list(digmap.values())
        output_int = int("".join([str(key_list[val_list.index(entry)]) for entry in output]))
        # print("i: {}, output_int: {}".format(i, output_int))
        output_sum += output_int

    print(output_sum)
