import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.ticker as ticker

fig, ax = plt.subplots(figsize=(12, 10))

#  calculation data
x1 = [20, 25, 30, 35, 40]
y = [0.0011565409016291773, 0.0008674769837819512, 0.000663045744471989, 0.0005255281289979596, 0.0004424574100861483]  #  s10_v02_r5
y1 = [i * 1.96 * 10000 for i in y]
x3 = [1/i for i in x1]

# linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x3, y1)

# approximation line
x2 = np.linspace(x1[0], x1[-1], len(x1)*100)
y2 = slope / x2 + intercept

# ax.plot(x1, y1)
ax.plot(x2, y2, 'r', label='y={:.2f}/x{:.2f}'.format(slope, intercept))
ax.scatter(x1, y1, label='Расчетные значения')
plt.plot([], [], ' ', label='R_sq = '+'{:.2f}'.format(r_value**2))


# ax.set_title("График зависимости случайного крена от ширины", fontsize=16)
ax.set_xlabel("Ширина здания L, м", fontsize=14)
ax.set_ylabel("Случайный крен i, x10⁴", fontsize=14)
# X axe step
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

plt.legend(fontsize=14)
plt.show()
