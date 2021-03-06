import datas
# import graphs
import asdasd
import datetime
import math

start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d") 
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")

df = datas.get_data()

results = datas.data_to_cvs(df)

rez = datas.filling_empty_days(results, start, end)

rez = datas.floating_mass(rez)
new_rez = datas.sequence(rez, start)
out = asdasd.diff_timeline(rez)
# graphs.plot(new_rez[0])

summ = 0
for i in range(len(rez)):
    summ += rez[i][1]
summ /= len(rez)  # среднее арифметическое ВСЕХ данных (всех отрезков)
summ_i = 0
square_temp = 0
z = []
for each in range(len(new_rez)):
    for j in range(len(new_rez[each])):
        summ_i += new_rez[each][j][1]
    summ_i /= len(new_rez[each])
    square_temp += math.pow((summ_i - summ), 2)
    if each != 0:
        z.append((summ - summ_i) + z[each-1])
    else:
        z.append(summ - summ_i)
    summ_i = 0

s = math.sqrt(square_temp/len(new_rez))
alpha = 1.5708 
r = max(z) - min(z)
h = math.log(r/s)/math.log(alpha*len(new_rez))
print('R = ', r)
print('S = ', s)
print('Z = ', z)
print('H = ', h)

k = 1.3 + h

print('k = ', k)
