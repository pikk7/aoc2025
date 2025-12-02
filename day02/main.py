def first_check(id_number):
    """
    Check if the ID is based on two repeted sequential digits.
    """
    id_number = str(id_number)
    return id_number[: len(id_number) // 2] == id_number[len(id_number) // 2 :]


def second_check(id_number):
    """
    Check if the ID is based some sequence of digits repeated at least twice.
    """
    id_number = str(id_number)

    for size in range(1, len(id_number) // 2 + 1):
        if id_number[:size] * (len(id_number) // size) == id_number:
            return True
    return False


if __name__ == "__main__":
    # Olvasás a fájlból (minden sor: Rn vagy Ln)
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.read().split(",")

    list_of_all_ids = []

    for line in lines:
        start_str, end_str = line.split("-")
        start = int(start_str)
        end = int(end_str)
        ids_in_range = list(range(start, end + 1))
        list_of_all_ids.extend(ids_in_range)

    # print(list_of_all_ids)

    invalid_ids = [element for element in list_of_all_ids if first_check(element)]
    print(invalid_ids)

    print(sum(invalid_ids))

    invalid_ids_2 = [element for element in list_of_all_ids if second_check(element)]
    print(invalid_ids_2)
    print(sum(invalid_ids_2))
