#!/bin/python3

import os
import bisect

# Complete the activityNotifications function below.
def median(sorted_expenses, d):
    if d % 2 != 0:
        return sorted_expenses[int(d / 2)]
    else:
        return (sorted_expenses[int(d / 2) - 1] + sorted_expenses[int(d / 2)]) / 2

def activityNotifications(expenditure, d):
    past_d_day_exp = expenditure[:d]
    sorted_expenses = sorted(past_d_day_exp)
    notify =0
    for exp in expenditure[d:]:
        m = median(sorted_expenses,d)
        if exp >= 2*m:
            notify +=1
        position = bisect.bisect(sorted_expenses, past_d_day_exp.pop(0))
        sorted_expenses.__delitem__(position-1)
        bisect.insort(sorted_expenses, exp)
        past_d_day_exp.append(exp)
    return notify


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')

    # fptr.close()
