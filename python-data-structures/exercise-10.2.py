# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the
# 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6


fh = open('mbox-short.txt')
counts = dict()

for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5].split(':')
    hour = time[0]
    counts[hour] = counts.get(hour, 0) + 1

# mySortedList = sorted([(v, k) for k, v in counts.items()], reverse=True)
mySortedList = sorted(counts.items())
for hour in mySortedList:
    print(hour[0], hour[1])
