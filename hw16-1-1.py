# Author: Tow 2/13/21

with open("alice.txt", "r") as infile:
    counter = {}
    for lines in infile:
        linesplit = lines.split()
        for value in linesplit:
            if value in counter:
                counter[value] += 1
            if value not in counter:
                counter[value] = 1

countlst = list(counter.items())
for value in countlst:
    print(value)