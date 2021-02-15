# Author: Tow 2//13/21

user_input = input("Enter the path to a text file on your computer: ex alice.txt`\n")

with open(user_input, "r") as infile:
    lines = 0
    number = infile.readlines()
    for line in number:
        lines += 1

print("There are {0} lines in {1}".format(lines, user_input))