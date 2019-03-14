import math


def diff_timeline(otrezok):
    x = [[0] * 2 for i in range(len(otrezok))]
    out = [[0] * 2 for i in range(len(otrezok))]
    for i in range(len(otrezok)):
        x[i][0] = otrezok[i][0]
        out[i][0] = otrezok[i][0]
    for i in range(len(otrezok)-1):
        x[i][1] = math.fabs(math.log(float(otrezok[i+1][1])) - math.log(float(otrezok[i][1])))
    sum_of_x = 0
    for i in range(0, len(x)):
        sum_of_x += float(x[i][1])
    for i in range(0, len(x)):
        out[i][1] = float(x[i][1]) / sum_of_x
    return out
