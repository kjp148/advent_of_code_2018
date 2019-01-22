# Parse all instructions
file = open("files/day3input", "r")

class Instruction:

    def __init__ (self, ID, from_left, from_top, size_horiz, size_vert):
        self.ID         = int(ID)
        self.from_left  = int(from_left)
        self.from_top   = int(from_top)
        self.size_horiz = int(size_horiz)
        self.size_vert  = int(size_vert)

    def printAll (self):
        print("ID Number:    " + str(self.ID))
        print("X Coordinate: " + str(self.from_left))
        print("Y Coordinate: " + str(self.from_top))
        print("Width:        " + str(self.size_horiz))
        print("Height:       " + str(self.size_vert))

# Create list of instructions
instr_list = []
for line in file:
    ID          = line[line.find("#") + 1:line.find(" ")]  # After "#"  | until " "
    from_left   = line[line.find("@ ") + 2:line.find(",")] # After "@ " | until ","
    from_top    = line[line.find(",") + 1:line.find(":")]  # After ","  | until ":"
    size_horiz  = line[line.find(": ") + 2:line.find("x")] # After ": " | until "x"
    size_vert   = line[line.find("x") + 1:]                # After "x"  | until end of line
    instr_list.append(Instruction(ID, from_left, from_top, size_horiz, size_vert))

# Part 1
sheet = [[0] * 1000 for i in range(1000)] # Every index [n][n] in sheet represents 1 square inch of fabric

# Add 1 to every square inch in sheet that an instruction covers
for instruction in instr_list:
    horiz_start = instruction.from_left - 1
    horiz_end   = horiz_start + instruction.size_horiz
    vert_start  = instruction.from_top - 1
    vert_end    = vert_start + instruction.size_vert

    for i in range(horiz_start, horiz_end):
        for j in range(vert_start, vert_end):
            sheet[i][j] += 1

# Count square inches with overlap
square_count = 0
for i in range(999):
    for j in range(999):
        if sheet[i][j] > 1:
            square_count += 1

print("< Day 3 Part 1 >")
print("Square Inches Overlapping: " + str(square_count) + "\n")

# Part 2

# Search each claim for no overlap
for instruction in instr_list:
    horiz_start = instruction.from_left - 1
    horiz_end   = horiz_start + instruction.size_horiz
    vert_start  = instruction.from_top - 1
    vert_end    = vert_start + instruction.size_vert
    bad_sheet   = False

    for i in range(horiz_start, horiz_end):
        for j in range(vert_start, vert_end):
            if sheet[i][j] > 1:
                bad_sheet = True

    if bad_sheet is False:
        good_claim = instruction.ID

print("< Day 3 Part 2 >")
print("Non-Overlapping Claim ID: " + str(good_claim) + "\n")