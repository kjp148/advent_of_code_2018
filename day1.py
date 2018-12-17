with open("files/day1input", "r") as file:
    instructions = [int(instruction.strip()) for instruction in file]

# Part 1
frequency = 0

for cmd in instructions:
    frequency += cmd

print("Part 1: " + str(frequency))

# Part 2
frequency = 0
viewed = set()

while True:
    for cmd in instructions:
        frequency += cmd
        if frequency in viewed:
            print("Part 2: " + str(frequency))
            exit()

        else:    
            viewed.add(frequency)