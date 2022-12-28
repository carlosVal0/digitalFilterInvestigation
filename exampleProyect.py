import matplotlib.pyplot as plt
import numpy as np


Fs = 8000
f = 400
f2 = 800
sample = 300
t = np.arange(0,60,1.0/Fs)
y1 = np.sin(2 * np.pi * f * t/ Fs)
y2 = np.sin(2*np.pi*f2*t/Fs)
yerr = 0.1 * np.random.normal(size=len(t)) 
plt.plot(t, y1 + yerr,'red')
plt.plot(t,y2,'blue')
plt.xlabel('Sample(n)')
plt.ylabel('voltage(V)')
plt.show()

print("EOF")