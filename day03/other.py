with open("test.txt", "r") as file:
    lines_list = [line.strip() for line in file]

digits = 12
total = 0
for line in lines_list:
    last_position = 0
    line_number = ""

    for digit in range(digits):
        max_digit = "0"

        for position in range(last_position, len(line) - digits + digit + 1):

            if int(line[position]) > int(max_digit):
                max_digit = line[position]
                last_position = position
        last_position += 1

        line_number += max_digit

    total += int(line_number)

print(total)
