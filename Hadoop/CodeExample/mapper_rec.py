import sys


for i in range(1,5):

    file_name = sys.argv[i]

    with open(str(file_name), "r") as file:

        lines = file.read().splitlines()

        for line in lines:

            roll_no, marks = line.split(' ')

            print(roll_no, "\t", marks)