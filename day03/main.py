from typing import List, Tuple


def get_joltes_2digits(line):

    realnumbers = [int(d) for d in line]

    (
        i,
        maximum,
        maximum2,
    ) = (
        0,
        0,
        0,
    )
    (indexloc,) = (0,)
    for numb in realnumbers:

        if numb > maximum and i != len(realnumbers) - 1:
            maximum = numb
            indexloc = i
        i += 1

    for numb in realnumbers[indexloc + 1 :]:

        if numb > maximum2:
            maximum2 = numb

    return int(f"{maximum}{maximum2}")


def part1(lines):
    sum = 0
    for line in lines:
        joltes = get_joltes_2digits(line)
        sum = sum + joltes
        print(f"A(z) {line} vonatkozású legnagyobb joltés: {joltes}")

    print(f"A joltések összege: {sum}")


# 2. taks, I used Copilot to help me with this task


def max_subsequence_number(s: str, k: int) -> str:
    """
    Visszaadja a s számsorból kiválasztott, sorrendet megtartó, k hosszú
    legnagyobb lehetséges számot sztringként.
    Példa: s='987654321111111', k=2 -> '98'
    """
    n = len(s)
    if k <= 0:
        return ""
    if k >= n:
        return s  # ha mindent kell, az eredeti a maximum

    result = []
    start = 0
    # t: hányadik számjegyet választjuk (0-index)
    for t in range(k):
        # Az utolsó választható kezdőpozíció, hogy maradjon elég karakter a végére
        end_limit = n - (k - t)
        # Keressük a maximum számjegyet az ablakban [start, end_limit]
        max_digit = "-1"
        max_idx = start
        for i in range(start, end_limit + 1):
            if s[i] > max_digit:
                max_digit = s[i]
                max_idx = i
                # rövidzár: ha '9'-et találtunk, ennél nincs jobb
                if max_digit == "9":
                    break
        result.append(max_digit)
        start = max_idx + 1

    return "".join(result)


def process_sequences(sequences: List[str], k: int) -> List[Tuple[str, str]]:
    """
    Több azonos hosszúságú számsorra lefuttatja az algoritmust.
    Visszaadja az (eredeti, maximum)-párokat.
    """
    return [int(max_subsequence_number(s, k)) for s in sequences]


if __name__ == "__main__":
    # Olvasás a fájlból (minden sor: Rn vagy Ln)
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    part1(lines)
    print(sum(process_sequences(lines, 12)))
