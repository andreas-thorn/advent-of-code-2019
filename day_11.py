from collections import defaultdict
import operator

data = [3,8,1005,8,335,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,51,1006,0,82,1006,0,56,1,1107,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,83,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,104,1006,0,58,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,129,1006,0,54,1006,0,50,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,161,2,101,14,10,1006,0,43,1006,0,77,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,193,2,101,12,10,2,109,18,10,1,1009,13,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,226,1,1103,1,10,1,1007,16,10,1,3,4,10,1006,0,88,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,263,1006,0,50,2,1108,17,10,1006,0,36,1,9,8,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,300,1006,0,22,2,106,2,10,2,1001,19,10,1,3,1,10,101,1,9,9,1007,9,925,10,1005,10,15,99,109,657,104,0,104,1,21101,0,937268454156,1,21102,1,352,0,1106,0,456,21101,0,666538713748,1,21102,363,1,0,1105,1,456,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3316845608,0,1,21102,1,410,0,1105,1,456,21101,0,209475103911,1,21101,421,0,0,1106,0,456,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,984353603944,1,21101,444,0,0,1105,1,456,21102,1,988220752232,1,21102,1,455,0,1106,0,456,99,109,2,22101,0,-1,1,21102,40,1,2,21101,487,0,3,21101,0,477,0,1106,0,520,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,482,483,498,4,0,1001,482,1,482,108,4,482,10,1006,10,514,1102,0,1,482,109,-2,2105,1,0,0,109,4,2101,0,-1,519,1207,-3,0,10,1006,10,537,21101,0,0,-3,22101,0,-3,1,22101,0,-2,2,21102,1,1,3,21101,556,0,0,1106,0,561,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,584,2207,-4,-2,10,1006,10,584,21201,-4,0,-4,1106,0,652,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,603,0,1105,1,561,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,622,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,644,21201,-1,0,1,21101,644,0,0,105,1,519,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]
# Left rotation at index 0 and right rotation at index 1
rotations = {"UP": ("LEFT", "RIGHT"), "RIGHT": ("UP", "DOWN"), "DOWN": ("RIGHT", "LEFT"), "LEFT": ("DOWN", "UP")}

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "UP"

    def rotate(self, change):
        self.direction = rotations[self.direction][change]

    def move_forward(self):
        if self.direction == "UP":
            self.y -= 1
        elif self.direction == "RIGHT":
            self.x += 1
        elif self.direction == "DOWN":
            self.y += 1
        elif self.direction == "LEFT":
            self.x -= 1


class Computer:
    def __init__(self):
        self.program = list(data)
        self.index = 0
        self.relative_base = 0
        self.input_index = 0
        self.input_values = []
        self.set_phase = True

    def run(self, input_value=None):
        while self.index < len(self.program):
            instructions = str(self.program[self.index]).rjust(5, '0')
            op_code = int(instructions[-2:])

            if op_code == 99:
                return None

            parameter_mode_3, parameter_mode_2, parameter_mode_1 = map(int, instructions[-5: -2])

            def get_operand_index(mode, operand_idx):
                if mode == 0:  # position mode
                    return self.program[self.index + operand_idx]
                elif mode == 1:  # immediate mode
                    return self.index + operand_idx
                elif mode == 2:  # relative mode
                    return self.program[self.index + operand_idx] + self.relative_base

            operand_1 = get_operand_index(parameter_mode_1, 1)
            operand_2 = get_operand_index(parameter_mode_2, 2) if op_code not in [3, 4, 9] else -1
            operand_3 = get_operand_index(parameter_mode_3, 3) if op_code in [1, 2, 7, 8] else -1

            if any(operand_index > len(self.program) for operand_index in [operand_1, operand_2, operand_3]):
                self.program += [0] * (max([operand_1, operand_2, operand_3]) + 1)  # Extend program with zeros

            if op_code == 1:
                self.program[operand_3] = self.program[operand_1] + self.program[operand_2]
                self.index += 4
            elif op_code == 2:
                self.program[operand_3] = self.program[operand_1] * self.program[operand_2]
                self.index += 4
            elif op_code == 3:
                self.program[operand_1] = input_value
                self.index += 2
            elif op_code == 4:
                # print(self.program[operand_1])
                self.index += 2
                return self.program[operand_1]
            elif op_code == 5:
                self.index = self.program[operand_2] if self.program[operand_1] != 0 else self.index + 3
            elif op_code == 6:
                self.index = self.program[operand_2] if self.program[operand_1] == 0 else self.index + 3
            elif op_code == 7:
                self.program[operand_3] = 1 if self.program[operand_1] < self.program[operand_2] else 0
                self.index += 4
            elif op_code == 8:
                self.program[operand_3] = 1 if self.program[operand_1] == self.program[operand_2] else 0
                self.index += 4
            elif op_code == 9:
                self.relative_base += self.program[operand_1]
                self.index += 2


def paint(start_color=0):
    computer = Computer()
    robot = Robot()
    hull = defaultdict(int)
    computer_input = start_color

    while True:
        # Run computer twice, one for paint_color output and one for direction output
        paint_color, robot_direction = computer.run(computer_input), computer.run()
        if paint_color is None or robot_direction is None:
            break

        hull[robot.x, robot.y] = paint_color  # Paint given color on current position
        robot.rotate(robot_direction)  # Rotate to next direction
        robot.move_forward()  # Move forward one step in the new direction
        computer_input = hull.get((robot.x, robot.y), 0)  # Read the color of the new panel

    return hull


if __name__ == '__main__':
    # Part 1
    print(f"Part 1: {len(paint().keys())}")

    # Part 2
    spacecraft_hull = paint(start_color=1)
    x_max = max(spacecraft_hull.keys(), key=(operator.itemgetter(0)))[0]
    x_min = min(spacecraft_hull.keys(), key=(operator.itemgetter(0)))[0]
    y_max = max(spacecraft_hull.keys(), key=(operator.itemgetter(1)))[1]
    y_min = min(spacecraft_hull.keys(), key=(operator.itemgetter(1)))[1]
    grid = [" " * (x_max - x_min) for i in range(y_min, y_max + 1)]

    for coord, color in spacecraft_hull.items():
        if color == 1:
            x, y = coord
            row = grid[y]
            new_row = row[:x] + "#" + row[x + 1:]
            grid[y] = new_row

    print("Part 2:")
    for row in grid:
        print(row)
