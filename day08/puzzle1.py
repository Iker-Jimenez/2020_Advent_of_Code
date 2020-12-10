
instructions = []
acc = 0
# First load the instructions into a in memory data structure
with open('instructions.txt', 'r') as instructions_file:
    for instruction in instructions_file:
        operation, argument = instruction.strip().split(' ')
        instructions.append((operation, argument))

processed = set()

instruction_pointer = 0
while instruction_pointer not in processed:
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

print("Accumulator value is %d" % acc)
