data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]


def run(noun, verb):
    program = list(data)
    program[1] = noun
    program[2] = verb
    index = 0
    length = len(program)
    while index < length:
        op_code = program[index]
        # Halt program execution
        if op_code == 99:
            break
        # Addition
        if op_code == 1:
            program[program[index + 3]] = program[program[index + 1]] + program[program[index + 2]]
        # Multiplication
        elif op_code == 2:
            program[program[index + 3]] = program[program[index + 1]] * program[program[index + 2]]

        # Continue to next OP
        index += 4

    return program[0]


print("Part 1: %s" % run(12, 2))

for noun in range(100):
    for verb in range(100):
        result = run(noun, verb)

        if result == 19690720:
            print("Part 2: noun = %s verb = %s. Answer = %s" % (noun, verb, (100 * noun) + verb))
