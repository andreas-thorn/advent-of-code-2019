def has_adjacent(code):
    previous_digit = None
    for digit in code:
        if previous_digit and digit == previous_digit:
            return True
        previous_digit = digit

    return False


def has_double_digits(code):
    for digit in range(0, 10):
        if code.count(str(digit)) == 2:
            return True

    return False


def is_increasing(code):
    return list(code) == sorted(code)


possible_codes_part_1, possible_codes_part_2 = [], []

for i in range(146810, 612564 + 1):
    i = str(i)
    if is_increasing(i):
        if has_adjacent(i):
            possible_codes_part_1.append(i)
            if has_double_digits(i):
                possible_codes_part_2.append(i)

print("Part 1: %s" % len(possible_codes_part_1))
print("Part 2: %s" % len(possible_codes_part_2))
