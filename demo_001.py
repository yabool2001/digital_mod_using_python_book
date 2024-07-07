import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append ( os.path.join ( 'C:/Users/mzeml/python/digital_mod_using_python_book/' ) ) # search path
# from dsp.generate_signal import gen_wave_signal # import function
import dsp.gen_signal as gen_signal
from dsp.plot_signal import plot_signal # import function

# ( n , x_n ) = gen_signal.wave ( 1 , 2 , 2000.0 , 8000.0 , 8 , 0 , 10 , 1 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# plot_signal ( n , x_n )
( n , x_n ) = gen_signal.rect_pulse ( 1 , 1 , 12 , 3 , 0 , 0 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
plot_signal ( n , x_n )
