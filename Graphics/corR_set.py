import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.ticker as ticker

fig, ax = plt.subplots(figsize=(12, 10))

#  calculation data
x1 = [0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 15, 20]
y = [0.00010586756118610673, 0.00012041543105905459, 0.00017501244362171746, 0.00024020865477477772, 0.00034229439104381786, 0.00045816426271207144, 0.0006940762042117601, 0.0008120061740907467, 0.0008650718274189689, 0.0009261912975785378]  # L20_s10_v02
y1 = [i * 1.96 * 10000 for i in y]
x3 = [i ** 0.3333 for i in x1]

# linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x3, y1)

# approximation line
x2 = np.linspace(x1[0], x1[-1], len(x1)*100)
y2 = slope * x2 ** 0.3333 + intercept

# ax.plot(x1, y1)
ax.plot(x2, y2, 'r', label='y={:.2f} * (x^0.5) {:.2f}'.format(slope, intercept))
ax.scatter(x1, y1, label='Расчетные значения')
plt.plot([], [], ' ', label='R_sq = '+'{:.2f}'.format(r_value**2))


# ax.set_title("График зависимости случайного крена от ширины", fontsize=16)
ax.set_xlabel("Радиус корреляции r, м", fontsize=14)
ax.set_ylabel("Случайный крен i, x10⁴", fontsize=14)
# X axe step
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

plt.legend(fontsize=14)
plt.show()
