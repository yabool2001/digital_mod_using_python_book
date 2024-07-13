def fft ( x_n , f_s , N , threshold = 1e-10 ) :
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
    import matplotlib.pyplot as plt

    X_m = fft ( x_n , N )

    X_m_mag = np.abs ( X_m ) / N
    X_m_mag[np.abs ( X_m_mag ) < threshold] = 0
    print ( f"{X_m_mag=}")

    X_m_phi = np.angle ( X_m_mag , deg = True )
    X_m_phi[np.abs ( X_m_phi ) < threshold] = 0
    print ( f"{X_m_phi=}")

    d_f = f_s / N
    m_freq = np.arange ( 0 , f_s , d_f )
    print ( f"{m_freq=}")

    return m_freq , X_m_mag , X_m_phi

def dft ( x_t , f_s , N , threshold = 1e-10 ) :
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
        # Ustawienie zerowej amplitudy i fazy dla małych wartości
        X_m /= N  # Skalowanie przez liczbę próbek
        if np.abs ( X_m ) < threshold:
            X_m_mag = 0
            X_m_phi = 0  # Faza zerowa dla bardzo małych wartości amplitudy
        else:
            if m == 0 or m == N//2:  # Nie podwajamy dla składnika DC i Nyquista
                X_m_mag = np.abs(X_m)
            else:
                X_m_mag = 2 * np.abs(X_m)  # Podwajanie amplitudy dla odpowiedzi częstotliwości
            X_m_phi = np.angle ( X_m , deg = True )  # Obliczanie fazy
        result [m] = [ X_m_freq , X_m_mag , X_m_phi ]

    return result

def plot_dft ( m_freq , X_m_mag , X_m_phi ) :

    import matplotlib.pyplot as plt

    plt.figure ( figsize = ( 10 , 5 ) )
    plt.subplot ( 211 )
    plt.stem ( m_freq , X_m_mag , 'b' ,  markerfmt = " " , basefmt = "-b" )
    plt.ylabel ( 'Magnitude of X(m) |X(freq)|' )

    plt.subplot ( 212 )
    plt.stem ( m_freq , X_m_phi , 'b', markerfmt = " ", basefmt = "-b" )
    plt.xlabel ( 'Freq (Hz)' )
    plt.ylabel ( 'Phase Angle of X(m) Xphi(freq)' )
    plt.show ()