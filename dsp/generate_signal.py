def generate_wave_signal ( sin , a , f , f_s , N , p_s , osr , depict ) :
    """
    Generate sine wave signal with the following parameters
    Parameters:
    f : frequency of sine wave in Hertz

    osr         oversampling rate (integer) for plot
    p_s         desired phase shift in radians
    N :         number of
    depict      plot the signal
    Returns:
    ( t , g )   time base (t) and the signal g(t) as tuple
    """
    
    import numpy as np

    t_s = 1.0 / f_s  # Okres próbkowania
    n = np.arange ( 0 , N * t_s , t_s ) # Wyznaczenie punktów próbkowania n
    print ( f"{n=}" )

    if ( sin ) :
        x_n = np.sin ( a * np.pi * f * n + p_s )
    else :
        x_n = np.cos ( a * np.pi * f * n + p_s )
    
    if ( depict ) :
        import matplotlib.pyplot as plt
        t = np.linspace ( 0 , ( N - 1 ) * t_s , num = N * osr ) # Na rysunku powinno być więcej punktów niż do analizy
        if ( sin ) :
            x_t = np.sin ( a * np.pi * f * t + p_s )
        else :
            x_t = np.cos ( a * np.pi * f * t + p_s )
        plt.figure ( figsize = ( 10 , 5 ) )
        plt.plot ( t , x_t , label = 'x_t amplitude' )
        plt.scatter ( n , x_n , color = 'red' , marker = '*' , s = 100 , label = 'Samples (n)' )
        plt.title ( 'Samples of x_n input signal ' )
        plt.xlabel ( 't' )
        plt.ylabel ( 'x_t' )
        plt.legend ()
        plt.grid ( True )
        plt.show ()

    return ( n , x_n ) # return time base and signal as tuple