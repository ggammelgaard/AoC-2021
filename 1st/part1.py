import os

if __name__ == "__main__":
    counter = 0

    with open(r"input.txt") as f:
        lines = f.readlines()
        clean_lines = [int(s.rstrip('\n')) for s in lines]
        print(clean_lines)

        for i in range(1, len(clean_lines)):
            if clean_lines[i] > clean_lines[i - 1]:
                counter += 1

        print(counter)
