def fft_shift ( x_n , f_s , N , threshold = 1e-10 , verbose = False ) :
    """
    Parameters:
    x_n         complex-valued time domain signal values as tupe
    f_s         sampling frequency
    N           the number of samples of the input sequence and the number of frequency points in the FFT output.
    Returns:

    Notes:
    1. The FFT length should be sufficient to cover the entire length of the input signal.
    2. If a signal is composed of more samples than the value specified by N, only the first N samples of this signal will be used to calculate the FFT. Any samples beyond this range will be ignored.
    """

    from scipy.fftpack import fft , fftshift
    import numpy as np

    print ( " fft_shift start" )

    X_m = fft ( x_n , N )
    if ( verbose ) : print ( f"{X_m=}")
    X_m.real[np.abs ( X_m.real ) < threshold] = 0
    X_m.imag[np.abs ( X_m.imag ) < threshold] = 0
    if ( verbose ) : print ( f"{X_m=}")

    X_m_shift = fftshift ( X_m )
    if ( verbose ) : print ( f"{X_m_shift=}")
    d_f = f_s / N
    m_shift_freq = np.arange ( - N // 2 , N // 2 ) * d_f
    if ( verbose ) : print ( f"{m_shift_freq=}")

    X_m_shift_mag = np.abs ( X_m_shift ) / N
    if ( verbose ) : print ( f"{X_m_shift_mag=}")

    #X_m_shift_phi = np.angle ( X_m_shift , deg = True )
    X_m_shift_phi = np.arctan2 ( np.imag(X_m_shift),np.real(X_m_shift))*180/np.pi # phase information
    if ( verbose ) : print ( f"{X_m_shift_phi=}")

    

    print ( " fft_shift finish" )

    return m_shift_freq , X_m_shift_mag , X_m_shift_phi

def fft ( x_n , f_s , N , threshold = 1e-10 , verbose = False ) :
    """
    Parameters:
    x_n         complex-valued time domain signal values as tupe
    f_s         sampling frequency
    N           the number of samples of the input sequence and the number of frequency points in the FFT output.
    Returns:

    Notes:
    1. The FFT length should be sufficient to cover the entire length of the input signal.
    2. If a signal is composed of more samples than the value specified by N, only the first N samples of this signal will be used to calculate the FFT. Any samples beyond this range will be ignored.
    """

    from scipy.fftpack import fft
    import numpy as np

    X_m = fft ( x_n , N )
    if ( verbose ) : print ( f"{X_m=}")
    X_m.real[np.abs ( X_m.real ) < threshold] = 0
    X_m.imag[np.abs ( X_m.imag ) < threshold] = 0
    if ( verbose ) : print ( f"{X_m=}")

    X_m_mag = np.abs ( X_m ) / N
    if ( verbose ) : print ( f"{X_m_mag=}")

    X_m_phi = np.angle ( X_m , deg = True )
    if ( verbose ) : print ( f"{X_m_phi=}")

    d_f = f_s / N
    m_freq = np.arange ( 0 , f_s , d_f )
    if ( verbose ) : print ( f"{m_freq=}")

    return m_freq , X_m_mag , X_m_phi

def dft ( x_t , f_s , N , threshold = 1.0e-10 , verbose = False ) :
    """
    Problem: funkcja generuje tylko amplitudę 1.
    Function generates positive frequency components with the Nyquist frequency.
    A general rectangular function x ( n ) can be defined as N samples containing K unity-valued samples.
    Parameters:
    x_t         signal values as tupe
    f_s         sampling frequency
    N           the number of samples of the input sequence and the number of frequency points in the DFT output.
    Returns:
    ( n , x_n ) time base (n) and the pulse x(n) as tuple

    Notes:
    
    """
    import numpy as np
    # Historia utworzenia funkcji https://chatgpt.com/share/e7a46f16-564f-4490-b71f-466276daa8bb
    # x_t: próbki sygnału w dziedzinie czasu
    # N: liczba próbek w sygnale
    half_N = N // 2 + 1  # Liczba elementów do analizy dla obu przypadków
    # X_m_mag = np.zeros ( half_N )  # Amplitudy w dziedzinie częstotliwości
    # X_m_phi = np.zeros ( half_N )  # Fazy w dziedzinie częstotliwości
    result = np.zeros ( ( half_N , 3 ) )  # Kolumny: częstotliwość, amplituda, faza

    for m in range ( half_N ) :
        X_m_freq = m * f_s / N
        X_m = 0j  # Inicjalizacja składowej częstotliwości jako liczby zespolonej
        for n in range ( N ) :
            X_m += x_t[n] * np.exp ( -2j * np.pi * m * n / N )
            real_part = X_m.real if np.abs ( X_m.real ) >= threshold else 0.0
            imag_part = X_m.imag if np.abs ( X_m.imag ) >= threshold else 0.0
            X_m = complex ( real_part , imag_part )
        # Ustawienie zerowej amplitudy i fazy dla małych wartości
        X_m /= N  # Skalowanie przez liczbę próbek
        if m == 0 or m == N//2:  # Nie podwajamy dla składnika DC i Nyquista
            X_m_mag = np.abs(X_m)
        else:
            X_m_mag = 2 * np.abs(X_m)  # Podwajanie amplitudy dla odpowiedzi częstotliwości
        X_m_phi = np.angle ( X_m , deg = True )  # Obliczanie fazy
        result [m] = [ X_m_freq , X_m_mag , X_m_phi ]
        if ( verbose ) : print ( f"{result[m]=}") 

    return result
