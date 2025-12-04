def get_joltes(line):

    realnumbers = [int(d) for d in line]

    i, maximum, maximum2,  = 0, 0, 0,
    indexloc, = 0,
    for numb in realnumbers:

        if numb > maximum and i != len(realnumbers) - 1:
            maximum = numb
            indexloc = i
        i += 1

    for numb in realnumbers[indexloc + 1 :]:

        if numb > maximum2:
            maximum2 = numb



    return int(f"{maximum}{maximum2}")


if __name__ == "__main__":
    # Olvasás a fájlból (minden sor: Rn vagy Ln)
    with open("test.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    print(lines)

    sum = 0
    for line in lines:
        joltes = get_joltes(line)
        sum = sum + joltes
        print(f"A(z) {line} vonatkozású legnagyobb joltés: {joltes}")

    print(f"A joltések összege: {sum}")
