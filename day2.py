file = open("files/day2input.txt")

# Part 1
two_sum   = 0
three_sum = 0

for line in file:

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

print("Two Sum:   " + str(two_sum))
print("Three Sum: " + str(three_sum))
print("Checksum:  " + str(checksum))

file.close()