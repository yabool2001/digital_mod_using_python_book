import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append ( os.path.join ( 'C:/Users/mzeml/python/digital_mod_using_python_book/' ) ) # search path
from dsp.signal_gen import sine_wave_gen # import function

"""
Simulate a sinusoidal signal with given sampling rate
"""
from digi_mod.signalgen import sine_wave # import the function

f = 10 #frequency = 10 Hz
overSampRate = 30 #oversammpling rate
phase = 1 / 3 * np.pi #phase shift in radians
nCyl = 5 # desired number of cycles of the sine wave
( t , g ) = sine_wave ( f , overSampRate , phase , nCyl ) #function call
plt.plot ( t , g ) # plot using pyplot library from matplotlib package
plt.title ( 'Sine wave f= ' + str (f) + ' Hz' ) # plot title
plt.xlabel ( 'Time (s)' ) # x-axis label
plt.ylabel ( 'Amplitude' ) # y-axis label
plt.show () # display the figure