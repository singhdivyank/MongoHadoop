import sys

sc = {}

for line in sys.stdin:

    roll_no, marks = line.split('\t')

    sc[roll_no] = marks

final = {k: v for k, v in sorted(sc.items(), key=lambda item: int(item[1]), reverse=True)}

for k,v in final.items():

    print("Highest marks is ", int(v), " by Roll Number", k)
    break