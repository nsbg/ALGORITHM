# Silver 5

import sys

grade_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total_credit = 0
total_score = 0

for _ in range(20):
    subject_info = sys.stdin.readline().split()

    if subject_info[2] in grade_score.keys():
        credit, grade = float(subject_info[1]), subject_info[2]

        total_credit += credit

        total_score += (credit*grade_score[grade])

print(total_score/total_credit)