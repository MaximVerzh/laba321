from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap

x = [0, 2, 4, 6, 8, 10]
y = [241, 187, 148, 134, 121, 110]

model5 = np.poly1d (np.polyfit (x , y , 5))


plt.grid(which='major', color = 'gray', linewidth = 0.5)
plt.minorticks_on()
plt.grid(which='minor', color = 'dimgray', linestyle = ':')

plt.title("\n".join(wrap('Калибровочный график зависимости показаний АЦП от уровня воды', 35)), loc = 'center', fontsize = 10)
plt.ylabel("Отсчеты АЦП", fontsize = 10)
plt.xlabel("Уровень воды, см", fontsize = 10)






polyline = np.linspace (0, 10, 500)
plt.scatter (x , y, c = 'cornflowerblue', label = 'Измерения')

line, = plt.plot (polyline, model5(polyline), color='orange')
plt.xlim(xmin=0)
plt.ylim(ymin = 105, ymax = 245)

line.set_label("\n".join(wrap("Калибровочная функция в диапазоне [105:245] отсчетов АЦП", 25)))
plt.legend(fontsize = 10)

plt.show()