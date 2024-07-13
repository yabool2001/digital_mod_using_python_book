def wave ( sin , a , f , f_s , N , p_o , osr , depict ) :
    """
    Generate sine wave signal with the following parameters
    Parameters:
    sin         sinus or cosinus
    a           amplitude
    f           frequency of wave in Hertz
    f_s         sampling frequency
    N           the number of samples of the input sequence and the number of frequency points in the DFT output.
    p_o         desired phase offset in radians
    osr         oversampling rate (integer) used for plot
    depict      plot the signal
    Returns:
    ( n , x_n ) time base (n) and the signal x(n) as tuple
    """
    
    import numpy as np

    t_s = 1.0 / f_s  # sampling period
    t = np.arange ( 0 , N * t_s , t_s ) # Sampling points generation
    print ( f"{t=}" )

    if ( sin ) :
        x_n = a * np.sin ( 2 * np.pi * f * t + p_o )
    else :
        x_n = a * np.cos ( 2 * np.pi * f * t + p_o )
    
    if ( depict ) :
        import matplotlib.pyplot as plt
        l = np.linspace ( 0 , ( N - 1 ) * t_s , num = N * osr ) # Na rysunku powinno być więcej punktów niż do analizy
        if ( sin ) :
            x_t = a * np.sin ( 2 * np.pi * f * l + p_o )
        else :
            x_t = a * np.cos ( 2 * np.pi * f * l + p_o )
        plt.figure ( figsize = ( 10 , 5 ) )
        plt.plot ( l , x_t , label = 'x_t amplitude' )
        plt.scatter ( t , x_n , color = 'red' , marker = '*' , s = 100 , label = 'Samples (t)' )
        plt.title ( 'Samples of x_n input signal ' )
        plt.xlabel ( 'l' )
        plt.ylabel ( 'x_t' )
        plt.legend ()
        plt.grid ( True )
        plt.show ()

    return ( t , x_n ) # return time base and signal as tuple

def rect_pulse ( a , f_s , N , K , s , sym , depict ) :
    """
    A general rectangular function x ( n ) can be defined as N samples containing K unity-valued samples.
    Parameters:
    a           amplitude
    f_s         sampling frequency
    N           the number of samples of the input sequence and the number of frequency points in the DFT output.
    K           number of samples with amplitude value a
    s           desired K samples shift
    sym         signal symmetry around 0  
    depict      plot the signal
    Returns:
    ( n , x_n ) time base (n) and the pulse x(n) as tuple

    Notes:
    1. If you want the window to be fully symmetrical, the N and K values ​​should be odd.
    """
    
    import numpy as np

    t_s = 1.0 / f_s  # sampling period
    
    if sym :
        t = np.arange ( -N // 2 + 1 , N // 2 + 1 ) * t_s # Sampling points generation
    else :
        t = np.arange ( 0 , N )  * t_s
    print ( f"{t=}" )
    x_t = np.zeros ( N )

    s = ( N // 2 ) - ( K // 2 ) + s # Do not multiply by t_s, it isn't ncessary and will not work
    e = s + K
    if e >= 0 :
        if s < 0 : s = 0
        x_t[s:e] = a

    if ( depict ) :
        import matplotlib.pyplot as plt
        plt.figure ( figsize = ( 10 , 5 ) )
        plt.scatter ( t , x_t , color = 'red' , marker = '*' , s = 100 , label = 'Samples (n)' )
        plt.title ( 'Samples of x_n input signal ' )
        plt.xlabel ( 'n' )
        plt.ylabel ( 'x_t' )
        plt.legend ()
        plt.grid ( True )
        plt.show ()

    return ( t , x_t ) # return time base and signal as tuple

def chirp ( a , f_s , N , f_0 , f_1 , p_o , m , v_z , depict ) :
    """
    A general rectangular function x ( n ) can be defined as N samples containing K unity-valued samples.
    Parameters:
    a           amplitude
    f_s         sampling frequency
    N           the number of samples of the input sequence and the number of frequency points in the DFT output.
    K           number of samples with amplitude value a
    s           desired K samples shift
    depict      plot the signal
    Returns:
    ( n , x_n ) time base (n) and the pulse x(n) as tuple

    Notes:
    1. If you want the window to be fully symmetrical, the N and K values ​​should be odd.
    """
    
    import numpy as np
    from scipy.signal import chirp
    
    t_s = 1.0 / f_s  # sampling period
    t_1 = ( N - 1 ) * t_s
    t = np.arange ( 0 , N * t_s , t_s ) # Sampling points generation
    print ( f"{t=}" )
    print ( f"{t=} {f_s=} {f_0=} {t_1=} {f_1=} {p_o=} {m=} {p_o=} {v_z=}" )
    # x_t = chirp ( t , f_0 , t_1 , f_1 , m , p_o )
    # t =np.arange(start = 0, stop = 1,step = 1/500)
    x_t = chirp ( t , f_0 , t1 = t_1 , f1 = f_1 , phi = p_o , method = m , vertex_zero = v_z )
    if depict :
        import matplotlib.pyplot as plt
        plt.plot ( t , x_t )
        plt.show ()
    
    return ( t , x_t ) # return time base and signal as tuple