import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import timeit


sys.path.append ( os.path.join ( 'C:/Users/mzeml/python/digital_mod_using_python_book/' ) ) # search path
# from dsp.generate_signal import gen_wave_signal # import function
import dsp.gen_signal as gen_signal
import dsp.ft as ft
import dsp.plot_signal as plot_signal # import function
import dsp.energy as energy # import function

np.set_printoptions ( formatter = { "float_kind" : lambda x : "%g" % x } )

timeit_tries = 1000

N = 8
f_s = 8000

#( t , x_n2 ) = gen_signal.wave ( 1 , 1 , 2000.0 , f_s , N , -1/2*np.pi , 10 , verbose = True ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# ( t , x_n4 ) = gen_signal.wave ( 1 , 4 , 4000.0 , f_s , N , 3/2*np.pi , 10 , verbose = False ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# ( t , x_n6 ) = gen_signal.wave ( 1 , 6 , 6000.0 , f_s , N , 0 , 10 , verbose = False ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# x_n = x_n2 + x_n4 + x_n6
#x_n = x_n2
( t , x_n ) = gen_signal.example_1_dft_mod ( f_s , N , 10 , verbose = True ) #fi phase = 1 / 3 * np.pi #phase shift in radians
print ( f"{x_n=}")

plot_signal.plot_signal ( t , x_n )

# ( t , x_n ) = gen_signal.rect_pulse ( 10 , f_s , N , 3 , 0 , 0 , 0 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# plot_signal ( t , x_n )

# ( t , x_n ) = gen_signal.chirp ( 1 , f_s , N , 1000 , 1100 , 0 , 'linear' , True , 1 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# plot_signal.plot_signal ( t , x_n )

#czas = timeit.timeit ( 'ft.dft ( x_n , f_s , N )' , setup = 'import dsp.ft as ft ; from __main__ import x_n , f_s , N' , number = timeit_tries )
#print ( f"{czas=}")
X_m = ft.dft ( x_n , f_s , N , verbose = True )
plot_signal.plot_dft ( X_m[:, 0] , X_m[:, 1] , X_m[:, 2] )

( m_freq , X_m_mag , X_m_phi ) = ft.fft ( x_n , f_s , N , verbose = True )
plot_signal.plot_dft ( m_freq , X_m_mag , X_m_phi )
#czas = timeit.timeit ( 'ft.fft ( x_n , f_s , N )' , setup = 'import dsp.ft as ft ; from __main__ import x_n , f_s , N' , number = timeit_tries )
#print ( f"{czas=}")

energy.power_spectrum ( x_n , N , verbose = True )

( m_shift_freq , X_m_shift_mag , X_m_shift_phi ) = ft.fft_shift ( x_n , f_s , N , verbose = True )
plot_signal.plot_dft ( m_shift_freq , X_m_shift_mag , X_m_shift_phi )