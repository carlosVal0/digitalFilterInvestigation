import matplotlib.pyplot as plt
import numpy as np
import digitalFilters

Fs = 44100
f = 400
f2 = 800
sample = 300
x = np.arange(sample)
y1 = np.sin(2 * np.pi * f * x / Fs)
y2 = np.sin(2*np.pi*f2*x/Fs)
y3 = y1 + y2
y4 = digitalFilters.resonatorFilter(0.9,Fs,f,x,y3)
print(y4)
plt.figure()
plt.plot(x, y3,'red')
plt.plot(x,y4,'blue')
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()
