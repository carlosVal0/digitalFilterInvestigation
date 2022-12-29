import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def resonator_filter(input_signal, fs, f0):
    b, a = signal.iirnotch(f0, 10, fs)
    filtered_signal = signal.filtfilt(b, a, input_signal)
    return filtered_signal


if __name__ == "__main__":
        
    t = 0.5
    fs = 8000
    f0 = 1200
    t_array = np.arange(t*fs)

    x = np.sin(2*np.pi*f0/fs*t_array)
    x1 = np.sin(2*np.pi*60/fs*t_array)
    y = resonator_filter(x1+x,fs,t_array,f0)

    plt.figure()
    plt.plot(t_array,x1,'red')
    plt.show()

    plt.figure()
    plt.plot(t_array,x1+x,'red')
    plt.plot(t_array,y,'blue')
    plt.show()