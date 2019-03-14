import math


def diff_timeline(otrezok):
    x = otrezok
    out = x
    for i in range(0, len(otrezok)-1):
        x[i][1] = math.fabs(math.log(otrezok[i+1][1]) - math.log(otrezok[i][1]))
    sum_of_x = 0
    for i in range(0, len(x)):
        sum_of_x += float(x[i][1])
    for i in range(0, len(x)):
        out[i][1] = float(x[i][1]) / sum_of_x
    return out
