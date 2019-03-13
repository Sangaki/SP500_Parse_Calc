import datas
import datetime

start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")  # здесь мы генерим массив дат
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")  # формат во второй переменной ГГГГ-ММ-ДД

df = datas.get_data()

results = datas.data_to_cvs(df)
print(results)

rez = datas.filling_empty_days(results, start, end)
print(rez)

new_rez = datas.sequence(rez, start)
print(new_rez[0][0][1])                                                                                                          #  итоговый массив формата [интервал][дата][значение]


