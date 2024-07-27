import os
import sys

sys.path.append ( os.path.join ( 'C:/Users/mzeml/python/digital_mod_using_python_book/' ) ) # search path
from dsp.modem import PSKModem #import the PSKModem class from modem.py
import numpy as np

M = 16 # 16 points in the constellation
pskModem = PSKModem ( M ) # create a 16-PSK modem object
# pskModem.plotConstellation () # plot ideal constellation for this modem
nSym = 10 # 10 symbols as input to PSK modem
inputSyms = np.random.randint ( low = 0 , high = M , size = nSym ) # uniform random symbols from 0 to M-1
# array ( [ 10 , 14 , 1 , 0 , 0 , 1 , 10 , 0 , 14 , 5 ] )
modulatedSyms = pskModem.modulate ( inputSyms ) #modulate
# array ( [ -0.5 -0.5j , 0.5 - 0.5j , 0.65 + 0.27j , 0.707 + 0.j , 0.707 + 0.j , 0.65 + 0.27j , -0.5 - 0.5j , 0.707 + 0.j , 0.5 - 0.5j , -0.27 + 0.65j ] )
detectedSyms = pskModem.demodulate ( modulatedSyms ) #demodulate
# array ( [ 10 , 14 , 1 , 0 , 0 , 1 , 10 , 0 , 14 , 5 ] , dtype = int64 )
pass