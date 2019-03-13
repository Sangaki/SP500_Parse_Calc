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
print(out)

summ = 0
for i in range(0, len(rez)):
    summ += rez[i][1]
summ /= len(rez)  # среднее арифметическое ВСЕХ данных (всех отрезков)
summ_i = 0
square_temp = 0
print(new_rez[0])
qwe = 0
for i in range(len(new_rez)):
    print(len(new_rez[qwe]), qwe)
    leng = len(new_rez[qwe]) - 1
    for j in range(0, leng):
        summ_i += new_rez[i][j][1]
    square_temp += math.pow(summ_i, 2)  # скобочка с квадратом в сумме хуйня ебаная блять я запутался
    summ_i = 0
    qwe += 1

print(square_temp)
n = 60
s = math.sqrt(square_temp/n)
print(s)
# alpha = 1.5708
# h = math.log(r/s)/math.log(alpha*n)

