import re

# fh = open('regex_sum_42.txt')
fh = open('regex_sum_1479027.txt')
raw_data = fh.read()

values = re.findall('[0-9]+', raw_data)
total = 0
for value in values:
    total += int(value)

print(total)
