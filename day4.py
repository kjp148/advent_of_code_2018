# Grab input
file = open("files/day4input", "r")

class Log:

    def __init__ (self, date, hour, minute, entry):
        self.date   = date
        self.hour   = hour
        self.minute = minute
        self.entry  = entry

    def printAll (self):
        print("[" + self.date + " " + str(self.hour) +
              ":" + str(self.minute) + "] " + self.entry)

    def fullDate (self):
        full_date = str(self.date) + str(self.hour) + str(self.minute)
        return full_date

class Guard:
    asleep = [0] * 60 # One index for each minute in the midnight hour

    def __init__ (self, ID):
        self.ID = ID

    def printAsleep (self):
        asleep_string = ""
        for minute, amount in enumerate(self.asleep):
            asleep_string += " | " + str(minute) + ": " + str(amount)
        return asleep_string

    def totalMinutes (self):
        minute_total = 0
        for amount in self.asleep:
            minute_total += amount
        return minute_total

# Create list of objects for sorting
log_list = []
for line in file:
    date   = line[1:11]
    hour   = line[12:14]
    minute = line[15:17]
    entry  = line[19:line.find("\n")]
    log_list.append(Log(date, hour, minute, entry))

# Sort chronologically
log_list.sort(key = lambda Log: Log.fullDate())

# Find largest guard number
max_guard_number = 0
for log in log_list:
    if "Guard" in log.entry:
        str_start    = log.entry.find("#") + 1
        str_end      = log.entry.find("begins") - 1
        guard_number = int(log.entry[str_start:str_end])
        if max_guard_number < guard_number:
            max_guard_number = guard_number

# Part 1

# Gather list of each guard's activities (guard # = index)
guard_list = []
for i in range(max_guard_number + 1):
    guard_list.append(Guard(i + 1))

for log in log_list:
    if "Guard" in log.entry:
        str_start    = log.entry.find("#") + 1
        str_end      = log.entry.find("begins") - 1
        guard_number = int(log.entry[str_start:str_end])

    elif "falls" in log.entry:
        start_sleep = int(log.minute)

    elif "wakes" in log.entry:
        end_sleep = int(log.minute)
        for i in range(start_sleep, end_sleep):
            guard_list[guard_number].asleep[i] += 1

# Find guard with most minutes asleep
highest_guard = guard_list[0]
for guard in guard_list:
    if guard.totalMinutes() > highest_guard.totalMinutes():
        highest_guard = guard

# Find minute most asleep
minute_max = highest_guard.asleep[0]
for minute in highest_guard.asleep:
    if minute > minute_max:
        minute_max = minute

print("< Day 4 Part 1 >")
print("Guard Most Asleep:    " + str(highest_guard.ID))
print("Total Minutes Asleep: " + str(highest_guard.totalMinutes()))
print("Minute Most Aleep:    " + str(minute_max))
print("Output:               " + str(highest_guard.ID * minute_max))