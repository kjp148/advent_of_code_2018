with open("files/day1input", "r") as file:
    instructions = [int(instruction.strip()) for instruction in file]

# Part 1
frequency = 0

for cmd in instructions:
    frequency += cmd

print("< Day 1 Part 1 >")
print("Frequency: " + str(frequency) + "\n")

# Part 2
frequency = 0
viewed = set()

while True:
    for cmd in instructions:
        frequency += cmd
        if frequency in viewed:
            print("< Day 1 Part 2 >")
            print("Repeated Frequency: " + str(frequency) + "\n")
            exit()

        else:    
            viewed.add(frequency)