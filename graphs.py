import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FixedLocator
import numpy as np

weeks = mdates.WeekdayLocator()  # every month
days = mdates.DayLocator()
weekFmt = mdates.DateFormatter('%Y-%m-%d')


def plot(data):
    xena = []
    yetta = []
    for i in range(len(data)):
        xena.append(data[i][0])
        yetta.append(float(data[i][1]))

    fig, ax = plt.subplots()

    ax.plot(xena, yetta)

    ax.xaxis.set_major_locator(weeks)
    ax.xaxis.set_major_formatter(weekFmt)
    ax.xaxis.set_minor_locator(days)
    # ax.yaxis.set_major_locator(FixedLocator(np.arange(max(yetta), max(yetta), 1)))

    datemin = np.datetime64(xena[0], 'm')
    datemax = np.datetime64(xena[-1], 'm') + np.timedelta64(3, 'D')

    ax.set_xlim(datemin, datemax)

    ax.set_xlabel('Дата')
    ax.set_ylabel('Close')

    def fatah(x):
        return '%1.2f' % x
    ax.format_ydata = fatah

    ax.grid(True)

    fig.autofmt_xdate()

    plt.show()
