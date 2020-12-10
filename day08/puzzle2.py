
instructions = []

# First load the instructions into a in memory data structure
with open('instructions.txt', 'r') as instructions_file:
    for instruction in instructions_file:
        operation, argument = instruction.strip().split(' ')
        instructions.append((operation, argument))


def run_simulation(instructions):
    acc = 0
    processed = set()

    instruction_pointer = 0
    while instruction_pointer not in processed and instruction_pointer != len(instructions):
        processed.add(instruction_pointer)
        operation, argument = instructions[instruction_pointer]

        if operation == "nop":
            instruction_pointer += 1
        elif operation == "acc":
            if argument[0] == "+":
                acc += int(argument[1:])
            else:
                acc -= int(argument[1:])
            instruction_pointer += 1
        elif operation == "jmp":
            if argument[0] == "+":
                instruction_pointer += int(argument[1:])
            else:
                instruction_pointer -= int(argument[1:])

    print("Instruction pointer finished at %d " % instruction_pointer)
    print("Accumulator value is %d" % acc)

    if instruction_pointer == len(instructions):
        return True
    else:
        return False


for i in range(0, len(instructions)):
    print("Loop %d, instruction being modified is %s" % (i, instructions[i]))
    if instructions[i][0] != "acc":
        modified_instructions = instructions.copy()
        (operation, argument) = modified_instructions[i]
        if operation == "nop":
            modified_instructions[i] = ("jmp", argument)
        else:
            modified_instructions[i] = ("nop", argument)
        if run_simulation(modified_instructions):
            break
