

# fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
    line.rstrip()
    pieces = line.split()
    for word in pieces:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
