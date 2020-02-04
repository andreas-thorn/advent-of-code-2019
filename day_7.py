import itertools

data = [3,8,1001,8,10,8,105,1,0,0,21,30,39,64,81,102,183,264,345,426,99999,3,9,1001,9,2,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1002,9,5,9,101,2,9,9,102,3,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]

def run(input_values, input_data=None):
    program = list(input_data) if input_data else list(data)
    index = 0
    length = len(program)
    output = None
    input_index = 0
    while index < length:
        instructions = str(program[index]).rjust(5, '0')
        op_code = int(instructions[-2:])

        if op_code == 99:
            break

        parameter_mode_3, parameter_mode_2, parameter_mode_1 = map(int, instructions[-5: -2])

        operand_1 = program[index + 1] if parameter_mode_1 else program[program[index + 1]]
        if op_code not in [3, 4]:
            operand_2 = program[index + 2] if parameter_mode_2 else program[program[index + 2]]

        if op_code == 1:
            program[program[index + 3]] = operand_1 + operand_2
            index += 4
        elif op_code == 2:
            program[program[index + 3]] = operand_1 * operand_2
            index += 4
        elif op_code == 3:
            program[program[index + 1]] = input_values[input_index]
            input_index += 1
            index += 2
        elif op_code == 4:
            # print operand_1
            output = operand_1
            index += 2
        elif op_code == 5:
            index = operand_2 if operand_1 != 0 else index + 3
        elif op_code == 6:
            index = operand_2 if operand_1 == 0 else index + 3
        elif op_code == 7:
            program[program[index + 3]] = 1 if operand_1 < operand_2 else 0
            index += 4
        elif op_code == 8:
            program[program[index + 3]] = 1 if operand_1 == operand_2 else 0
            index += 4

    return output


# Part 1
thrust_signal = 0
for phase_settings in list(itertools.permutations([0, 1, 2, 3, 4])):
    result = 0
    for phase in phase_settings:
        result = run([phase, result])

    thrust_signal = result if result > thrust_signal else thrust_signal

print("Part 1: %s" % thrust_signal)


class Amplifier:

    def __init__(self, phase):
        self.program = list(data)
        self.index = 0
        self.input_index = 0
        self.input_values = []
        self.phase = phase
        self.set_phase = True

    def execute(self, input_value):
        self.input_values.append(input_value)
        while self.index < len(self.program):
            instructions = str(self.program[self.index]).rjust(5, '0')
            op_code = int(instructions[-2:])

            if op_code == 99:
                return None

            parameter_mode_3, parameter_mode_2, parameter_mode_1 = map(int, instructions[-5: -2])

            operand_1 = self.program[self.index + 1] if parameter_mode_1 else self.program[self.program[self.index + 1]]
            if op_code not in [3, 4]:
                operand_2 = self.program[self.index + 2] if parameter_mode_2 else self.program[self.program[self.index + 2]]

            if op_code == 1:
                self.program[self.program[self.index + 3]] = operand_1 + operand_2
                self.index += 4
            elif op_code == 2:
                self.program[self.program[self.index + 3]] = operand_1 * operand_2
                self.index += 4
            elif op_code == 3:
                if self.set_phase:
                    self.program[self.program[self.index + 1]] = self.phase
                    self.set_phase = False
                else:
                    self.program[self.program[self.index + 1]] = self.input_values[self.input_index]
                    self.input_index += 1
                self.index += 2
            elif op_code == 4:
                self.index += 2
                return operand_1
            elif op_code == 5:
                self.index = operand_2 if operand_1 != 0 else self.index + 3
            elif op_code == 6:
                self.index = operand_2 if operand_1 == 0 else self.index + 3
            elif op_code == 7:
                self.program[self.program[self.index + 3]] = 1 if operand_1 < operand_2 else 0
                self.index += 4
            elif op_code == 8:
                self.program[self.program[self.index + 3]] = 1 if operand_1 == operand_2 else 0
                self.index += 4


# Part 2
best_result = 0

for phase_setting in list(itertools.permutations([5, 6, 7, 8, 9])):
    amplifiers = [Amplifier(x) for x in phase_setting]
    index, result = 0, 0

    while True:
        amplifier = amplifiers[index]
        result = amplifier.execute(result)

        if result is None:
            break

        if index == 4 and result > best_result:
            best_result = result

        index = (index + 1) % 5

print("Part 2: %s" % best_result)
