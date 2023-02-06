import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.ticker as ticker

fig, ax = plt.subplots(figsize=(12, 10))

#  calculation data
x1 = [0.0673, 0.081, 0.101, 0.135, 0.202]
y = [0.00043803891256482565, 0.0005337069122397747, 0.0006617504082649303, 0.0009133139323605268, 0.0013707608019066053] # L30_v02_r5
y1 = [i * 10000 for i in y]

# linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x1, y1)

# approximation line
x2 = np.linspace(x1[0], x1[-1], len(x1))
y2 = slope * x2 + intercept

# ax.plot(x1, y1)
ax.plot(x2, y2, 'r', label='y={:.2f}x {:.2f}'.format(slope, intercept))
ax.scatter(x1, y1, label='Расчетные значения')
plt.plot([], [], ' ', label='R_sq = '+'{:.2f}'.format(r_value**2))


# ax.set_title("График зависимости случайного крена от коэффициента вариации", fontsize=16)
ax.set_xlabel("Средняя осадка S, м", fontsize=14)
ax.set_ylabel("Случайный крен i, x10⁴", fontsize=14)
# X axe step
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))

plt.legend(fontsize=14)
plt.show()
