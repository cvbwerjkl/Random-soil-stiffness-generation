import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.ticker as ticker


def total(x, y):
    fig, ax = plt.subplots(figsize=(12, 10))

    x1 = [i * 10000 for i in x]
    y1 = [i * 10000 for i in y]

    # linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x1, y1)

    # approximation line
    x2 = np.linspace(min(x1), max(x1), len(x1))
    y2 = slope * x2 + intercept

    # ax.plot(x1, y1)
    ax.plot(x2, y2, 'r', label='y={:.2f}x{:.2f}'.format(slope, intercept))
    ax.scatter(x1, y1, label='Расчетные значения')
    plt.plot([], [], ' ', label='R_sq = ' + '{:.2f}'.format(r_value ** 2))

    # ax.set_title("График зависимости случайного крена от коэффициента вариации", fontsize=16)
    ax.set_xlabel("Вычисленное значение, x10⁴", fontsize=14)
    ax.set_ylabel("Случайный крен i, x10⁴", fontsize=14)
    # X axe step
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    #ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

    plt.legend(fontsize=14)
    plt.show()

    return


if __name__ == "__main__":
    x = []
    y = []
    with open('output.txt') as f:
        for i in f:
            d = i.split()
            x.append(float(d[0]))
            y.append(float(d[1]))
    print(x)

    xn = np.array(x)
    yn = np.array(y)

    total(xn, yn)
