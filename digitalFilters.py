import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def resonatorFilter(r,Fs,f0,t,x):
      w0 = 2*np.pi*(f0/Fs)
      b0 = (1-r)*np.sqrt(1+r**2 - 2*r*np.cos(2*w0))
      num = [b0]
      den = [1.,2*r*np.cos(w0),r**2]
      H = signal.TransferFunction(num,den)
      H = H._z_to_zinv(num,den)
      w, mag, phase = signal.bode(H)
      plt.figure()
      plt.semilogx(w, mag)    # Bode magnitude plot
      plt.figure()
      plt.semilogx(w, phase)  # Bode phase plot
      plt.show()
      return signal.lfilter(H.num,H.den,x)
