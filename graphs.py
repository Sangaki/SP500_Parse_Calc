import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

weeks = mdates.WeekdayLocator()  # every month
days = mdates.DayLocator()
weekFmt = mdates.DateFormatter('%Y-%m-%d')


def plot(data):
    xena = []
    yetta = []
    for i in range(len(data)):
        xena.append(data[i][0])
        yetta.append(data[i][1])

    fig, ax = plt.subplots()

    ax.plot(xena, yetta)

    ax.xaxis.set_major_locator(weeks)
    ax.xaxis.set_major_formatter(weekFmt)
    ax.xaxis.set_minor_locator(days)

    datemin = np.datetime64(xena[0], 'm')
    datemax = np.datetime64(xena[-1], 'm') + np.timedelta64(3, 'D')
    ax.set_xlim(datemin, datemax)

    ax.set_xlabel('Дата')
    ax.set_ylabel('Close')
    ax.grid(True)

    #TODO форматирование xdata для корректного отображения grid'a и нормального внешнего вида

    fig.autofmt_xdate()

    plt.show()
