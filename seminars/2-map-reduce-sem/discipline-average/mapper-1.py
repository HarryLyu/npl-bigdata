import sys

disciplines_dict = {}
lines = open('../data/student_disciplines.txt', 'r').read().split("\n")

for line in lines:
    if (len(line.strip()) > 0):
        lastname, discipline = line.strip().split("\t")
        if lastname in disciplines_dict:
            if disciplines_dict[lastname] < discipline:
                disciplines_dict[lastname] = discipline
        disciplines_dict[lastname] = discipline

for line in sys.stdin:
    lastname, score = line.strip().split("\t")
    print disciplines_dict[lastname] + "\t" + score