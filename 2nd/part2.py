if __name__ == "__main__":
    # read input
    # f = open(r"example.txt")
    f = open(r"input.txt")
    lines = f.readlines()
    clean_lines = [s.rstrip('\n') for s in lines]

    # prep
    horz = 0
    vert = 0
    aim = 0

    # loop through
    for line in clean_lines:
        my_split = line.split()
        direction = my_split[0]
        X = int(my_split[1])

        # logic
        if direction == "forward":
            horz += X
            vert += aim*X
        elif direction == "down":
            aim += X
        elif direction == "up":
            aim -= X

    # result
    print("horz", horz)
    print("vert", horz)
    print("horz*vert", horz*vert)