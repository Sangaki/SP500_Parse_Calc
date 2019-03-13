import math
import datas
import datetime


def my_function(otrezok):
    x = []
    out = []
    for i in range(0, len(otrezok)-1):
        x[i][1] = math.fabs(math.log(float(otrezok[i+1][1])) - math.log(float(otrezok[i][1])))
    for i in range(0, len(x)):
        out[i][1] = x[i][1] / math.fsum(x)
    print(out)


start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")

df = datas.get_data()

results = datas.data_to_cvs(df)
print(results)

rez = datas.filling_empty_days(results, start, end)
print(rez)
otrez = datas.sequence(rez, start)[0]
my_function(otrez)
