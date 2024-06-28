def sine_wave_gen ( f , f_s , osr , phase_shift , nCyl ) :
    """
    Generate sine wave signal with the following parameters
    Parameters:
    f : frequency of sine wave in Hertz
    osr : oversampling rate (integer)
    phase_shift : desired phase_shift shift in radians
    nCyl : number of cycles of sine wave to generate
    Returns:
    (t,g) : time base (t) and the signal g(t) as tuple
    Example:
    f=10; osr=30;
    phase_shift = 1/3*np.pi ; nCyl = 5;
    (t,g) = sine_wave(f,osr,phase_shift,nCyl)
    """

    import numpy as np
    
    f_os = osr * f_s # sampling frequency
    t = np.arange ( 0 , nCyl * 1 / f - 1 / f_s , 1 / f_s ) # time base
    g = np.sin ( 2 * np.pi * f * t + phase_shift ) # replace with cos if a cosine wave is desired

    return ( t , g ) # return time base and signal g(t) as tuple