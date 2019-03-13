import math
import datas
import datetime


def diff_timeline(otrezok):
    x = otrez
    out = x
    for i in range(0, len(otrezok)-1):
        x[i][1] = math.fabs(math.log(float(otrezok[i+1][1])) - math.log(float(otrezok[i][1])))
    sum_of_x = 0
    for i in range(0, len(x)):
        sum_of_x += float(x[i][1])
    for i in range(0, len(x)):
        out[i][1] = float(x[i][1]) / sum_of_x
    print(out)


start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")

df = datas.get_data()

results = datas.data_to_cvs(df)

rez = datas.filling_empty_days(results, start, end)
otrez = datas.sequence(rez, start)[0]
my_function(otrez)

