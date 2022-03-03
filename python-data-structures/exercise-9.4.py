# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of
# mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who
# sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the
# number of times they appear in the file. After the
# dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most
# prolific committer.

fh = open('mbox-short.txt')
counts = dict()
bigEmail = None
bigCount = 0
for line in fh:
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    pieces = line.split()
    email = pieces[1]
    counts[email] = counts.get(email, 0) + 1
    if counts[email] > bigCount:
        bigCount = counts[email]
        bigEmail = email
print(bigEmail, bigCount)
