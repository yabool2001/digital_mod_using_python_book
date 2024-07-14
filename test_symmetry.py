import matplotlib.pyplot as plt
import numpy as np

N = 8
f_s = 8000

t_s = 1.0 / f_s  # sampling period
t = np.arange ( 0 , N * t_s , t_s ) # Sampling points generation
l = np.linspace ( 0 , ( N - 1 ) * t_s , num = N * osr ) # Na rysunku powinno być więcej punktów niż do analizy
print ( f"{t=}" )
print ( f"{l=}" )

x_n = np.cos ( 2 * np.pi * 1000 * t + np.pi )
x_l = np.cos ( 2 * np.pi * 1000 * l + np.pi )
print ( f"{x_n=}")

plt.figure ( figsize = ( 10 , 5 ) )
plt.plot ( l , x_l , label = 'x_t amplitude' )
plt.scatter ( t , x_n , color = 'red' , marker = '*' , s = 100 , label = 'Samples ( l = N * osr )' )
plt.title ( 'Samples of x_l input signal ' )
plt.xlabel ( 'l' )
plt.ylabel ( 'x_l' )
plt.legend ()
plt.grid ( True )
plt.show ()

X_m = ft.dft ( x_n , f_s , N , verbose = True )
plot_signal.plot_dft ( X_m[:, 0] , X_m[:, 1] , X_m[:, 2] )

( m_freq , X_m_mag , X_m_phi ) = ft.fft ( x_n , f_s , N , verbose = True )
plot_signal.plot_dft ( m_freq , X_m_mag , X_m_phi )
#czas = timeit.timeit ( 'ft.fft ( x_n , f_s , N )' , setup = 'import dsp.ft as ft ; from __main__ import x_n , f_s , N' , number = timeit_tries )
#print ( f"{czas=}")

energy.power_spectrum ( x_n , N , verbose = True )

( m_shift_freq , X_m_shift_mag , X_m_shift_phi ) = ft.fft_shift ( x_n , f_s , N , verbose = True )
plot_signal.plot_dft ( m_shift_freq , X_m_shift_mag , X_m_shift_phi )