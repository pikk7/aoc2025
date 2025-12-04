def check(x, y):
    counter = 0
    if lines[x][y] == ".":
        return False

    if x > 0:
        if lines[x - 1][y] == "@":
            counter += 1
        if y < len(lines[x]) - 1:
            if lines[x - 1][y + 1] == "@":
                counter += 1

        if y > 0:
            if lines[x - 1][y - 1] == "@":
                counter += 1
    if y < len(lines[x]) - 1:
        if lines[x][y + 1] == "@":
            counter += 1

    if y > 0:
        if lines[x][y - 1] == "@":
            counter += 1

    if x < len(lines) - 1:
        if y < len(lines[x]) - 1:
            if lines[x + 1][y + 1] == "@":
                counter += 1

        if y > 0:
            if lines[x + 1][y - 1] == "@":
                counter += 1
        if lines[x + 1][y] == "@":
            counter += 1

    # print(x, y, counter)
    if counter < 4:
        return True

    return False


if __name__ == "__main__":
    # Olvasás a fájlból (minden sor: Rn vagy Ln)
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    cnt_sum = 0
    moved = []
    new_lines = []
    round_n = 1
    cnt = 1
    while cnt > 0:
        print("Round:", round_n)
        cnt = 0
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                if check(x, y):
                    cnt += 1
                    moved.append((x, y))
        new_lines = [list(row) for row in lines]
        for x, y in moved:
            new_lines[x][y] = "."
        lines = ["".join(row) for row in new_lines]
        moved = []
        round_n += 1
        cnt_sum += cnt

    print(cnt_sum)
