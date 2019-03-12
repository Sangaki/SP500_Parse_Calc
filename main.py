import pandas_datareader.data as web
import datetime
import csv
import pandas as pd


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

df = web.DataReader('^GSPC', 'yahoo', start=start, end=end)

header = ['Close']
f = df.to_csv('csvvvv.csv', columns=header)

results = []

with open("csvvvv.csv") as csvfile:
    reader = csv.reader(csvfile, quotechar=',') # change contents to floats
    for row in reader: # each row is a list
        results.append(row)


start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")                                                              #здесь мы генерим массив дат
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")                                                                #формат во второй переменной ГГГГ-ММ-ДД
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]


rez = []
for i in range(len(date_generated)):
    rez.append([datetime.datetime.strftime(date_generated[i], "%Y-%m-%d"), 0])

print(rez)

for i in range(1, len(results)):
    for j in range(i, len(date_generated)):                                                                             #нужно подождать секунд 15-20(слишком много жрет циклов)
        if datetime.datetime.strptime(results[i][0], "%Y-%m-%d") == date_generated[j]:
            rez[j][1] = results[i][1]                                                                                   
print(rez)
