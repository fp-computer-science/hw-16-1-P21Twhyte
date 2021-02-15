# Author: Tow 2/13/21

user = input(" Enter the path to a text file on your computer: ex alma_mater.txt \n ")

with open(user, "r") as infile:
    lines = []
    count = infile.readlines()
    for number in count:
        if len(number) == 0:
            del number
        else:
            lines.append([number])
    lines.sort()

print("The longest line is {0} in {1}.".format(lines[0], user))