from Computer import Computer
import time

input_data = [109,424,203,1,21101,11,0,0,1105,1,282,21101,18,0,0,1105,1,259,2101,0,1,221,203,1,21101,31,0,0,1106,0,282,21102,1,38,0,1106,0,259,21002,23,1,2,22102,1,1,3,21101,0,1,1,21101,0,57,0,1105,1,303,1202,1,1,222,21002,221,1,3,20102,1,221,2,21102,259,1,1,21101,0,80,0,1105,1,225,21101,104,0,2,21101,0,91,0,1106,0,303,2101,0,1,223,20102,1,222,4,21101,0,259,3,21102,1,225,2,21102,1,225,1,21102,1,118,0,1106,0,225,20102,1,222,3,21101,67,0,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,148,1,0,1105,1,259,1202,1,1,223,20102,1,221,4,21001,222,0,3,21101,0,18,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,109,20207,1,223,2,21001,23,0,1,21101,-1,0,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22101,0,-3,1,22102,1,-2,2,21202,-1,1,3,21101,250,0,0,1106,0,225,21202,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21201,-2,0,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21102,343,1,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21101,384,0,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2106,0,0]

def part_one():
    start = time.time()
    result = dict()

    ones_seen, ones_done = False, False
    x, y, first_x = 0, 0, 0
    while y < 50:
        if ones_done:
            x = first_x
            y += 1
            ones_done, ones_seen = False, False
            continue

        computer = Computer(input_data, None)

        output = computer.run([x, y])

        if output == 1 and not ones_seen:
            first_x = x
            ones_seen = True

        if output == 0 and ones_seen:
            ones_done = True
            x += 1
            continue

        if output is None:
            continue

        result[(x, y)] = output
        if x < 50:
            x += 1
        else:
            x = first_x
            y += 1

    end = time.time()
    print(f"Part 1: {(sum(result.values()))}. Elapsed time: {end-start}s")


def part_two():
    start = time.time()
    y_min, y_max = 100, 2000
    best_solution = 999999999999
    while y_min < y_max:
        y_test = (y_max + y_min)//2
        if y_test in [y_min, y_max]:
            break

        ones_seen, does_work = False, False
        x = 0
        while True:
            computer = Computer(input_data, None)
            output = computer.run([x, y_test])

            if output == 0 and ones_seen:
                break

            if output == 1:
                if not ones_seen:
                    ones_seen = True
                if does_square_fit(x, y_test):
                    y_max = y_test  # This y work
                    does_work = True
                    if (x*10000 + y_test) < best_solution:
                        best_solution = (x*10000 + y_test)
                    break

            if output is None:
                x += 1
                continue
            x += 1
        if not does_work:
            y_min = y_test

    end = time.time()
    print(f"Part 2: {best_solution}. Elapsed time: {end - start}s")
    return best_solution

def does_square_fit(x, y):
    for x_1, y_1 in [(99, 0), (0, 99), (99, 99)]:
        computer = Computer(input_data, None)
        output = computer.run([x + x_1, y + y_1])
        if output == 0:
            return False

    return True


if __name__ == '__main__':
    part_one()
    part_two()
