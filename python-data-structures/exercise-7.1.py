# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Use the file name mbox-short.txt as the file name

confidences = []
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find('0.')
    val = float(line[pos-1:])
    confidences.append(val)
    print(line.rstrip(), val)

print(confidences)
total = 0
for c in confidences:
    total += c

if len(confidences) != 0:
    average = total / len(confidences)
    print('Average spam confidence: ', average, avg(confidences))
