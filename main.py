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
out = asdasd.diff_timeline(rez)
# TODO ПОЧЕМУ ПОСЛЕ ВЫПОЛНЕНИЯ ЭТОЙ ФУНКЦИИ В new_rez НА ПЕРВОМ ИНТЕРВАЛЕ ДИФФЕРЕНЦИРОВАННЫЕ ЗНАЧЕНИЯ???????

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
    square_temp += math.pow((summ_i - summ), 2)  # скобочка с квадратом в сумме хуйня ебаная блять я запутался
    if each != 0:
        z.append((summ - summ_i) + z[each-1])
    else:
        z.append(summ - summ_i)
    summ_i = 0

s = math.sqrt(square_temp/len(new_rez))
alpha = 1.5708  # по той формуле можно альфу на 0.5 поменять и тогда h=0.4011
r = max(z) - min(z)
h = math.log(r/s)/math.log(0.5*alpha*len(new_rez))

# print('H = ', h)

k = 1.3 + h

# print('k = ', k)
