def part1(ranges, ids):
    count = 0
    for id in ids:
        for r in ranges:
            if r[0] <= int(id) <= r[1]:
                count += 1
                break
    return count


def part2(ranges):
    """
    ranges: list of (start, end) párok, zárt intervallumok [start, end]
    Visszaadja az összes egyedi lefedett elem számát kibontás nélkül.
    """
    if not ranges:
        return 0

    # 1) Rendezés kezdőpont alapján (és végpont alapján stabilan)
    ranges_sorted = sorted(ranges, key=lambda r: (r[0], r[1]))

    merged = []
    cur_start, cur_end = ranges_sorted[0]

    for s, e in ranges_sorted[1:]:
        # Ha átfed vagy közvetlenül érinti (pl. [1,3] és [4,6] zárt esetben összeér)
        if s <= cur_end + 1:
            # összevonás: kiterjesztjük a végét
            cur_end = max(cur_end, e)
        else:
            # lezárjuk az aktuálisat és új intervallumot kezdünk
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e

    # az utolsó intervallum hozzáadása
    merged.append((cur_start, cur_end))

    # 3) Összegzés (zárt intervallum => +1)
    total = sum(e - s + 1 for s, e in merged)
    return total


if __name__ == "__main__":
    ranges = []
    ids = []
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        i = 0
        index = 0
        for line in lines:
            if line.strip() == "":
                index = i

            i += 1

    ranges = [
        (int(line.split("-")[0]), int(line.split("-")[1])) for line in lines[0:index]
    ]
    ids = lines[index + 1 :]
    # print("Ranges:", ranges)
    # print("IDs:", ids)
    part1_result = part1(ranges, ids)
    print("Part 1 Result:", part1_result)
    part2_result = part2(ranges)
    print("Part 2 Result:", part2_result)
