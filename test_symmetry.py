import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft , fftshift

N = 8
f_s = 8000

t_s = 1.0 / f_s  # sampling period
t = np.arange ( 0 , N * t_s , t_s ) # Sampling points generation
l = np.linspace ( 0 , ( N - 1 ) * t_s , N * 10 ) # Na rysunku powinno być więcej punktów niż do analizy
print ( f"{t=}" )
# print ( f"{l=}" )

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


X_m = fft ( x_n )
threshold = 1e-10
X_m.real[np.abs ( X_m.real ) < threshold] = 0
X_m.imag[np.abs ( X_m.imag ) < threshold] = 0
print ( f"{X_m=}")
X_m_shift = fftshift ( X_m )
print ( f"{X_m_shift=}")
