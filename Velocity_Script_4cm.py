from matplotlib import pyplot as plt
import numpy as np
import textwrap

def str_to_float(str_in):
    import re
    str_in = re.sub(r'[^\d.]', '', str_in.replace(",", "."))
    # Try to convert the string to float
    try:
        float_res = float(str_in)
    except ValueError:
        float_res = 0

    return float_res

converted_data = []

adc = open('4cm.txt', 'r')
data = adc.read()
adc_data = data.replace('\n', ' ').replace('"', '').split(" ")
for i in range(len(adc_data)):
    adc_data[i] = str_to_float(adc_data[i])

for i in range(164):
    for j in range(0, 4000, 10):
        if adc_data[2*i] < (np.polyval([0.01536, - 0.3958, 3.422, - 9.417, - 18.93, 241], j/1000) + 1) and adc_data[2*i] > (np.polyval([0.01536, - 0.3958, 3.422, - 9.417, - 18.93, 241], j/1000) - 1):
            converted_data.append(j)
            break

time = []
for i in range(1, 164, 1):
    time.append(adc_data[2*i - 1])

time.pop(80)
time.pop(79)
time.pop(78)
time.pop(77)
time.pop(76)
time.pop(75)
time.pop(74)
time.pop(73)
time.pop(72)

time1 = []
time2 = []

converted_data1 = []
converted_data2 = []

for i in range(len(converted_data)):
    converted_data[i] = converted_data[i]/100
    if converted_data[i] < 36.2:
        converted_data1.append(converted_data[i])
    elif converted_data[i] > 36.2:
        converted_data2.append(converted_data[i])
    elif converted_data[i] == 36.2:
        converted_data1.append(converted_data[i])
        converted_data2.append(converted_data[i])

for i in range(len(time)):
    if i < 17:
        time2.append(time[i])
    elif i > 17:
        time1.append(time[i])
    elif i == 17:
        time1.append(time[i])
        time2.append(time[i])

redline = []
for i in range(len(converted_data)):
    redline.append(1.675)

print(len(time))
print(len(converted_data))
print(converted_data1, converted_data2, time1, time2)

fig, ax = plt.subplots(figsize=(200, 10), dpi=100)

ax.text(10.05, 34, f"Расстояние от дверцыдо электродов: 1.4 м", fontsize = 11, color = 'black')
ax.text(10.05, 33, f"Время движения волны до электродов: 1.7 c", fontsize = 11, color = 'black')
ax.text(10.05, 32, f"Cкорость волны: 0.82 м/c", fontsize = 11, color = 'black')

ax.grid(which='major', color = 'black')
ax.minorticks_on()
ax.grid(which='minor', color = 'dimgray', linestyle = ':')

ax.set_ylabel("Уровень воды, мм", fontsize = 15)
ax.set_xlabel("Время, с", fontsize = 15)

line1, = ax.plot(time1, converted_data1, c='blue', linewidth=2)
line2, = ax.plot(time2, converted_data2, c='orange', linewidth=2)
ax.plot(redline, converted_data, '--', c ='red', linewidth = 3,)

plt.xlim(xmin = 0.0543, xmax = 15)
plt.ylim(ymin = 8, ymax = 39.5)

plt.title('Уровень воды в кювете после открытия торцевой двери', loc = 'center', fontsize = 15)
line1.set_label("Уровень воды в кювете")
line2.set_label("Ожидание волны")
ax.legend(fontsize = 12)

plt.show()

