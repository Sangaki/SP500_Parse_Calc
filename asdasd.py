import math
import datas
import datetime
import graphs


def diff_timeline(otrezok):
    x = otrezok
    out = x
    print('lulkappa', type(otrezok[len(otrezok)-1][1]))
    for i in range(0, len(otrezok)-1):
        x[i][1] = math.fabs(math.log(float(otrezok[i+1][1])) - math.log(float(otrezok[i][1])))
    x[len(otrezok)][1] = math.fabs(math.log(float(datas.sequence(rez, start)[1][0][1])) -
                                   math.log(float(otrezok[len(otrezok)-1][1])))
    print(x[len(x)])
    sum_of_x = 0
    for i in range(0, len(x)):
        sum_of_x += float(x[i][1])
    for i in range(0, len(x)):
        out[i][1] = float(x[i][1]) / sum_of_x
    print('its out)')
    print(out)
    print(sum_of_x)

    return out


start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")

df = datas.get_data()

results = datas.data_to_cvs(df)
# print(results)

rez = datas.filling_empty_days(results, start, end)
# print(rez)
otrez = datas.sequence(rez, start)[0]
out = diff_timeline(otrez)

graphs.plot(out)
