import datas
import graphs
import asdasd
import datetime
import math

start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")  # здесь мы генерим массив дат
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")  # формат во второй переменной ГГГГ-ММ-ДД

df = datas.get_data()

results = datas.data_to_cvs(df)
#  print(results)

rez = datas.filling_empty_days(results, start, end)
#  print(rez)

rez = datas.floating_mass(rez)

new_rez = datas.sequence(rez, start)
# print(new_rez[0][0][1])  # итоговый массив формата [интервал][дата][значение]

out = asdasd.diff_timeline(new_rez[0], start, rez)

# graphs.plot(new_rez[0])

summ = 0
for i in range(0, len(rez)):
    summ += rez[i][1]
summ /= len(rez)  # среднее арифметическое ВСЕХ данных (всех отрезков)
summ_i = 0
square_temp = 0
z = []
qwe = 0
for each in range(len(new_rez)):
    leng = len(new_rez[qwe]) - 1
    for j in range(0, len(new_rez[qwe])):
        summ_i += new_rez[qwe][j][1]
    summ_i /= len(new_rez[qwe])
    square_temp += math.pow((summ_i - summ), 2)  # скобочка с квадратом в сумме хуйня ебаная блять я запутался
    z.append(summ - summ_i)
    summ_i = 0
    qwe += 1

print('huynya = ', square_temp)
print('z = ', z)
print('summ z = ', math.fsum(z))
s = math.sqrt(square_temp/len(new_rez))
print('s = ', s)
alpha = 1.5708
r = max(z) - min(z)
print('R = ', r)

h = math.log(r/s)/math.log(alpha*len(new_rez))

print('H = ', h)
