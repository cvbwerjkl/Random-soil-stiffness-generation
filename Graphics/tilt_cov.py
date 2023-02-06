import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.ticker as ticker

fig, ax = plt.subplots(figsize=(12, 10))

#  calculation data
x1 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
y = [0.00016586914586731266, 0.00032389123108255867, 0.0005059615767009082, 0.0006675860553896048, 0.0008690286666219085, 0.0010749792081413791] # L30_s10_r5
y1 = [i * 10000 for i in y]

# linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x1, y1)

# approximation line
x2 = np.linspace(x1[0], x1[-1], len(x1))
y2 = slope * x2 + intercept

# ax.plot(x1, y1)
ax.plot(x2, y2, 'r', label='y={:.2f}x+{:.2f}'.format(slope, intercept))
ax.scatter(x1, y1, label='Расчетные значения')
plt.plot([], [], ' ', label='R_sq = '+'{:.2f}'.format(r_value**2))


# ax.set_title("График зависимости случайного крена от коэффициента вариации", fontsize=16)
ax.set_xlabel("Коэффициент вариации V", fontsize=14)
ax.set_ylabel("Случайный крен i, x10⁴", fontsize=14)
# X axe step
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))

plt.legend(fontsize=14)
plt.show()
