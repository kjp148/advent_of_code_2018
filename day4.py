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
guard_str_list = [""] * (max_guard_number + 1)
for log in log_list:
    if "Guard" in log.entry:
        str_start    = log.entry.find("#") + 1
        str_end      = log.entry.find("begins") - 1
        guard_number = int(log.entry[str_start:str_end])

    elif "falls" in log.entry:
        guard_str_list[guard_number] += str(log.hour) + str(log.minute) + "-"

    elif "wakes" in log.entry:
        guard_str_list[guard_number] += str(log.hour) + str(log.minute) + ","

for index, guard in enumerate(guard_str_list):
    print("Guard " + str(index) + ": " + guard)