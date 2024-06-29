def sine_wave_gen ( sin , a , f , f_s , N , p_s , osr , depict ) :
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
    t_n = np.arange ( 0 , N * t_s , t_s ) # Wyznaczenie punktów próbkowania t_n

    if ( sin ) :
        x_n = np.sin ( a * np.pi * f * t_n + p_s )
    else :
        x_n = np.cos ( a * np.pi * f * t_n + p_s )
    
    if ( depict ) :
        import matplotlib.pyplot as plt
        

    return ( t_n , x_n ) # return time base and signal as tuple