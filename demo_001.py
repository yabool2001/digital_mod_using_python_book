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

timeit_tries = 1000

N = 8
f_s = 8000

( t , x_n ) = gen_signal.wave ( 1 , 10 , 2000.0 , f_s , N , 1/2*np.pi , 10 , 1 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
plot_signal ( t , x_n )
# ( t , x_n ) = gen_signal.rect_pulse ( 1 , f_s , N , 3 , 0 , 0 , 0 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# plot_signal ( t , x_t )
# ( t , x_n ) = gen_signal.chirp ( 1 , 1500 , 1000 , 10 , 50 , 0 , 'linear' , True , 1 ) #fi phase = 1 / 3 * np.pi #phase shift in radians
# plot_signal ( t , x_n )

czas = timeit.timeit ( 'ft.dft ( x_n , f_s , N )' , setup = 'import dsp.ft as ft ; from __main__ import x_n , f_s , N' , number = timeit_tries )
print ( f"{czas=}")
# Obliczenie DFT
X_m = ft.dft ( x_n , f_s , N )
# Wyświetlenie wyników
print ( f"{X_m=}")

plt.figure ( figsize = ( 10 , 5 ) )
plt.subplot ( 211 )
plt.stem ( X_m[:, 0] , X_m[:, 1] , 'b' ,  markerfmt = " " , basefmt = "-b" )
plt.ylabel ( 'Magnitude of X(m) |X(freq)|' )

plt.subplot ( 212 )
plt.stem ( X_m[:, 0] , X_m[:, 2] , 'b', markerfmt = " ", basefmt = "-b" )
plt.xlabel ( 'Freq (Hz)' )
plt.ylabel ( 'Phase Angle of X(m) Xphi(freq)' )
plt.show ()

( m_freq , X_m_mag , X_m_phi ) = ft.fft ( x_n , f_s , N )
ft.plot_dft ( m_freq , X_m_mag , X_m_phi )
czas = timeit.timeit ( 'ft.fft ( x_n , f_s , N )' , setup = 'import dsp.ft as ft ; from __main__ import x_n , f_s , N' , number = timeit_tries )
print ( f"{czas=}")