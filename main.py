import datas
import graphs
import asdasd
import datetime

start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")  # здесь мы генерим массив дат
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")  # формат во второй переменной ГГГГ-ММ-ДД

df = datas.get_data()

results = datas.data_to_cvs(df)
print(results)

rez = datas.filling_empty_days(results, start, end)
print(rez)

rez = datas.floating_mass(rez)

new_rez = datas.sequence(rez, start)
print(new_rez[0][0][1])  # итоговый массив формата [интервал][дата][значение]

out = asdasd.diff_timeline(new_rez[0], start, rez)

# graphs.plot(new_rez[0])
