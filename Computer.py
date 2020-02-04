
class Computer:
    def __init__(self, input_data, input_function):
        self.program = list(input_data)
        self.index = 0
        self.relative_base = 0
        self.input_index = 0
        self.input_values = []
        self.set_phase = True
        self.input_function = input_function

    def run(self, input_value=""):
        if input_value != "":
            self.input_values.extend(input_value)
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

            if any(operand_index > len(self.program) - 1 for operand_index in [operand_1, operand_2, operand_3]):
                self.program += [0] * (max([operand_1, operand_2, operand_3]) + 1)  # Extend program with zeros

            if op_code == 1:
                self.program[operand_3] = self.program[operand_1] + self.program[operand_2]
                self.index += 4
            elif op_code == 2:
                self.program[operand_3] = self.program[operand_1] * self.program[operand_2]
                self.index += 4
            elif op_code == 3:
                if self.input_values is []:
                    self.program[operand_1] = self.input_function()
                else:
                    self.program[operand_1] = self.input_values.pop(0)
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
