import pandas_datareader.data as web
import datetime
import csv


def get_data():
    start = datetime.datetime(2006, 1, 1)
    end = datetime.datetime(2016, 1, 1)

    df = web.DataReader('^GSPC', 'yahoo', start=start, end=end)
    return df


def data_to_cvs(df):
    header = ['Close']
    df.to_csv('csvvvv.csv', columns=header)

    results = []

    with open("csvvvv.csv") as csvfile:
        reader = csv.reader(csvfile, quotechar=',')  # change contents to floats
        for row in reader:  # each row is a list
            results.append(row)
    return results


def filling_empty_days(results, start, end):

    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    rez = []
    for i in range(len(date_generated)):
        rez.append([date_generated[i], 0])

    for i in range(1, len(results)):
        for j in range(i, len(date_generated)):
            if datetime.datetime.strptime(results[i][0], "%Y-%m-%d") == date_generated[j]:
                rez[j][1] = results[i][1]
                break
    prev_non_zero = 0

    if rez[0][1] == 0:
        for i in range(0, len(rez)):
            if rez[i][1] != 0:
                next_non_zero = rez[i][1]
                for j in range(0, i):
                    rez[j][1] = next_non_zero
                break

    not_zero = True
    j = -1

    for i in range(0, len(rez)):  # Проходим по циклу, ищем нули, заполняем их средним
        if (rez[i][1] == 0) and not_zero:
            prev_non_zero = float(rez[i - 1][1])
            j = i
            not_zero = False
        if (rez[i][1] != 0) and not not_zero:
            next_non_zero = float(rez[i][1])
            middle_value = (prev_non_zero + next_non_zero) / 2
            for each in range(j, i):
                rez[each][1] = str(middle_value)
            not_zero = True
    return rez


def floating_mass(rez):
    for i in range(len(rez)):
        rez[i][1] = float(rez[i][1])
    return rez


def sequence(rez, start):
    curr_year = start.year
    curr_month = start.month

    start_dt = curr_month + curr_year * 12

    end_dt = rez[len(rez) - 1][0].month + rez[len(rez) - 1][0].year * 12

    new_rez = []
    voidamas = []

    for i in range(start_dt, end_dt, 2):
        temp = []
        curr_month = i % 12
        curr_year = i // 12

        for j in range(len(rez)):
            if (rez[j][0].month == curr_month or rez[j][0].month == curr_month + 1) and rez[j][0].year == curr_year:
                temp.append(rez[j])
            elif temp != voidamas:
                new_rez.append(temp)
                break

    return new_rez
