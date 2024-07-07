import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append ( os.path.join ( 'C:/Users/mzeml/python/digital_mod_using_python_book/' ) ) # search path
from dsp.generate_wave_signal import generate_wave_signal # import function
from dsp.plot_signal import plot_sine_wave # import function

( n , x_n ) = generate_wave_signal ( 1 , 2 , 2000.0 , 8000.0 , 8 , 0 , 10 , 1 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
plot_sine_wave ( n , x_n )
# x_t_plot = np.sin ( 2 * np.pi * freq1 * t_plot ) + 0.5 * np.sin ( 2 * np.pi * freq2 * t_plot + 3 * np.pi/4 )