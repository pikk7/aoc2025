
def count_password(lines, start_pos=50):
    """
    lines: iterable[str] - minden sor 'R' vagy 'L', utána egész szám (pl. 'R48', 'L68')
    start_pos: int       - induló pozíció (alapértelmezés: 50), 0..99 közé normalizáljuk

    Visszaad:
      (cross_count, land_count, final_pos)
      - cross_count: 0 átlépése menet közben (during rotation)
      - land_count: pont 0-ra érkezés a lépés végén
      - final_pos: végső pozíció [0..99]
    """
    pos = start_pos % 100
    cross_count = 0
    land_count = 0

    for ln in lines:
        ln = ln.strip()
        direction = ln[0]          # 'R' vagy 'L'
        steps = int(ln[1:])        # lépések száma (>=0)

        if direction == 'R':
            # Átlépések jobbra: minden alkalommal, amikor a köztes lépések egyikén a mutató 0-ra kerül
            cross_count += (steps - 1 + pos) // 100

            # Új pozíció
            pos = (pos + steps) % 100

        else:  # direction == 'L'
            if pos == 0:
                # Ha 0-ról indulunk balra, az első köztes 0 csak 100 lépéssel később jönne
                cross_count += (steps - 1) // 100
            else:
                # Ha pos > 0: akkor az első köztes 0 pos lépés múlva jönne
                remaining = steps - 1 - pos
                if remaining >= 0:
                    cross_count += 1 + (remaining // 100)
                # Ha remaining < 0 → a köztes lépésekben nem érjük el a 0-t

            # Új pozíció
            pos = (pos - steps) % 100

        # Landolás (lépés végén pont 0-ra érkezünk)
        if pos == 0:
            land_count += 1

    return cross_count, land_count, pos


# --- Példahasználat: a rövid minta ---
if __name__ == "__main__":
    # Olvasás a fájlból (minden sor: Rn vagy Ln)
    with open("test1.txt", "r", encoding="utf-8") as f:
        test_lines = f.read().splitlines()

    with open("1.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    cross, land, final_pos = count_password(test_lines, start_pos=50)
    print(f"Átlépések: {cross}, Landolások: {land}, Összesen: {cross + land}")

    cross, land, final_pos = count_password(lines, start_pos=50)
    print(f"Átlépések: {cross}, Landolások: {land}, Összesen: {cross + land}")
