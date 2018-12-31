with open("files/day2input", "r") as file:
    box_IDs = [str(box_ID) for box_ID in file]

# Part 1
two_sum   = 0
three_sum = 0

for line in box_IDs:
    seen       = {}
    two_flag   = False
    three_flag = False
    
    for letter in line:
        if letter is not '\n':
            if letter in seen:
                seen[letter] += 1

            else:
                seen[letter] = 1

    for letter in seen:
        if seen[letter] is 2:
            two_flag = True

        elif seen[letter] is 3:
            three_flag = True

    if two_flag is True:
        two_sum += 1

    if three_flag is True:
        three_sum += 1

checksum = two_sum * three_sum

print("< Day 2 Part 1 >")
print("Two Sum:   " + str(two_sum))
print("Three Sum: " + str(three_sum))
print("Checksum:  " + str(checksum) + "\n")

# Part 2
for current_ID in box_IDs:
    for check_ID in box_IDs:
        different = 0

        for i in range(len(current_ID) - 1):
            if current_ID[i] is check_ID[i]:
                different += 0

            else:
                different += 1

        if different is 1:
            current_ID = current_ID.replace('\n', '')
            check_ID   = check_ID.replace('\n', '')

            for i in range(len(current_ID) - 1):
                if current_ID[i] is not check_ID[i]:
                    correct_ID = current_ID[:i] + current_ID[i + 1:]

            print("< Day 2 Part 2 >")
            print("Current ID:   " + current_ID)
            print("Identical ID: " + check_ID)
            print("Correct ID:   " + correct_ID + "\n")
            exit()