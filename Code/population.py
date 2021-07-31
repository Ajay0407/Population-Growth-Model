import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

x = np.array([0, 10, 20, 30, 40, 50, 60])

y = np.array([3.5856000, 4.6941000, 6.1418000, 8.0286000, 10.6715000, 13.8188000, 17.2245000]) #Hindu Population 
z = np.array([30.3675000, 36.6528000, 45.3292000, 56.2389000, 69.0060000, 82.7579000, 98.0378000])  # Muslim Population

pop_m = np.polyfit(x, y, 2)
pop_h = np.polyfit(x, z, 2)

f = np.poly1d(pop_m)
pdc_m_21 =print("\n Muslims in 2021 =", f(70))

g = np.poly1d(pop_h)
pdc_h_21 = print("\n Hindus in 2021 =", g(70))
#print('Here "x" represents "Time" and "f(x)" represents "Population" \n\n')

print("\n Muslim : f \n", f)
print("\n Hindu : g \n", g)

x_new = np.linspace(-5, 70, 100)

y_new = f(x_new) #pridiction Hindu
z_new = g(x_new) # Pridiction Muslim

plt.subplot(2, 1, 1)
plt.rcParams["figure.figsize"] = (10, 5)
plt.plot(x, y,'o', color='black', label="Muslim Population")
plt.plot(70, 21.33,'o', color='red', label="pridiction in 2021")
plt.plot(x_new, y_new, '-', color='green', label="Muslim Population Curve")
plt.title("Population Growth: Polynomial")
plt.ylabel("Population (in Crore)")
plt.legend(shadow=True)
#plt.figure(figsize=(5, 7))

plt.subplot(2, 1, 2)
plt.rcParams["figure.figsize"] = (10, 5)
plt.plot(x, z,'o', color='black', label="Hindu Population")
plt.plot(70, 115.90,'o', color='red', label="pridiction in 2021")
plt.plot(x_new, z_new, '-', color='darkorange', label="Hindu Population Curve")
plt.xlabel("Time (in years, since 1951)")
plt.ylabel("Population (in Crore)")
#plt.ylim(0, 100)
plt.legend(shadow=True)
#plt.figure(figsize=(5, 20))

plt.savefig('pop_poly_growth.pdf')
plt.show()
