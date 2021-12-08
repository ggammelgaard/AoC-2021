import numpy as np

if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]
    # print(clean_lines)

    digits = [x.split() for x in clean_lines]
    patterns = [x[0:10] for x in digits]
    output = [x[-4:] for x in digits]
    output_len = np.array([[len(s) for s in x] for x in output])
    assert len(patterns) == len(output) == len(output_len)

    val_1 = np.count_nonzero(output_len == 2)
    val_4 = np.count_nonzero(output_len == 4)
    val_7 = np.count_nonzero(output_len == 3)
    val_8 = np.count_nonzero(output_len == 7)

    appearances = val_1 + val_4 + val_7 + val_8
    print(appearances)
