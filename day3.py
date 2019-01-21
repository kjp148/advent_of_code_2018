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
        print("Width:        " + str(self.size_vert))
        print("Height:       " + str(self.size_horiz))

instr_array = []
for line in file:
    ID          = line[line.find("#") + 1:line.find(" ")]  # After "#"  | until " "
    from_left   = line[line.find("@ ") + 2:line.find(",")] # After "@ " | until ","
    from_top    = line[line.find(",") + 1:line.find(":")]  # After ","  | until ":"
    size_horiz  = line[line.find(": ") + 2:line.find("x")] # After ": " | until "x"
    size_vert   = line[line.find("x") + 1:line.find("\n")] # After "x"  | until "\n"
    instr_array.append(Instruction(ID, from_left, from_top, size_horiz, size_vert))

# Part 1

