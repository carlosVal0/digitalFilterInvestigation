import matplotlib.pyplot as plt
import numpy as np


Fs = 44100
f = 400
f2 = 800
sample = 300
x = np.arange(sample)
y1 = np.sin(2 * np.pi * f * x / Fs)
y2 = np.sin(2*np.pi*f2*x/Fs)
plt.plot(x, y1,'red')
plt.plot(x,y2,'blue')
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()

