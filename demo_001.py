import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import timeit


sys.path.append ( os.path.join ( 'C:/Users/mzeml/python/digital_mod_using_python_book/' ) ) # search path
# from dsp.generate_signal import gen_wave_signal # import function
import dsp.gen_signal as gen_signal
import dsp.ft as ft
from dsp.plot_signal import plot_signal # import function

np.set_printoptions ( formatter = { "float_kind" : lambda x : "%g" % x } )

timeit_tries = 1000

N = 80
f_s = 8000

# ( t , x_n ) = gen_signal.wave ( 1 , 10 , 2000.0 , f_s , N , 1/2*np.pi , 10 , 1 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# plot_signal ( t , x_n )
# ( t , x_n ) = gen_signal.rect_pulse ( 10 , f_s , N , 3 , 0 , 0 , 0 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# plot_signal ( t , x_n )
( t , x_n ) = gen_signal.chirp ( 1 , f_s , N , 1000 , 1100 , 0 , 'linear' , True , 1 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
plot_signal ( t , x_n )

#czas = timeit.timeit ( 'ft.dft ( x_n , f_s , N )' , setup = 'import dsp.ft as ft ; from __main__ import x_n , f_s , N' , number = timeit_tries )
#print ( f"{czas=}")
X_m = ft.dft ( x_n , f_s , N , verbose = False )
ft.plot_dft ( X_m[:, 0] , X_m[:, 1] , X_m[:, 2] )

( m_freq , X_m_mag , X_m_phi ) = ft.fft ( x_n , f_s , N , verbose = False )
ft.plot_dft ( m_freq , X_m_mag , X_m_phi )
#czas = timeit.timeit ( 'ft.fft ( x_n , f_s , N )' , setup = 'import dsp.ft as ft ; from __main__ import x_n , f_s , N' , number = timeit_tries )
#print ( f"{czas=}")